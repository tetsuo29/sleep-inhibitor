import json
import os
from typing import List, Dict

class ConfigManager:
    """Manages application configuration and presets."""

    def __init__(self):
        self.config_dir = os.path.expanduser("~/.config/sleep-inhibitor")
        self.config_file = os.path.join(self.config_dir, "config.json")
        self.presets: List[Dict[str, any]] = []
        self._ensure_config_dir()
        self.load_presets()

    def _ensure_config_dir(self):
        """Create config directory if it doesn't exist."""
        os.makedirs(self.config_dir, exist_ok=True)

    def load_presets(self):
        """Load presets from config file."""
        if os.path.exists(self.config_file):
            try:
                with open(self.config_file, 'r') as f:
                    data = json.load(f)
                    self.presets = data.get('presets', [])
            except (json.JSONDecodeError, IOError):
                self.presets = self._get_default_presets()
        else:
            self.presets = self._get_default_presets()
            self.save_presets()

    def save_presets(self):
        """Save presets to config file."""
        data = {'presets': self.presets}
        try:
            with open(self.config_file, 'w') as f:
                json.dump(data, f, indent=2)
        except IOError as e:
            print(f"Error saving presets: {e}")

    def _get_default_presets(self) -> List[Dict[str, any]]:
        """Return default preset intervals."""
        return [
            {"name": "15 minutes", "minutes": 15},
            {"name": "30 minutes", "minutes": 30},
            {"name": "1 hour", "minutes": 60},
            {"name": "2 hours", "minutes": 120},
            {"name": "4 hours", "minutes": 240},
        ]

    def add_preset(self, name: str, minutes: int):
        """Add a new preset."""
        self.presets.append({"name": name, "minutes": minutes})
        self.save_presets()

    def remove_preset(self, index: int):
        """Remove a preset by index."""
        if 0 <= index < len(self.presets):
            self.presets.pop(index)
            self.save_presets()

    def get_presets(self) -> List[Dict[str, any]]:
        """Get all presets."""
        return self.presets
