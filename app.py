from flask import Flask
from flask_mysqldb import MySQL
from flask_compress import Compress

PORT=8000

app = Flask(__name__)
Compress(app)

# mysql database credentials
app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'reminder'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

mysql = MySQL(app)

from views import *
from routes import *

from utils import generate

if __name__ == '__main__':
    app.secret_key = generate(35)
    
    # set this to false in prod
    app.debug = True
    app.run('locahost', PORT)
    
