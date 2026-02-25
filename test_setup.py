#!/usr/bin/env python3
"""
Simple test script to verify the setup and dependencies.
Run this to check if everything is properly installed.
"""

import sys
import subprocess

def check_python_version():
    """Check Python version."""
    print("Checking Python version...")
    version = sys.version_info
    if version.major >= 3 and version.minor >= 6:
        print(f"✓ Python {version.major}.{version.minor}.{version.micro} - OK")
        return True
    else:
        print(f"✗ Python {version.major}.{version.minor}.{version.micro} - Too old (need 3.6+)")
        return False

def check_pyqt5():
    """Check if PyQt5 is installed."""
    print("\nChecking PyQt5...")
    try:
        import PyQt5
        from PyQt5.QtWidgets import QApplication
        print(f"✓ PyQt5 {PyQt5.QtCore.PYQT_VERSION_STR} - OK")
        return True
    except ImportError as e:
        print(f"✗ PyQt5 not found: {e}")
        print("  Install with: pip install PyQt5")
        return False

def check_systemd_inhibit():
    """Check if systemd-inhibit is available."""
    print("\nChecking systemd-inhibit...")
    try:
        result = subprocess.run(
            ["which", "systemd-inhibit"],
            capture_output=True,
            text=True
        )
        if result.returncode == 0:
            print(f"✓ systemd-inhibit found at: {result.stdout.strip()}")
            return True
        else:
            print("✗ systemd-inhibit not found")
            print("  This is required for the application to work.")
            return False
    except Exception as e:
        print(f"✗ Error checking systemd-inhibit: {e}")
        return False

def check_config_manager():
    """Check if config manager works."""
    print("\nChecking config manager...")
    try:
        from config_manager import ConfigManager
        config = ConfigManager()
        presets = config.get_presets()
        print(f"✓ Config manager working - {len(presets)} presets loaded")
        return True
    except Exception as e:
        print(f"✗ Config manager error: {e}")
        return False

def check_inhibit_manager():
    """Check if inhibit manager can be imported."""
    print("\nChecking inhibit manager...")
    try:
        from inhibit_manager import InhibitManager
        print("✓ Inhibit manager OK")
        return True
    except Exception as e:
        print(f"✗ Inhibit manager error: {e}")
        return False

def main():
    print("=" * 50)
    print("Sleep Inhibitor - Setup Test")
    print("=" * 50)

    checks = [
        check_python_version(),
        check_pyqt5(),
        check_systemd_inhibit(),
        check_config_manager(),
        check_inhibit_manager(),
    ]

    print("\n" + "=" * 50)
    if all(checks):
        print("✓ All checks passed! You're ready to run the application.")
        print("\nRun the application with: python3 main.py")
    else:
        print("✗ Some checks failed. Please fix the issues above.")
        sys.exit(1)
    print("=" * 50)

if __name__ == "__main__":
    main()
