import os
import signal
import subprocess

# Find the PID of a python process whose command line contains "signaltraps"
result = subprocess.run(
    ['powershell', '-Command',
     "Get-Process python | Where-Object {$_.CommandLine -like '*signaltraps*'} | Select-Object -First 1 -ExpandProperty Id"],
    capture_output=True, text=True
)

pid_str = result.stdout.strip()
if not pid_str:
    print("signaltraps process not found.")
    raise SystemExit(1)

pid = int(pid_str)

print("Choose an option:")
print("1) Send SIGBREAK (Ctrl+Break)")
print("2) Send SIGTERM (Terminate)")
choice = input("Enter 1 or 2: ").strip()

if choice == "1":
    print(f"Sending SIGBREAK to process {pid}...")
    os.kill(pid, signal.SIGBREAK)
    print("SIGBREAK sent!")
elif choice == "2":
    print(f"Sending SIGTERM to process {pid}...")
    os.kill(pid, signal.SIGTERM)
    print("SIGTERM sent!")
else:
    print("Invalid choice. No signal sent.")