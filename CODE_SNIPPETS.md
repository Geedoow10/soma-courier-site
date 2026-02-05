# Event Hall Management System - Key Code Snippets

This document highlights the key implementations in the Event Hall Management System.

## 1. Conflict Detection Logic

The core feature that prevents double bookings:

```python
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
```

**How it works:**
- Queries all appointments for the same hall
- Checks for time overlap: `start < existing_end AND end > existing_start`
- This catches all overlap types: exact, partial, encompassing
- When editing, `exclude_id` prevents checking against itself

## 2. Upcoming Appointments Filter

Shows only future appointments on the dashboard:

```python
@app.route('/')
@login_required
def dashboard():
    """Display the dashboard with the user's upcoming appointments."""
    now = datetime.now()
    appointments = Appointment.query.filter_by(owner=current_user).filter(
        Appointment.start_time >= now
    ).order_by(Appointment.start_time).all()
    return render_template_string(DASHBOARD_PAGE, appointments=appointments)
```

**Benefits:**
- Cleaner interface showing only relevant bookings
- Sorted by start time for easy viewing
- Automatically hides past events

## 3. Booking Creation with Validation

Creating a new booking with conflict checking:

```python
@app.route('/appointment/new', methods=['GET', 'POST'])
@login_required
def new_appointment():
    """Create a new appointment."""
    message = ''
    if request.method == 'POST':
        try:
            title = request.form['title']
            hall_name = request.form['hall_name']
            # Support both datetime-local format and text format
            start_time_str = request.form['start_time']
            end_time_str = request.form['end_time']
            try:
                start_time = datetime.strptime(start_time_str, '%Y-%m-%dT%H:%M')
                end_time = datetime.strptime(end_time_str, '%Y-%m-%dT%H:%M')
            except ValueError:
                start_time = datetime.strptime(start_time_str, '%Y-%m-%d %H:%M')
                end_time = datetime.strptime(end_time_str, '%Y-%m-%d %H:%M')
            
            # Validation checks
            if start_time >= end_time:
                message = 'Start time must be earlier than end time.'
            elif not Appointment.check_availability(hall_name, start_time, end_time):
                message = 'This hall is not available during the selected time...'
            else:
                # Create and save the appointment
                appt = Appointment(title=title, hall_name=hall_name,
                                   start_time=start_time, end_time=end_time,
                                   description=description, owner=current_user)
                db.session.add(appt)
                db.session.commit()
                return redirect(url_for('dashboard'))
        except ValueError:
            message = 'Invalid date/time format.'
    return render_template_string(APPOINTMENT_FORM_PAGE, appointment=None, message=message)
```

**Key features:**
- Dual datetime format support (HTML5 datetime-local and text)
- Time validation (start before end)
- Conflict detection before saving
- Clear error messages

## 4. Secure Password Handling

User model with password security:

```python
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
```

**Security features:**
- Passwords hashed using Werkzeug (PBKDF2)
- Never stores plain text passwords
- Secure comparison for authentication

## 5. Database Models

### User Model
- `id`: Primary key
- `username`: Unique identifier for login
- `email`: Unique email address
- `password_hash`: Securely hashed password
- `appointments`: One-to-many relationship

### Appointment Model
```python
class Appointment(db.Model):
    """Appointment model stores hall bookings for a user."""
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128), nullable=False)
    hall_name = db.Column(db.String(128), nullable=False)
    start_time = db.Column(db.DateTime, nullable=False)
    end_time = db.Column(db.DateTime, nullable=False)
    description = db.Column(db.Text, nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
```

## 6. Authentication Flow

### Registration
```python
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        
        # Check for duplicates
        if User.query.filter_by(username=username).first():
            message = 'Username already taken.'
        elif User.query.filter_by(email=email).first():
            message = 'Email already registered.'
        else:
            # Create new user with hashed password
            user = User(username=username, email=email)
            user.set_password(password)
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('login'))
```

### Login
```python
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        
        # Verify credentials
        if user and user.check_password(password):
            login_user(user)  # Start session
            return redirect(url_for('dashboard'))
        message = 'Invalid credentials.'
```

## 7. Modern UI with CSS

Example of the modern gradient design:

```css
body {
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    min-height: 100vh;
    display: flex;
    align-items: center;
    justify-content: center;
}

.container {
    background: white;
    padding: 40px;
    border-radius: 10px;
    box-shadow: 0 10px 40px rgba(0,0,0,0.1);
    max-width: 400px;
    width: 90%;
}
```

## 8. HTML5 Datetime Picker

Modern date/time input in forms:

```html
<label>Start Time *</label>
<input type="datetime-local" name="start_time" 
       value="{% if appointment %}{{ appointment.start_time.strftime('%Y-%m-%dT%H:%M') }}{% endif %}" 
       required>
```

**Advantages:**
- Native browser date/time picker
- Automatic validation
- Consistent user experience
- Mobile-friendly

## 9. Protected Routes

All booking operations require authentication:

```python
@app.route('/')
@login_required  # User must be logged in
def dashboard():
    # Only show appointments owned by current user
    appointments = Appointment.query.filter_by(owner=current_user).filter(
        Appointment.start_time >= datetime.now()
    ).order_by(Appointment.start_time).all()
    return render_template_string(DASHBOARD_PAGE, appointments=appointments)
```

## 10. Edit with Conflict Detection

Editing appointments while checking availability:

```python
@app.route('/appointment/<int:appointment_id>/edit', methods=['GET', 'POST'])
@login_required
def edit_appointment(appointment_id: int):
    appt = Appointment.query.get_or_404(appointment_id)
    
    # Security: Only owner can edit
    if appt.owner != current_user:
        return redirect(url_for('dashboard'))
    
    if request.method == 'POST':
        # ... parse form data ...
        
        # Check availability, excluding this appointment
        if not Appointment.check_availability(hall_name, start_time, end_time, 
                                               exclude_id=appointment_id):
            message = 'This hall is not available...'
        else:
            # Update appointment
            appt.hall_name = hall_name
            appt.start_time = start_time
            appt.end_time = end_time
            db.session.commit()
            return redirect(url_for('dashboard'))
```

**Important:** The `exclude_id` parameter prevents checking against the appointment being edited.

---

## Summary

The implementation provides a complete, production-ready foundation for an event hall management system with:

- **Robust conflict detection** preventing double bookings
- **Secure authentication** with password hashing
- **Modern UI/UX** with responsive design
- **Comprehensive validation** on all inputs
- **Clean code structure** following Flask best practices
- **Extensible architecture** for future enhancements

All core requirements from the problem statement have been successfully implemented.
