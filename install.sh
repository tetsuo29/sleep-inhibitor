#!/bin/bash

# Installation script for Sleep Inhibitor

echo "Installing Sleep Inhibitor..."
echo ""

# Get the absolute path to the script directory
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# Check if PyQt5 is available
echo "Checking for PyQt5..."
if python3 -c "import PyQt5" 2>/dev/null; then
    echo "✓ PyQt5 is already installed"
else
    echo "✗ PyQt5 is not installed"
    echo ""
    echo "Please install PyQt5 using your system package manager:"
    echo ""
    echo "  Debian/Ubuntu/KDE Neon:"
    echo "    sudo apt install python3-pyqt5"
    echo ""
    echo "  Fedora:"
    echo "    sudo dnf install python3-qt5"
    echo ""
    echo "  Arch Linux:"
    echo "    sudo pacman -S python-pyqt5"
    echo ""
    echo "Or create a virtual environment and use pip:"
    echo "    python3 -m venv venv"
    echo "    source venv/bin/activate"
    echo "    pip install -r requirements.txt"
    echo ""
    read -p "Do you want to try installing with pip --user? (y/N) " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        pip install --user -r "$SCRIPT_DIR/requirements.txt" 2>/dev/null
        if [ $? -ne 0 ]; then
            echo "Note: pip install failed. Please use your system package manager instead."
        fi
    else
        echo "Skipping pip installation. Please install PyQt5 manually and run this script again."
        exit 1
    fi
fi
echo ""

# Create desktop entry
echo "Creating desktop entry..."
DESKTOP_FILE="$HOME/.local/share/applications/sleep-inhibitor.desktop"
mkdir -p "$HOME/.local/share/applications"

cat > "$DESKTOP_FILE" << EOF
[Desktop Entry]
Type=Application
Version=1.0
Name=Sleep Inhibitor
Comment=Prevent system sleep using systemd-inhibit
Exec=/usr/bin/python3 $SCRIPT_DIR/main.py
Icon=preferences-desktop-notification
Terminal=false
Categories=System;Utility;Qt;KDE;
Keywords=sleep;inhibit;systemd;power;
StartupNotify=true
EOF

chmod +x "$DESKTOP_FILE"

# Make main.py executable
chmod +x "$SCRIPT_DIR/main.py"

echo ""
echo "Installation complete!"
echo ""
echo "You can now:"
echo "1. Launch from KDE application menu (search for 'Sleep Inhibitor')"
echo "2. Run directly: python3 $SCRIPT_DIR/main.py"
echo ""
echo "Note: This application requires systemd-inhibit to be available on your system."
