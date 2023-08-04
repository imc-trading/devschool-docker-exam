from flask import Flask
import os
import mysql.connector

app = Flask(__name__)
db = mysql.connector.connect(
    host=os.getenv("MYSQL_HOST", "somehost"),
    port=os.getenv("MYSQL_PORT", 1234),
    user=os.getenv("MYSQL_USER", "someuser"),
    password=os.getenv("MYSQL_PASSWORD", "somepassword"),
    database=os.getenv("MYSQL_DATABASE", "somedatabase")
)
cursor = db.cursor()


@app.route('/')
def get_users():
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    return f'The users in your system: {users}'


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=4000)
