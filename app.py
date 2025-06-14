# api.py
from flask import Flask, jsonify
import time
import random
import sqlite3
import math

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

# Adicione esses novos 
@app.route('/heavy-db')
def heavy_db_operation():
    start = time.time()
    conn = get_db_connection()

    # Operação mais pesada com múltiplas tabelas
    for _ in range(random.randint(10, 50)):
        conn.execute('''SELECT * FROM users u1 
                       JOIN users u2 ON u1.id = u2.id 
                       JOIN users u3 ON u1.id != u3.id 
                       LIMIT 100''').fetchall()
    conn.close()
    duration = time.time() - start
    app.logger.info(f"heavy-db took {duration:.2f} seconds")
    return jsonify({"status": "heavy operation completed"})


@app.route('/memory-intensive')
def memory_intensive():
    # Consumo crescente de memória
    big_data = []
    for _ in range(random.randint(1000, 5000)):
        big_data.append([random.random() for _ in range(1000)])
    
    return jsonify({"status": "memory allocated", "size": len(big_data)})

@app.route('/cpu-intensive')
def cpu_intensive():
    # Cálculo pesado de CPU
    start = time.time()
    for _ in range(1000000):
        math.factorial(random.randint(1, 100))
    
    return jsonify({"status": "cpu task done", "time": time.time() - start})

@app.route('/break-me')
def break_me():
    # Consumo extremo de memória
    data = [str(i)*100000 for i in range(10000)]
    return jsonify({"status": "memory allocated"})


if __name__ == '__main__':
    app.run(port=5000)
