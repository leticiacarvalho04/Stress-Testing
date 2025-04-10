# api.py
from flask import Flask, jsonify
import time
import random

app = Flask(__name__)

@app.route('/fast')
def fast_endpoint():
    return jsonify({"status": "success", "message": "This is a fast endpoint"})

@app.route('/slow')
def slow_endpoint():
    # Simula processamento demorado
    delay = random.uniform(0.1, 2.0)
    time.sleep(delay)
    return jsonify({"status": "success", "message": f"This endpoint was delayed by {delay:.2f} seconds"})

@app.route('/error-prone')
def error_prone_endpoint():
    # Simula erros aleatórios
    if random.random() < 0.3:  # 30% de chance de erro
        return jsonify({"status": "error", "message": "Internal server error"}), 500
    return jsonify({"status": "success", "message": "This endpoint might fail sometimes"})

if __name__ == '__main__':
    app.run(port=5000)