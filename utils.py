import random, string

from datetime import datetime

from app import mysql
from htmlmin.minify import html_minify

def get_all_reminders():
    
    reminders = []

    query = "SELECT * from reminders"

    result = execute_sql(query, None, False, 'get')

    for row in result:
        reminder = {
            'id': row['id'],
            'title': row['title'],
            'reminder': row['reminder'],
            'date': row['date'],
            'completed': row['completed'],
            'deleted': row['deleted'],
            'timestamp': row['timestamp']
        }
        # filter out reminders marked as deleted
        if row['deleted'] == 1:
            pass
        else:
            #datetime.strftime(reminder['date'], "%B/%d/%Y")
            reminders.append(reminder)
    
    return reminders

def get_one_reminder(id):

    cursor = mysql.connection.cursor()
    
    query = "SELECT id, title, reminder, date, completed, deleted, timestamp from reminders WHERE id = %(id)s"

    _data = {
        'id': id
    }

    result = cursor.execute(query, _data)

    data = cursor.fetchone()

    if data['deleted'] == 1:
        deleted = {
            'id': 'Deleted',
            'title': 'Deleted',
            'reminder': 'Deleted',
            'date': 'Deleted',
            'completed': 'Deleted',
            'deleted': data['deleted'],
            'timestamp': 'Deleted'
        }
        return deleted
    else:
        reminder = {
            'id': data['id'],
            'title': data['title'],
            'reminder': data['reminder'],
            'date': data['date'],
            'completed': data['completed'],
            'deleted': data['deleted'],
            'timestamp': data['timestamp']
        }

        return reminder

def generate(length):

    CHARS=string.ascii_letters + string.digits + '#$%&()*+,-./:;<=>?@[]^_`{|}~'

    result=''

    for i in range(length):
        index = random.choice(CHARS)

        result += index

    return result

# dynamic html compressor
def compress(template):
    return html_minify(template)

def execute_sql(query, data, commit=False, mode=""):

    cursor = mysql.connection.cursor()

    if mode == "get":
        cursor.execute(query)
    else:
        cursor.execute(query, data)

    if commit == True:
        mysql.connection.commit()

    if mode == "get":
        return cursor

