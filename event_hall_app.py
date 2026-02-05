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

    @staticmethod
    def check_availability(hall_name, start_time, end_time, exclude_id=None):
        """Check if a hall is available for the given time range."""
        query = Appointment.query.filter(
            Appointment.hall_name == hall_name,
            Appointment.start_time < end_time,
            Appointment.end_time > start_time
        )
        if exclude_id:
            query = query.filter(Appointment.id != exclude_id)
        return query.first() is None


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
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Register - Event Hall Management</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; 
               background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
               min-height: 100vh; display: flex; align-items: center; justify-content: center; }
        .container { background: white; padding: 40px; border-radius: 10px; box-shadow: 0 10px 40px rgba(0,0,0,0.1); 
                     max-width: 400px; width: 90%; }
        h2 { color: #333; margin-bottom: 30px; text-align: center; }
        label { display: block; margin-bottom: 5px; color: #555; font-weight: 500; }
        input { width: 100%; padding: 12px; margin-bottom: 20px; border: 1px solid #ddd; 
                border-radius: 5px; font-size: 14px; }
        input:focus { outline: none; border-color: #667eea; }
        button { width: 100%; padding: 12px; background: #667eea; color: white; border: none; 
                 border-radius: 5px; font-size: 16px; font-weight: 600; cursor: pointer; }
        button:hover { background: #5568d3; }
        .links { text-align: center; margin-top: 20px; color: #666; }
        .links a { color: #667eea; text-decoration: none; }
        .links a:hover { text-decoration: underline; }
        .message { color: #d32f2f; text-align: center; margin-top: 15px; }
    </style>
</head>
<body>
    <div class="container">
        <h2>Create Account</h2>
        <form method="post">
            <label>Username</label>
            <input type="text" name="username" required>
            <label>Email</label>
            <input type="email" name="email" required>
            <label>Password</label>
            <input type="password" name="password" required>
            <button type="submit">Register</button>
            <div class="links">
                Already have an account? <a href="{{ url_for('login') }}">Log in</a>
            </div>
            {% if message %}<p class="message">{{ message }}</p>{% endif %}
        </form>
    </div>
</body>
</html>
"""

LOGIN_PAGE = """
<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login - Event Hall Management</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; 
               background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
               min-height: 100vh; display: flex; align-items: center; justify-content: center; }
        .container { background: white; padding: 40px; border-radius: 10px; box-shadow: 0 10px 40px rgba(0,0,0,0.1); 
                     max-width: 400px; width: 90%; }
        h2 { color: #333; margin-bottom: 30px; text-align: center; }
        label { display: block; margin-bottom: 5px; color: #555; font-weight: 500; }
        input { width: 100%; padding: 12px; margin-bottom: 20px; border: 1px solid #ddd; 
                border-radius: 5px; font-size: 14px; }
        input:focus { outline: none; border-color: #667eea; }
        button { width: 100%; padding: 12px; background: #667eea; color: white; border: none; 
                 border-radius: 5px; font-size: 16px; font-weight: 600; cursor: pointer; }
        button:hover { background: #5568d3; }
        .links { text-align: center; margin-top: 20px; color: #666; }
        .links a { color: #667eea; text-decoration: none; }
        .links a:hover { text-decoration: underline; }
        .message { color: #d32f2f; text-align: center; margin-top: 15px; }
    </style>
</head>
<body>
    <div class="container">
        <h2>Welcome Back</h2>
        <form method="post">
            <label>Username</label>
            <input type="text" name="username" required>
            <label>Password</label>
            <input type="password" name="password" required>
            <button type="submit">Login</button>
            <div class="links">
                Need an account? <a href="{{ url_for('register') }}">Register</a>
            </div>
            {% if message %}<p class="message">{{ message }}</p>{% endif %}
        </form>
    </div>
</body>
</html>
"""

DASHBOARD_PAGE = """
<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Dashboard - Event Hall Management</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; 
               background: #f5f5f5; min-height: 100vh; }
        .header { background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
                  color: white; padding: 20px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); }
        .header-content { max-width: 1200px; margin: 0 auto; display: flex; 
                          justify-content: space-between; align-items: center; }
        .nav-links a { color: white; text-decoration: none; margin-left: 20px; 
                       padding: 8px 16px; border-radius: 5px; }
        .nav-links a:hover { background: rgba(255,255,255,0.2); }
        .container { max-width: 1200px; margin: 30px auto; padding: 0 20px; }
        .page-title { font-size: 28px; margin-bottom: 30px; color: #333; }
        .appointments-grid { display: grid; gap: 20px; }
        .appointment-card { background: white; padding: 20px; border-radius: 8px; 
                           box-shadow: 0 2px 8px rgba(0,0,0,0.1); }
        .appointment-card h3 { color: #667eea; margin-bottom: 10px; }
        .appointment-info { color: #666; margin: 8px 0; }
        .appointment-actions { margin-top: 15px; }
        .appointment-actions a { display: inline-block; padding: 8px 16px; margin-right: 10px; 
                                 border-radius: 5px; text-decoration: none; font-size: 14px; }
        .btn-edit { background: #667eea; color: white; }
        .btn-edit:hover { background: #5568d3; }
        .btn-delete { background: #dc3545; color: white; }
        .btn-delete:hover { background: #c82333; }
        .btn-primary { display: inline-block; padding: 12px 24px; background: #667eea; 
                       color: white; text-decoration: none; border-radius: 5px; 
                       font-weight: 600; margin-bottom: 20px; }
        .btn-primary:hover { background: #5568d3; }
        .empty-state { text-align: center; padding: 60px 20px; color: #999; }
        .empty-state p { margin-top: 10px; }
    </style>
</head>
<body>
    <div class="header">
        <div class="header-content">
            <h1>Event Hall Management</h1>
            <div class="nav-links">
                <span>Welcome, {{ current_user.username }}</span>
                <a href="{{ url_for('logout') }}">Logout</a>
            </div>
        </div>
    </div>
    <div class="container">
        <a href="{{ url_for('new_appointment') }}" class="btn-primary">+ Create New Booking</a>
        <h2 class="page-title">Upcoming Appointments</h2>
        {% if appointments %}
            <div class="appointments-grid">
            {% for appt in appointments %}
                <div class="appointment-card">
                    <h3>{{ appt.title }}</h3>
                    <p class="appointment-info"><strong>Hall:</strong> {{ appt.hall_name }}</p>
                    <p class="appointment-info"><strong>Date:</strong> {{ appt.start_time.strftime('%A, %B %d, %Y') }}</p>
                    <p class="appointment-info"><strong>Time:</strong> {{ appt.start_time.strftime('%H:%M') }} - {{ appt.end_time.strftime('%H:%M') }}</p>
                    {% if appt.description %}
                    <p class="appointment-info"><strong>Details:</strong> {{ appt.description }}</p>
                    {% endif %}
                    <div class="appointment-actions">
                        <a href="{{ url_for('edit_appointment', appointment_id=appt.id) }}" class="btn-edit">Edit</a>
                        <a href="{{ url_for('delete_appointment', appointment_id=appt.id) }}" class="btn-delete" 
                           onclick="return confirm('Are you sure you want to delete this booking?')">Delete</a>
                    </div>
                </div>
            {% endfor %}
            </div>
        {% else %}
            <div class="empty-state">
                <p style="font-size: 48px;">📅</p>
                <p>No upcoming appointments scheduled.</p>
                <p>Click "Create New Booking" to get started!</p>
            </div>
        {% endif %}
    </div>
</body>
</html>
"""

APPOINTMENT_FORM_PAGE = """
<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% if appointment %}Edit{% else %}New{% endif %} Appointment - Event Hall Management</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; 
               background: #f5f5f5; min-height: 100vh; }
        .header { background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
                  color: white; padding: 20px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); }
        .header-content { max-width: 800px; margin: 0 auto; }
        .container { max-width: 800px; margin: 30px auto; padding: 0 20px; }
        .form-card { background: white; padding: 40px; border-radius: 8px; 
                    box-shadow: 0 2px 8px rgba(0,0,0,0.1); }
        h2 { color: #333; margin-bottom: 30px; }
        label { display: block; margin-bottom: 5px; color: #555; font-weight: 500; }
        input, textarea { width: 100%; padding: 12px; margin-bottom: 20px; border: 1px solid #ddd; 
                          border-radius: 5px; font-size: 14px; font-family: inherit; }
        input:focus, textarea:focus { outline: none; border-color: #667eea; }
        textarea { min-height: 100px; resize: vertical; }
        .form-row { display: grid; grid-template-columns: 1fr 1fr; gap: 20px; }
        button { width: 100%; padding: 12px; background: #667eea; color: white; border: none; 
                 border-radius: 5px; font-size: 16px; font-weight: 600; cursor: pointer; }
        button:hover { background: #5568d3; }
        .back-link { display: inline-block; margin-top: 20px; color: #667eea; 
                     text-decoration: none; }
        .back-link:hover { text-decoration: underline; }
        .message { background: #fff3cd; color: #856404; padding: 12px; border-radius: 5px; 
                   margin-bottom: 20px; border: 1px solid #ffeaa7; }
        .help-text { font-size: 12px; color: #999; margin-top: -15px; margin-bottom: 15px; }
    </style>
</head>
<body>
    <div class="header">
        <div class="header-content">
            <h1>{% if appointment %}Edit{% else %}New{% endif %} Appointment</h1>
        </div>
    </div>
    <div class="container">
        <div class="form-card">
            {% if message %}<div class="message">{{ message }}</div>{% endif %}
            <form method="post">
                <label>Event Title *</label>
                <input type="text" name="title" value="{{ appointment.title if appointment else '' }}" 
                       placeholder="e.g., Birthday Party, Business Meeting" required>
                
                <label>Hall Name *</label>
                <input type="text" name="hall_name" value="{{ appointment.hall_name if appointment else '' }}" 
                       placeholder="e.g., Grand Hall, Conference Room A" required>
                
                <div class="form-row">
                    <div>
                        <label>Start Time *</label>
                        <input type="datetime-local" name="start_time" 
                               value="{% if appointment %}{{ appointment.start_time.strftime('%Y-%m-%dT%H:%M') }}{% endif %}" required>
                    </div>
                    <div>
                        <label>End Time *</label>
                        <input type="datetime-local" name="end_time" 
                               value="{% if appointment %}{{ appointment.end_time.strftime('%Y-%m-%dT%H:%M') }}{% endif %}" required>
                    </div>
                </div>
                
                <label>Description</label>
                <textarea name="description" placeholder="Add any additional details about your event...">{{ appointment.description if appointment else '' }}</textarea>
                
                <button type="submit">{% if appointment %}Update{% else %}Create{% endif %} Booking</button>
                <a href="{{ url_for('dashboard') }}" class="back-link">← Back to Dashboard</a>
            </form>
        </div>
    </div>
</body>
</html>
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
    """Display the dashboard with the user's upcoming appointments."""
    now = datetime.now()
    appointments = Appointment.query.filter_by(owner=current_user).filter(
        Appointment.start_time >= now
    ).order_by(Appointment.start_time).all()
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
            # Support both datetime-local format and the old text format
            start_time_str = request.form['start_time']
            end_time_str = request.form['end_time']
            try:
                start_time = datetime.strptime(start_time_str, '%Y-%m-%dT%H:%M')
                end_time = datetime.strptime(end_time_str, '%Y-%m-%dT%H:%M')
            except ValueError:
                start_time = datetime.strptime(start_time_str, '%Y-%m-%d %H:%M')
                end_time = datetime.strptime(end_time_str, '%Y-%m-%d %H:%M')
            description = request.form.get('description')
            # Ensure start_time is before end_time
            if start_time >= end_time:
                message = 'Start time must be earlier than end time.'
            # Check if the hall is available
            elif not Appointment.check_availability(hall_name, start_time, end_time):
                message = 'This hall is not available during the selected time. Please choose a different time or hall.'
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
            hall_name = request.form['hall_name']
            # Support both datetime-local format and the old text format
            start_time_str = request.form['start_time']
            end_time_str = request.form['end_time']
            try:
                start_time = datetime.strptime(start_time_str, '%Y-%m-%dT%H:%M')
                end_time = datetime.strptime(end_time_str, '%Y-%m-%dT%H:%M')
            except ValueError:
                start_time = datetime.strptime(start_time_str, '%Y-%m-%d %H:%M')
                end_time = datetime.strptime(end_time_str, '%Y-%m-%d %H:%M')
            if start_time >= end_time:
                message = 'Start time must be earlier than end time.'
            # Check availability for the new hall/time, excluding this appointment
            elif not Appointment.check_availability(hall_name, start_time, end_time, exclude_id=appointment_id):
                message = 'This hall is not available during the selected time. Please choose a different time or hall.'
            else:
                appt.hall_name = hall_name
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