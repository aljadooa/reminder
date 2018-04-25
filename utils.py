import random

from app import mysql

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


def generate(start=0, end=0):
    
    result = random.randint(start, end)

    return result


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
