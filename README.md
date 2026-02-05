# Event Hall Management System

Welcome to the Event Hall Management System! This comprehensive platform makes booking and managing event halls simple, efficient, and conflict-free.

## 🌐 Live Website

**Landing Page:** `index.html` - Modern promotional website for the Event Hall Management System  
**Application:** `event_hall_app.py` - Flask-based booking management application

## 📦 What's Included

This repository contains a complete event hall booking solution:

### 1. Landing Page (index.html)
A beautiful, modern website that introduces the Event Hall Management System.

**Features:**
- 🎨 Purple gradient theme matching the application
- 📱 Fully responsive design using Tailwind CSS
- ✨ Smooth animations and hover effects
- 📋 Features showcase
- 📖 How it works section
- 💼 About and contact information
- 🚀 Direct links to the booking application

### 2. Event Hall Management Application (event_hall_app.py)
A Flask-based web application for managing event hall bookings.

**Features:**
- 👤 User registration and authentication
- 📅 Create, edit, and delete hall bookings
- ⚠️ Real-time conflict detection (prevents double bookings)
- 📊 Personal dashboard showing upcoming appointments
- 🎨 Modern purple gradient design theme (#667eea → #764ba2)
- 🔒 Secure password hashing and session management
- 📱 Responsive HTML5 datetime pickers

**Documentation:**
- **[README_EVENT_HALL.md](README_EVENT_HALL.md)** - Detailed setup and usage guide
- **[FEATURES_OVERVIEW.md](FEATURES_OVERVIEW.md)** - Complete feature documentation
- **[CODE_SNIPPETS.md](CODE_SNIPPETS.md)** - Implementation examples and code reference
- **[PREVIEW.md](PREVIEW.md)** - Visual preview with ASCII mockups
- **[PURPLE_THEME.md](PURPLE_THEME.md)** - Design theme guide and color palette

## 🚀 Quick Start

### Viewing the Landing Page

The landing page is a static HTML file that can be opened directly:

```bash
# Open in browser
open index.html
# or on Linux
xdg-open index.html
# or on Windows
start index.html
```

For deployment, simply upload `index.html` to any static hosting service (GitHub Pages, Netlify, Vercel, etc.).

### Running the Event Hall Application

1. **Install dependencies:**
   ```bash
   pip install flask flask_sqlalchemy flask_login
   ```

2. **Run the application:**
   ```bash
   python event_hall_app.py
   ```

3. **Access the application:**
   - Open `http://127.0.0.1:5000` in your browser
   - Register a new account
   - Start creating hall bookings!

## 📂 Project Structure

```
event-hall-management/
├── index.html                 # Landing page (new Event Hall website)
├── event_hall_app.py          # Flask booking application
│
├── README.md                  # This file
├── README_EVENT_HALL.md       # Application setup guide
├── FEATURES_OVERVIEW.md       # Feature documentation
├── CODE_SNIPPETS.md           # Code examples
├── PREVIEW.md                 # Visual mockups
├── PURPLE_THEME.md            # Design theme guide
│
├── .gitignore                 # Git ignore rules
└── old_soma_courier/          # Archived files (ignored by git)
```

## 🎨 Design & Branding

### Purple Gradient Theme

The entire system uses a cohesive purple gradient design:

- **Primary Gradient:** `linear-gradient(135deg, #667eea 0%, #764ba2 100%)`
- **Primary Color:** `#667eea` (Soft Purple)
- **Accent Color:** `#764ba2` (Deep Purple)
- **Hover State:** `#5568d3` (Darker Purple)

**Where it's used:**
- Landing page header and hero sections
- Application login/register pages
- Dashboard headers
- Primary buttons and links
- Focus states on inputs

### Typography & Framework

- **Frontend Framework:** Tailwind CSS (CDN)
- **Font Family:** System fonts (Apple, Segoe UI, Roboto)
- **Responsive Design:** Mobile-first approach
- **Icons:** SVG icons for performance

## 💻 Technology Stack

### Landing Page
- HTML5
- CSS3 (Tailwind CSS)
- Vanilla JavaScript (smooth scrolling)
- SVG graphics

### Flask Application
- **Backend:** Python 3.x, Flask
- **Database:** SQLite with SQLAlchemy ORM
- **Authentication:** Flask-Login
- **Security:** Werkzeug password hashing
- **Frontend:** Embedded HTML templates with CSS

## 🔐 Security Features

- **Password Hashing:** Werkzeug PBKDF2 encryption
- **SQL Injection Protection:** SQLAlchemy ORM
- **XSS Protection:** Template escaping
- **Session Management:** Flask-Login secure sessions
- **User Isolation:** Users can only manage their own bookings

**Important:** Change the `SECRET_KEY` in `event_hall_app.py` before production deployment.

## 🚢 Deployment

### Landing Page Deployment

The landing page is ready to deploy to any static hosting:

**GitHub Pages:**
1. Push to GitHub
2. Enable GitHub Pages in repository settings
3. Select main branch
4. Site will be live at `https://yourusername.github.io/repo-name/`

**Netlify/Vercel:**
1. Connect repository
2. Deploy automatically

**Note:** Update the Flask app URLs in `index.html` to point to your deployed application URL instead of `http://127.0.0.1:5000`.

### Flask Application Deployment

For production deployment of the booking system:

**Heroku:**
```bash
# Create Procfile
echo "web: python event_hall_app.py" > Procfile

# Create requirements.txt
pip freeze > requirements.txt

# Deploy
heroku create your-app-name
git push heroku main
```

**PythonAnywhere, DigitalOcean, AWS, GCP:**
- See [README_EVENT_HALL.md](README_EVENT_HALL.md) for detailed deployment instructions

**Production Checklist:**
- ✅ Change SECRET_KEY to secure random value
- ✅ Use environment variables for configuration
- ✅ Upgrade from SQLite to PostgreSQL/MySQL
- ✅ Enable HTTPS
- ✅ Set DEBUG = False
- ✅ Configure proper logging
- ✅ Set up database backups

## 📚 Documentation

### Complete Documentation Suite

1. **[README_EVENT_HALL.md](README_EVENT_HALL.md)** - Application installation and usage
2. **[FEATURES_OVERVIEW.md](FEATURES_OVERVIEW.md)** - All features explained in detail
3. **[PREVIEW.md](PREVIEW.md)** - Visual mockups and design previews
4. **[PURPLE_THEME.md](PURPLE_THEME.md)** - Complete color system and theming guide
5. **[CODE_SNIPPETS.md](CODE_SNIPPETS.md)** - Code examples and implementation details

## 🎯 Use Cases

Perfect for:
- 🏢 **Corporate Events** - Meeting rooms, conference halls, training spaces
- 🎊 **Social Events** - Birthday parties, weddings, celebrations
- 🎓 **Educational** - Classrooms, lecture halls, seminar rooms
- 🏛️ **Community Centers** - Public halls, activity rooms
- 🎭 **Entertainment Venues** - Performance spaces, studios
- 🏋️ **Fitness Centers** - Studio rooms, activity halls

## 🤝 Contributing

This project is set up for easy customization:

1. **Customize the landing page** - Edit `index.html` to match your branding
2. **Extend the Flask app** - Add features in `event_hall_app.py`
3. **Update theme** - Modify colors in `PURPLE_THEME.md` for reference
4. **Add documentation** - Help others understand your changes

## 📄 License

© 2026 Event Hall Management System. Open source project for event management.

## 🎉 Getting Started

Ready to streamline your hall bookings?

1. **Try the landing page:** Open `index.html` in your browser
2. **Run the application:** `python event_hall_app.py`
3. **Create an account:** Register at `http://127.0.0.1:5000/register`
4. **Make your first booking:** Click "Create New Booking" from the dashboard

## 📧 Support

For questions, issues, or feature requests:
- Check the [documentation files](README_EVENT_HALL.md)
- Review the [code examples](CODE_SNIPPETS.md)
- See the [visual previews](PREVIEW.md)

---

**Built with ❤️ for seamless event planning**

Last Updated: February 2026
