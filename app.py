from flask import Flask
from flask_mysqldb import MySQL

PORT=PORT_HERE

app = Flask(__name__)

app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_USER'] = ''
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = ''
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

mysql = MySQL(app)

from views import *
from routes import *


if __name__ == '__main__':
    app.secret_key = '  '

    app.debug = True
    app.run('YOUR_LOCAL_IP_HERE', PORT)
    
