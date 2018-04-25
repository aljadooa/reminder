import random

from app import app
from flask import jsonify, send_from_directory, request, url_for, redirect, flash
from utils import execute_sql, generate

# serve site assets
@app.route('/public/<path:path>')
def serve_static_assets(path):
    return send_from_directory('public', path)


@app.route('/r/add', methods=['POST'])
def add_reminder():

    query = ("INSERT INTO reminders " 
    "(id, title, reminder, date, completed) " 
    "VALUES (%(id)s, %(title)s, %(reminder)s, %(date)s, %(completed)s)")
    
    data = {
        'id': generate(1000, 9999),
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
    
    data = {
        'id': request.args.get('id'),
        'deleted': 1
    }

    execute_sql(query, data, True, None)

    return jsonify({"result": "Reminder Deleted Successfully"})



@app.route('/r/complete', methods=['POST'])
def complete():

    query = ("UPDATE reminders SET completed = %(completed)s  WHERE id = %(id)s")
    
    data = {
        'id': request.args.get('id'),
        'completed': 'Yes'
    }

    execute_sql(query, data, True, None)

    return jsonify({"result": "Reminder marked as completed."})


@app.route('/r/uncomplete', methods=['POST'])
def uncomplete():

    query = ("UPDATE reminders SET completed = %(completed)s  WHERE id = %(id)s")
    
    data = {
        'id': request.args.get('id'),
        'completed': 'No'
    }

    execute_sql(query, data, True, None)

    return jsonify({"result": "Reminder marked as completed."})