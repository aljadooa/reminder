from flask import Flask
from flask_mysqldb import MySQL

PORT=80

app = Flask(__name__)

app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_USER'] = ''
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'reminder'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

mysql = MySQL(app)

from views import *
from routes import *


if __name__ == '__main__':
    app.debug = True
    app.run('10.0.0.252', PORT)
