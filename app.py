from flask import Flask,render_template, request
from flask_mysqldb import MySQL
 
app = Flask(__name__)
 
app.config['MYSQL_HOST'] = 'sql12.freemysqlhosting.net'
app.config['MYSQL_USER'] = 'sql12613064'
app.config['MYSQL_PASSWORD'] = 'gqg7zYPphz'
app.config['MYSQL_DB'] = 'sql12613064'
 
mysql = MySQL(app)
 
@app.route('/')
def form():
    return 'Hello, Brother!'

@app.route('/text', methods = ['POST', 'GET'])
def login():
    if request.method == 'GET':
        cursor = mysql.connection.cursor()
        cursor.execute(''' SELECT * FROM Content ''')
        rows = cursor.fetchall()
        if len(rows) > 0:
            cursor.close()
            return {
                'content': rows[0][0],
                'success': True
            }
        else:
            cursor.close()
            return {
                'content': '',
                'success': True
            }
     
    if request.method == 'POST':
        content = request.form['content']
        cursor = mysql.connection.cursor()
        result = cursor.execute(''' SELECT * FROM Content ''')
        if result > 0:
            cursor.execute(f''' UPDATE Content SET text = '{content}' ''')
        else:
            cursor.execute(f''' INSERT INTO Content VALUES('{content}')''')

        mysql.connection.commit()
        cursor.close()
        return f"Done!!"
 
app.run(host='localhost', port=5000)
