from flask import Flask
from flask_mysqldb import MySQL

PORT=80

app = Flask(__name__)

app.config['MYSQL_HOST'] = ''
app.config['MYSQL_USER'] = ''
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = ''
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

mysql = MySQL(app)

from views import *
from routes import *

from utils import generate


if __name__ == '__main__':
    app.secret_key = generate(35)

    app.debug = True
    app.run('10.0.0.252', PORT)
    