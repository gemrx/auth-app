from flask import Flask, request, jsonify
from flask_cors import CORS
import mysql.connector

app = Flask(__name__)
CORS(app)

db_config = {
    "host": "auth-db",
    "user": "root",
    "password": "root",
    "database": "auth_db",
}

def get_db_connection():
    return mysql.connector.connect(**db_config)

@app.route('/register', methods=['POST'])
def register():
    data = request.json
    name = data.get("name")
    username = data.get("username")
    password = data.get("password")

    if not all([name, username, password]):
        return jsonify({"error": "All fields are required"}), 400

    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("INSERT INTO users (name, username, password) VALUES (%s, %s, %s)", 
                       (name, username, password))
        conn.commit()
    except mysql.connector.IntegrityError:
        return jsonify({"error": "Username already exists"}), 409
    finally:
        cursor.close()
        conn.close()

    return jsonify({"message": "User registered successfully"}), 201

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get("username")
    password = data.get("password")

    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT name FROM users WHERE username=%s AND password=%s", (username, password))
    user = cursor.fetchone()
    
    cursor.close()
    conn.close()

    if user:
        return jsonify({"message": user['name']}), 200
    return jsonify({"error": "Invalid credentials"}), 401

@app.route('/users', methods=['GET'])
def get_users():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    
    cursor.execute("SELECT id, name, username, password FROM users")
    users = cursor.fetchall()
    
    cursor.close()
    conn.close()

    return jsonify(users), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
