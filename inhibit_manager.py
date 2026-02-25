import subprocess
from typing import Optional
from PyQt5.QtCore import QObject, pyqtSignal

class InhibitManager(QObject):
    """Manages systemd-inhibit sleep process."""

    status_changed = pyqtSignal(bool)  # Signal emitted when inhibit status changes

    def __init__(self):
        super().__init__()
        self.process: Optional[subprocess.Popen] = None
        self.is_active = False
        self.is_indefinite = True
        self.duration_seconds = 0

    def start_inhibit(self, indefinite: bool = True, duration_seconds: int = 0):
        """Start sleep inhibition."""
        if self.is_active:
            self.stop_inhibit()

        try:
            # Build systemd-inhibit command
            cmd = ["systemd-inhibit", "--what=sleep", "--who=Sleep Inhibitor",
                   "--why=User requested sleep inhibition"]

            if indefinite:
                # For indefinite inhibit, keep a persistent sleep process
                # cmd.extend(["sleep", "infinity"])
                # cmd =["systemd-inhibit", "sleep", "31536000"]
                cmd =["systemd-inhibit", "sh"]
            else:
                # For timed inhibit, sleep for specific duration
                # cmd.extend(["sleep", str(duration_seconds)])
                cmd = ["systemd-inhibit", "sleep", str(duration_seconds)]

            # Start the process
            self.process = subprocess.Popen(
                cmd,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE
            )

            self.is_active = True
            self.is_indefinite = indefinite
            self.duration_seconds = duration_seconds
            self.status_changed.emit(True)
            return True

        except Exception as e:
            print(f"Error starting inhibit: {e}")
            self.is_active = False
            self.status_changed.emit(False)
            return False

    def stop_inhibit(self):
        """Stop sleep inhibition."""
        if self.process:
            try:
                self.process.terminate()
                self.process.wait(timeout=5)
            except subprocess.TimeoutExpired:
                self.process.kill()
            except Exception as e:
                print(f"Error stopping inhibit: {e}")
            finally:
                self.process = None

        self.is_active = False
        self.is_indefinite = True
        self.duration_seconds = 0
        self.status_changed.emit(False)

    def check_status(self) -> bool:
        """Check if inhibit is still active."""
        if self.process:
            poll = self.process.poll()
            if poll is not None:
                # Process has ended
                self.stop_inhibit()
                return False
            return True
        return False
