from app import app
from flask import jsonify, send_from_directory, request, url_for, redirect
from utils import execute_sql

@app.route('/public/<path:path>')
def serve_static_assets(path):
    return send_from_directory('public', path)


@app.route('/r/add', methods=['POST'])
def add_reminder():
    # query
    query = ("INSERT INTO reminders " 
    "(title, reminder, date, completed) " 
    "VALUES (%(title)s, %(reminder)s, %(date)s, %(completed)s)")
    
    # data given to database
    data = {
        'title': request.form['title'],
        'reminder': request.form['add-reminder'],
        'date': request.form['date'],
        'completed': 'No'
    }

    execute_sql(query, data, True, "None")

    return redirect(url_for('dashboard'))

@app.route('/r/update', methods=['POST'])
def update():

    query = ("UPDATE reminders SET title = %(title)s, reminder = %(reminder)s, date = %(date)s  WHERE id = %(id)s")
    
    # data given to database
    data = {
        'id': request.args.get('id'),
        'title': request.form['title'],
        'reminder': request.form['edit-reminder'],
        'date': request.form['date']
    }

    execute_sql(query, data, True, None)

    return redirect(url_for('dashboard'))

@app.route('/r/delete', methods=['POST'])
def delete():

    query = ("UPDATE reminders SET deleted = %(deleted)s  WHERE id = %(id)s")
    
    # data given to database
    data = {
        'id': request.args.get('id'),
        'deleted': 1
    }

    execute_sql(query, data, True, None)

    return jsonify({"message": "Reminder Deleted Successfully"})
