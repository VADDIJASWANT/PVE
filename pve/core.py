# pve/core.py
import os
import sys
import venv
import subprocess

class VirtualEnvManager:
    def __init__(self, env_name="venv"):
        self.env_name = env_name
        self.env_path = os.path.join(os.getcwd(), env_name)

    def create(self):
        """Create a virtual environment."""
        builder = venv.EnvBuilder(with_pip=True)
        builder.create(self.env_path)
        print(f"Virtual environment '{self.env_name}' created at {self.env_path}")

    def start(self):
        """Activate the virtual environment."""
        if not os.path.exists(self.env_path):
            print(f"Error: Virtual environment '{self.env_name}' does not exist.")
            return

        # Detect the platform
        if sys.platform == "win32":
            activate_script = os.path.join(self.env_path, "Scripts", "activate.bat")
            cmd = f"cmd.exe /K {activate_script}"
        else:  # macOS/Linux
            activate_script = os.path.join(self.env_path, "bin", "activate")
            cmd = f"source {activate_script}"

        try:
            # For Windows, this will open a new shell; for Unix, it needs to be run in the current shell
            subprocess.run(cmd, shell=True)
            print(f"Activated virtual environment '{self.env_name}'")
        except Exception as e:
            print(f"Error activating virtual environment: {e}")

    def exists(self):
        """Check if the virtual environment exists."""
        return os.path.exists(self.env_path)