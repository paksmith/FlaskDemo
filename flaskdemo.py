from flask import Flask, render_template
import pymysql

app = Flask(__name__)
wsgi_app = app.wsgi_app

def create_connection():
    return pymysql.connect(  
        host = 'localhost',
        user = 'root',
        password = '13com',
        db = 'laptops',
        charset = 'utf8mb4',
        cursorclass = pymysql.cursors.DictCursor
    )



@app.route('/')
def index():
    connection = create_connection()
    with connection.cursor() as cursor:
        sql = "SELECT * FROM tblstudents;"
        cursor.execute(sql)
        students = cursor.fetchall()
        connection.close()
    return render_template("index.html", students = students)

if __name__ == '__main__':
    import os
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(os.environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT)
