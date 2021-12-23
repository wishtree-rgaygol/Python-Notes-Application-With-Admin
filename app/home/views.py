from flask import abort, render_template,flash,request,jsonify
from flask_login import current_user, login_required

from app.models import Note
from app.__init__ import db
from . import home
import json

@home.route('/')
def homepage():
    """
    Render the homepage template on the / route
    """
    return render_template('home/index.html', title="Welcome")


@home.route('/dashboard',methods=['GET', 'POST'])
@login_required
def dashboard():
    """
    Render the dashboard template on the /dashboard route
    """
    if request.method == 'POST':
        note = request.form.get('note')

        if len(note) < 1:
            flash('Note is too short!', category='error')
        else:
            new_note = Note(data=note, employee_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('Note added!', category='success')
    return render_template('home/dashboard.html', title="Dashboard",employee=current_user)

@home.route('/delete-note', methods=['POST'])
def delete_note():
    print('Enter in delete')
    note = json.loads(request.data)
    noteId = note['noteId']
    note = Note.query.get(noteId)
    print("NOTE --------------==========")
    if note:
        if note.employee_id == current_user.id:
            db.session.delete(note)
            db.session.commit()

    return jsonify({})

@home.route('/admin/dashboard')
@login_required
def admin_dashboard():
    # prevent non-admins from accessing the page
    if not current_user.is_admin:
        abort(403)

    return render_template('home/admin_dashboard.html', title="Dashboard")
