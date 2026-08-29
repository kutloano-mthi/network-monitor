import subprocess
devices = [
    "8.8.8.8",
    "1.1.1.1",
    "google.com",
    "192.168.1.1"
]
for ip in devices:
    result = subprocess.run(
        ["ping", "-n", "1", ip],
        capture_output=True,
        text=True
    )
    if "TTL=" in result.stdout:
        print(f"{ip} is ONLINE")
    else:
        print(f"{ip} is OFFLINE")