from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def hello():
    return "<h1>Hello, World!</h1><p>This is a simple Python Flask app running in Docker.</p>"


@app.route("/health")
def health():
    return jsonify({"status": "ok"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
