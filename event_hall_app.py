"""
Simple Event Hall Management System using Flask, SQLAlchemy, and Flask‑Login.

This script defines a minimal web application that allows users to register,
log in, log out and manage their own hall booking appointments. Each user
can create, edit and delete appointments. A dashboard shows upcoming
appointments for the logged‑in user. The code is intentionally compact to
serve as a starting point for building a more comprehensive system. To run
this application in your own environment, install Flask and its extensions
with `pip install flask flask_sqlalchemy flask_login` and execute this file.

Note: This code cannot be executed in the current environment because
external package installation is blocked. It is provided for instructional
purposes and should be run locally.

"""

from datetime import datetime
from flask import Flask, render_template_string, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, logout_user, current_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash


app = Flask(__name__)
app.config['SECRET_KEY'] = 'change_me_to_a_secret_value'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///event_hall.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'


class User(UserMixin, db.Model):
    """User model stores account credentials."""
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    appointments = db.relationship('Appointment', backref='owner', lazy=True)

    def set_password(self, password: str) -> None:
        self.password_hash = generate_password_hash(password)

    def check_password(self, password: str) -> bool:
        return check_password_hash(self.password_hash, password)


class Appointment(db.Model):
    """Appointment model stores hall bookings for a user."""
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128), nullable=False)
    hall_name = db.Column(db.String(128), nullable=False)
    start_time = db.Column(db.DateTime, nullable=False)
    end_time = db.Column(db.DateTime, nullable=False)
    description = db.Column(db.Text, nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)


@login_manager.user_loader
def load_user(user_id: str):
    return User.query.get(int(user_id))


@app.before_first_request
def create_tables():
    """Create database tables if they do not exist."""
    db.create_all()


# HTML templates embedded as multi‑line strings for simplicity. In a real
# project, move these to separate files under a templates/ directory.

REGISTER_PAGE = """
<!doctype html>
<title>Register</title>
<h2>Register</h2>
<form method="post">
    <p><label>Username</label><br><input type="text" name="username" required></p>
    <p><label>Email</label><br><input type="email" name="email" required></p>
    <p><label>Password</label><br><input type="password" name="password" required></p>
    <p><button type="submit">Register</button></p>
    <p>Already have an account? <a href="{{ url_for('login') }}">Log in</a></p>
    <p>{{ message }}</p>
</form>
"""

LOGIN_PAGE = """
<!doctype html>
<title>Login</title>
<h2>Login</h2>
<form method="post">
    <p><label>Username</label><br><input type="text" name="username" required></p>
    <p><label>Password</label><br><input type="password" name="password" required></p>
    <p><button type="submit">Login</button></p>
    <p>Need an account? <a href="{{ url_for('register') }}">Register</a></p>
    <p>{{ message }}</p>
</form>
"""

DASHBOARD_PAGE = """
<!doctype html>
<title>Dashboard</title>
<h2>Welcome, {{ current_user.username }}</h2>
<p><a href="{{ url_for('new_appointment') }}">Create new appointment</a> | <a href="{{ url_for('logout') }}">Logout</a></p>
<h3>Your Appointments</h3>
{% if appointments %}
    <ul>
    {% for appt in appointments %}
        <li>
            <strong>{{ appt.title }}</strong> in {{ appt.hall_name }} from {{ appt.start_time.strftime('%Y-%m-%d %H:%M') }} to {{ appt.end_time.strftime('%Y-%m-%d %H:%M') }}<br>
            {{ appt.description or '' }}<br>
            <a href="{{ url_for('edit_appointment', appointment_id=appt.id) }}">Edit</a> |
            <a href="{{ url_for('delete_appointment', appointment_id=appt.id) }}">Delete</a>
        </li>
    {% endfor %}
    </ul>
{% else %}
    <p>No appointments scheduled.</p>
{% endif %}
"""

