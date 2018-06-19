from app import app
from flask import render_template, jsonify, flash
from utils import get_all_reminders, get_one_reminder, compress

@app.route('/')
def index():
    page_title = "Reminder - Home"
    
    template = render_template('index.html', page_title=page_title)

    return compress(template)

@app.route('/r')
def reminders():
    count=0
    reminders = get_all_reminders()

    # reminder counter
    for reminder in reminders:
        if reminder['deleted'] == 0:
            count += 1

    page_title = "Reminders ({}) - All Reminders".format(count)
 
    template = render_template('reminders.html', reminders=reminders, page_title=page_title)

    return compress(template)

@app.route('/r/<int:id>')
def reminder(id):
    page_title=''
    reminder = get_one_reminder(id)

    if reminder['deleted'] == 1:
        page_title = "Deleted"
    else:
        page_title = "Reminder - {0}".format(reminder['title'])

    template = render_template('reminder.html', reminder=reminder, page_title=page_title)

    return compress(template)

@app.route('/dashboard')
def dashboard():
    page_title = "Reminder - Dashboard"
    name = "Hassan"
    reminders = get_all_reminders()

    template = render_template('dashboard.html', page_title=page_title, name=name, reminders=reminders)

    return compress(template)