# Event Hall Management System

A web-based event hall booking system built with Flask that allows users to register, log in, and manage their hall reservations.

## Features

### Core Functionality
- **User Authentication**: Secure registration and login system
- **Hall Booking Management**: Create, view, edit, and delete hall reservations
- **Real-time Conflict Detection**: Prevents double-booking of halls
- **Upcoming Appointments Dashboard**: Shows only future bookings
- **Modern UI**: Clean, responsive design with improved user experience

### Key Features
1. **User Registration & Login**: Role-based authentication with secure password hashing
2. **Create Bookings**: Book event halls with title, hall name, date/time range, and description
3. **Edit Bookings**: Modify existing reservations with conflict checking
4. **Delete Bookings**: Remove bookings with confirmation
5. **Conflict Prevention**: Automatic checking to prevent double-booking of halls
6. **Dashboard**: Personal dashboard showing all upcoming appointments

## Technology Stack

- **Backend**: Flask (Python web framework)
- **Database**: SQLite with SQLAlchemy ORM
- **Authentication**: Flask-Login
- **Security**: Werkzeug password hashing
- **UI**: Embedded HTML templates with CSS styling

## Installation

1. **Install Python dependencies**:
   ```bash
   pip install flask flask_sqlalchemy flask_login
   ```

2. **Run the application**:
   ```bash
   python event_hall_app.py
   ```

3. **Access the application**:
   Open your browser and navigate to `http://127.0.0.1:5000`

## Usage

### First Time Setup
1. Navigate to the application URL
2. Click "Register" to create a new account
3. Fill in your username, email, and password
4. Log in with your credentials

### Creating a Booking
1. From the dashboard, click "Create New Booking"
2. Enter the event details:
   - Event title (e.g., "Birthday Party", "Business Meeting")
   - Hall name (e.g., "Grand Hall", "Conference Room A")
   - Start date and time
   - End date and time
   - Optional description
3. Click "Create Booking"
4. If the hall is available, your booking will be created
5. If there's a conflict, you'll receive a message to choose a different time or hall

### Managing Bookings
- **View**: All upcoming bookings are displayed on the dashboard
- **Edit**: Click "Edit" on any booking to modify its details
- **Delete**: Click "Delete" to remove a booking (with confirmation)

### Conflict Detection
The system automatically checks for booking conflicts:
- Each hall can only have one booking at any given time
- When creating or editing a booking, the system verifies no overlapping reservations exist
- If a conflict is detected, you'll be prompted to select a different time or hall

## Database Schema

### User Model
- `id`: Primary key
- `username`: Unique username
- `email`: Unique email address
- `password_hash`: Hashed password

### Appointment Model
- `id`: Primary key
- `title`: Event title
- `hall_name`: Name of the booked hall
- `start_time`: Start date/time
- `end_time`: End date/time
- `description`: Optional event description
- `user_id`: Foreign key to User

## Security Features

- Password hashing using Werkzeug's security module
- Session-based authentication with Flask-Login
- Protected routes requiring login
- User isolation (users can only manage their own bookings)

## Future Enhancements

The following features can be added in future versions:
- Admin approval workflow for bookings
- Usage analytics and reporting
- Email notifications
- Calendar view of bookings
- Multiple hall types and categories
- Booking history (including past appointments)
- Payment integration
- Guest user invitations

## Notes

- The application uses SQLite for simplicity. For production use, consider PostgreSQL or MySQL.
- The secret key is hardcoded for demonstration. In production, use environment variables.
- The app runs in debug mode by default. Disable this in production.
- This is a foundational implementation that can be extended based on specific requirements.

## License

This is a demonstration project for educational purposes.
