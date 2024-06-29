import subprocess
import os
import sys

# sync with upstream
subprocess.run(["git", "fetch", "upstream"])
subprocess.run(["git", "merge", "upstream/main"])

# Create a virtual environment
subprocess.run([sys.executable, "-m", "venv", "venv"])

# Activate the virtual environment
if os.name == "posix":
    subprocess.run(["source", "venv/bin/activate"])
else:
    subprocess.run(["venv\\Scripts\\activate.bat"])

# Install requirements
subprocess.run([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])

