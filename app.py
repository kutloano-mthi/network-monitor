from flask import Flask, render_template
import subprocess

app = Flask(__name__)

devices = [
    "Device ID
Hostname
IP Address
Device Type
Location
Status
Last Seen
Latency"
]

@app.route("/")
def home():

    results = []

    for ip in devices:

        result = subprocess.run(
            ["ping", "-n", "1", ip],
            capture_output=True,
            text=True
        )

        status = "ONLINE" if "TTL=" in result.stdout else "OFFLINE"

        results.append({
            "ip": ip,
            "status": status
        })

    return render_template(
        "index.html",
        results=results
    )

if __name__ == "__main__":
    app.run(debug=True)