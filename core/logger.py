import json
from datetime import datetime

LOG_FILE = "data/logs.json"

def log_failure(node_id):
    entry = {
        "node": node_id,
        "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "event": "Node Failure"
    }

    try:
        with open(LOG_FILE, "r") as f:
            data = json.load(f)
    except:
        data = []

    data.append(entry)

    with open(LOG_FILE, "w") as f:
        json.dump(data, f, indent=4)
