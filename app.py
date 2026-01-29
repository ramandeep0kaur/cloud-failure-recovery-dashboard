from flask import Flask, render_template, jsonify
from core.monitor import get_node_status
from core.recovery import recover_node
from core.predictor import predict
from core.logger import log_failure

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

@app.route("/api/status")
def status():
    nodes = get_node_status()

    for n in nodes:
        if n["status"] == "DOWN":
            log_failure(n["id"])
            n["prediction"] = predict(n["cpu"], n["memory"])
        else:
            n["prediction"] = predict(n["cpu"], n["memory"])

    return jsonify(nodes)

@app.route("/api/recover/<node_id>")
def recover(node_id):
    return jsonify(recover_node(node_id))

if __name__ == "__main__":
    app.run(debug=True)
