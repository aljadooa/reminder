from app import app
from flask import render_template, jsonify, flash
from utils import get_all_reminders, get_one_reminder

@app.route('/')
def index():
    page_title = "Reminder - Home"
    return render_template('index.html', page_title=page_title)


@app.route('/test')
def test():
    page_title = 'test'
    return render_template('test.html', page_title=page_title)


@app.route('/r')
def reminders():
    reminders = get_all_reminders()
    page_title = "Reminders ({}) - All Reminders".format(len(reminders))

    return render_template('reminders.html', reminders=reminders, page_title=page_title)

@app.route('/r/<int:id>')
def reminder(id):
    reminder = get_one_reminder(id)
    page_title = "Reminder - {0}".format(reminder['title'])

    return render_template('reminder.html', reminder=reminder, page_title=page_title)


@app.route('/dashboard')
def dashboard():
    page_title = "Reminder - Dashboard"
    reminders = get_all_reminders()

    return render_template('dashboard.html', page_title=page_title, reminders=reminders)
