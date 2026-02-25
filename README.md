# Sleep Inhibitor for KDE

A simple KDE application to prevent system sleep using systemd-inhibit. Perfect for preventing your system from sleeping during long-running tasks, downloads, or presentations.

## Features

- **Indefinite or Timed Inhibition**: Choose to prevent sleep indefinitely or for a specific duration
- **Visual Countdown Timer**: See exactly how much time remains in timed sessions
- **System Tray Integration**: Minimize to tray and monitor status at a glance
- **Preset Management**: Create and manage custom preset time intervals for quick access
- **Clear Status Indicators**: Always know whether sleep inhibition is active
- **Native KDE Integration**: Designed to work seamlessly with KDE Plasma

## System Requirements

- Linux with systemd
- Python 3.6+
- PyQt5
- systemd-inhibit command (usually included with systemd)

## Installation

### Installing PyQt5

First, install PyQt5 using your system package manager (recommended):

**Debian/Ubuntu/KDE Neon:**
```bash
sudo apt install python3-pyqt5
```

**Fedora:**
```bash
sudo dnf install python3-qt5
```

**Arch Linux:**
```bash
sudo pacman -S python-pyqt5
```

**Alternative (using pip):**
If you prefer to use pip, create a virtual environment first:
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Quick Install (Recommended)

Run the installation script to set everything up automatically:

```bash
chmod +x install.sh
./install.sh
```

This will:
- Install Python dependencies (if using pip)
- Create a desktop entry for KDE
- Make the application available in your application menu

### Manual Installation

1. Install PyQt5 (see above)

2. Make the main script executable:
```bash
chmod +x main.py
```

3. Run the application:
```bash
python3 main.py
```

### Verify Installation

Run the test script to check if everything is properly set up:

```bash
python3 test_setup.py
```

## Usage

### Starting the Application

- From KDE Application Menu: Search for "Sleep Inhibitor"
- From Terminal: `python3 main.py`
- From File Manager: Double-click `main.py`

### Using Sleep Inhibition

1. **Choose a Mode**:
   - **Indefinite**: Prevents sleep until you manually stop it
   - **Timed**: Prevents sleep for a specific duration

2. **Set Duration** (for Timed mode):
   - Select a preset from the dropdown (e.g., "30 minutes", "1 hour")
   - Or enter a custom duration using hours and minutes

3. **Start Inhibition**:
   - Click "Start Inhibit"
   - The status will change to "Active" and turn green/orange
   - For timed sessions, a countdown timer will display

4. **Monitor Status**:
   - Main window shows current status and countdown
   - System tray icon shows active/inactive status
   - Hover over tray icon to see remaining time

5. **Stop Inhibition**:
   - Click "Stop Inhibit" to allow sleep again
   - Or close the application (which stops inhibition automatically)

### Managing Presets

1. Click "Manage" button in the Duration section
2. Add new presets with custom names and durations
3. Remove presets you no longer need
4. Presets are saved automatically and persist between sessions

### System Tray

- Click the tray icon to show/hide the main window
- Right-click for quick menu:
  - Show: Bring window to front
  - Quit: Stop inhibition and exit application

## Configuration

Presets and settings are stored in:
```
~/.config/sleep-inhibitor/config.json
```

Default presets include:
- 15 minutes
- 30 minutes
- 1 hour
- 2 hours
- 4 hours

## How It Works

The application uses `systemd-inhibit` to prevent the system from sleeping. When you start sleep inhibition:

- **Indefinite mode**: Runs `systemd-inhibit --what=sleep sleep infinity`
- **Timed mode**: Runs `systemd-inhibit --what=sleep sleep <duration>`

This creates a sleep inhibitor lock that prevents the system from entering sleep mode. The lock is automatically released when:
- You click "Stop Inhibit"
- The timer expires (in timed mode)
- You close the application
- The application crashes (systemd handles cleanup)

## Troubleshooting

### "Failed to start sleep inhibition" error

This usually means `systemd-inhibit` is not available. Check if it's installed:
```bash
which systemd-inhibit
```

If not found, install systemd (it's usually installed by default on most modern Linux distributions).

### Application doesn't appear in KDE menu

Run the install script again, or manually update the desktop database:
```bash
update-desktop-database ~/.local/share/applications
```

### System still goes to sleep

Some laptop lid or power button settings may override sleep inhibition. Check your power management settings in KDE System Settings.

## License

This application is free and open source. Use it however you like!