APPOINTMENT_FORM_PAGE = """
<!doctype html>
<title>{% if appointment %}Edit{% else %}New{% endif %} Appointment</title>
<h2>{% if appointment %}Edit{% else %}New{% endif %} Appointment</h2>
<form method="post">
    <p><label>Title</label><br><input type="text" name="title" value="{{ appointment.title if appointment else '' }}" required></p>
    <p><label>Hall Name</label><br><input type="text" name="hall_name" value="{{ appointment.hall_name if appointment else '' }}" required></p>
    <p><label>Start Time (YYYY‑MM‑DD HH:MM)</label><br><input type="text" name="start_time" value="{{ appointment.start_time.strftime('%Y-%m-%d %H:%M') if appointment else '' }}" required></p>
    <p><label>End Time (YYYY‑MM‑DD HH:MM)</label><br><input type="text" name="end_time" value="{{ appointment.end_time.strftime('%Y-%m-%d %H:%M') if appointment else '' }}" required></p>
    <p><label>Description</label><br><textarea name="description">{{ appointment.description if appointment else '' }}</textarea></p>
    <p><button type="submit">Save</button></p>
    <p><a href="{{ url_for('dashboard') }}">Back to Dashboard</a></p>
    <p>{{ message }}</p>
</form>
"""


@app.route('/register', methods=['GET', 'POST'])
def register():
    """Allow a new user to create an account."""
    message = ''
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        # Basic validation
        if User.query.filter_by(username=username).first():
            message = 'Username already taken.'
        elif User.query.filter_by(email=email).first():
            message = 'Email already registered.'
        else:
            user = User(username=username, email=email)
            user.set_password(password)
            db.session.add(user)
            db.session.commit()
            message = 'Registration successful. Please log in.'
            return redirect(url_for('login'))
    return render_template_string(REGISTER_PAGE, message=message)


@app.route('/login', methods=['GET', 'POST'])
def login():
    """Authenticate a user and start a session."""
    message = ''
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and user.check_password(password):
            login_user(user)
            return redirect(url_for('dashboard'))
        message = 'Invalid credentials.'
    return render_template_string(LOGIN_PAGE, message=message)


@app.route('/logout')
@login_required
def logout():
    """Log out the current user."""
    logout_user()
    return redirect(url_for('login'))


@app.route('/')
@login_required
def dashboard():
    """Display the dashboard with the user's appointments."""
    appointments = Appointment.query.filter_by(owner=current_user).order_by(Appointment.start_time).all()
    return render_template_string(DASHBOARD_PAGE, appointments=appointments)


@app.route('/appointment/new', methods=['GET', 'POST'])
@login_required
def new_appointment():
    """Create a new appointment."""
    message = ''
    if request.method == 'POST':
        try:
            title = request.form['title']
            hall_name = request.form['hall_name']
            start_time = datetime.strptime(request.form['start_time'], '%Y-%m-%d %H:%M')
            end_time = datetime.strptime(request.form['end_time'], '%Y-%m-%d %H:%M')
            description = request.form.get('description')
            # Ensure start_time is before end_time
            if start_time >= end_time:
                message = 'Start time must be earlier than end time.'
            else:
                appt = Appointment(title=title, hall_name=hall_name,
                                   start_time=start_time, end_time=end_time,
                                   description=description, owner=current_user)
                db.session.add(appt)
                db.session.commit()
                return redirect(url_for('dashboard'))
        except ValueError:
            message = 'Invalid date/time format.'
    return render_template_string(APPOINTMENT_FORM_PAGE, appointment=None, message=message)


@app.route('/appointment/<int:appointment_id>/edit', methods=['GET', 'POST'])
@login_required
def edit_appointment(appointment_id: int):
    """Edit an existing appointment belonging to the current user."""
    appt = Appointment.query.get_or_404(appointment_id)
    if appt.owner != current_user:
        return redirect(url_for('dashboard'))
    message = ''
    if request.method == 'POST':
        try:
            appt.title = request.form['title']
            appt.hall_name = request.form['hall_name']
            start_time = datetime.strptime(request.form['start_time'], '%Y-%m-%d %H:%M')
            end_time = datetime.strptime(request.form['end_time'], '%Y-%m-%d %H:%M')
            if start_time >= end_time:
                message = 'Start time must be earlier than end time.'
            else:
                appt.start_time = start_time
                appt.end_time = end_time
                appt.description = request.form.get('description')
                db.session.commit()
                return redirect(url_for('dashboard'))
        except ValueError:
            message = 'Invalid date/time format.'
    return render_template_string(APPOINTMENT_FORM_PAGE, appointment=appt, message=message)


@app.route('/appointment/<int:appointment_id>/delete')
@login_required
def delete_appointment(appointment_id: int):
    """Delete an appointment belonging to the current user."""
    appt = Appointment.query.get_or_404(appointment_id)
    if appt.owner == current_user:
        db.session.delete(appt)
        db.session.commit()
    return redirect(url_for('dashboard'))


if __name__ == '__main__':
    # The application is intended for demonstration and should be run locally.
    app.run(debug=True)