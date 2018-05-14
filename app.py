from flask import Flask
from flask_mysqldb import MySQL

PORT=PORT_HERE

app = Flask(__name__)

app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_USER'] = 'USERNAME_HERE'
app.config['MYSQL_PASSWORD'] = 'PASSWORD_HERE'
app.config['MYSQL_DB'] = 'DATABASE_NAME_HERE'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

mysql = MySQL(app)

from views import *
from routes import *

from utils import generate

if __name__ == '__main__':
    app.secret_key = generate(35)

    app.debug = True
    app.run('127.0.0.1', PORT)
    
