from flask import Flask
import mysql.connector
import os

app = Flask(__name__)

def get_db_connection():
    return mysql.connector.connect(
        host="mysql-db",
        user="root",
        password=os.environ.get("MYSQL_ROOT_PASSWORD", "secretpass"),
        database="testdb"
    )

@app.route('/')
def index():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT VERSION();")
        version = cursor.fetchone()
        cursor.close()
        conn.close()
        return f"<h1>Success! Connected to MySQL. Version: {version[0]}</h1>"
    except Exception as e:
        return f"<h1>Connection Failed! Error: {str(e)}</h1>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
