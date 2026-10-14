from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello from my DevOps project!"

@app.route("/health")
def health():
    return jsonify(status="ok")
