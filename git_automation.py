# import os
import subprocess

# Get the current directory 
# curdir = os.getcwd()

# Navigate back to the Git root folder
# os.chdir(os.path.join(curdir, "../../"))

# Run git status
subprocess.run(["git", "status"])

# Run git add . 
subprocess.run(["git", "add", "."])

# Run git commit -m "update"
subprocess.run(["git", "commit", "-m", "update"])

# Run git push
subprocess.run(["git", "push"])
