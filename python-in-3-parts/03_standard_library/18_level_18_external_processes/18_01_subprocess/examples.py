import subprocess, sys
result = subprocess.run([sys.executable, "--version"], capture_output=True, text=True)
print(result.stdout or result.stderr)
result = subprocess.run([sys.executable, "-c", "print(2 + 3)"], capture_output=True, text=True)
print(result.returncode)
print(result.stdout)
