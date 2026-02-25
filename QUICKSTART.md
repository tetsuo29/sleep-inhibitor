# Quick Start Guide

Get up and running with Sleep Inhibitor in under 5 minutes!

## Step 1: Install PyQt5

Choose your distribution:

**Ubuntu/Debian/KDE Neon:**
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

## Step 2: Run the Installation Script

```bash
chmod +x install.sh
./install.sh
```

## Step 3: Launch the Application

### Option A: From Application Menu
1. Open KDE Application Launcher
2. Search for "Sleep Inhibitor"
3. Click to launch

### Option B: From Terminal
```bash
python3 main.py
```

## Step 4: Use It!

### For Quick Tasks (Use Presets)
1. Select **Timed** mode
2. Choose a preset: "30 minutes", "1 hour", etc.
3. Click **Start Inhibit**
4. Your computer won't sleep for that duration

### For Long Tasks (Indefinite)
1. Select **Indefinite** mode
2. Click **Start Inhibit**
3. Your computer won't sleep until you click **Stop Inhibit**

### For Custom Durations
1. Select **Timed** mode
2. Choose **Custom** and enter hours and minutes
3. Click **Start Inhibit**

## Tips

- **System Tray**: The app minimizes to the system tray. Click the icon to show/hide the window.
- **Custom Presets**: Click "Manage" to add your own time presets (e.g., "Download time - 3 hours")
- **Check Status**: The window always shows if sleep inhibition is active and how much time remains

## Troubleshooting

### Can't find the app in the menu?
Run:
```bash
update-desktop-database ~/.local/share/applications
```

### "Failed to start" error?
Make sure systemd-inhibit is available:
```bash
which systemd-inhibit
```

### Need help?
Run the test script to diagnose issues:
```bash
python3 test_setup.py
```

## Common Use Cases

### Downloading Large Files
1. Timed mode
2. Estimate download time
3. Add 10-15 minutes buffer
4. Start inhibit

### Watching Movies/Presentations
1. Indefinite mode
2. Start inhibit
3. Stop when done

### Running Long Scripts/Builds
1. Indefinite mode
2. Start inhibit before running script
3. Stop when complete

### Preventing Sleep During Specific Hours
1. Calculate duration (e.g., 3 hours)
2. Create a custom preset if you use it often
3. Start inhibit

That's it! You're ready to prevent unwanted sleep on your system.
