# api.py
from flask import Flask, jsonify
import time
import random
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/fast')
def fast_endpoint():
    return jsonify({"status": "success", "message": "This is a fast endpoint"})

import psutil, os

@app.route('/status')
def status():
    process = psutil.Process(os.getpid())
    mem = process.memory_info().rss / (1024 * 1024)  # Em MB
    cpu = process.cpu_percent()
    return jsonify({
        "memory_MB": mem,
        "cpu_percent": cpu
    })

@app.route('/slow')
def slow_endpoint():
    delay = random.uniform(0.1, 2.0)
    time.sleep(delay)

    conn = get_db_connection()
    data = conn.execute('SELECT COUNT(*) as count FROM users').fetchone()
    conn.close()

    return jsonify({
        "status": "success",
        "message": f"This endpoint was delayed by {delay:.2f} seconds",
        "users_in_db": data['count']
    })

@app.route('/error-prone')
def error_prone_endpoint():
    if random.random() < 0.3:
        return jsonify({"status": "error", "message": "Internal server error"}), 500

    conn = get_db_connection()
    data = conn.execute('SELECT * FROM users ORDER BY RANDOM() LIMIT 1').fetchone()
    conn.close()

    return jsonify({
        "status": "success",
        "user": dict(data) if data else "No users"
    })

if __name__ == '__main__':
    app.run(port=5000)
