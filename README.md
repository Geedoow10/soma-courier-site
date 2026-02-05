# Event Hall Management System

Welcome to the Event Hall Management System! This comprehensive platform makes booking and managing event halls simple, efficient, and conflict-free.

## 🌐 Live Website

**Status:** ✅ **Ready for Production Deployment**

**Landing Page:** Available on GitHub Pages after deployment  
**Application:** Flask-based booking system (requires separate deployment)

👉 **[See DEPLOYMENT.md for complete deployment instructions](DEPLOYMENT.md)**

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

### Option 1: Local Development

**Landing Page:**
```bash
# Open in browser
open index.html
# or on Linux
xdg-open index.html
# or on Windows
start index.html
```

**Flask Application:**
```bash
# Install dependencies
pip install -r requirements.txt

# Run the application
python event_hall_app.py

# Visit http://127.0.0.1:5000
```

### Option 2: Deploy to Production

**📚 Complete deployment guide:** See **[DEPLOYMENT.md](DEPLOYMENT.md)**

**Quick Summary:**
1. Deploy landing page to GitHub Pages (automatic with this repo)
2. Deploy Flask app to Heroku, PythonAnywhere, or Render
3. Update `APP_CONFIG` in `index.html` with your Flask app URL
4. Push changes and you're live!

## 📂 Project Structure

```
event-hall-management/
├── index.html                 # Landing page with dynamic URL config
├── event_hall_app.py          # Flask booking application (production-ready)
│
├── Procfile                   # Heroku deployment configuration
├── requirements.txt           # Python dependencies
├── runtime.txt                # Python version specification
│
├── README.md                  # This file
├── DEPLOYMENT.md              # 🚀 Complete deployment guide
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

**Note:** The app now automatically handles environment variables for production deployment. See [DEPLOYMENT.md](DEPLOYMENT.md) for complete instructions.

## 🚢 Deployment

### ⚡ Quick Deploy

The system is now **production-ready** with all deployment files included!

**🎯 See [DEPLOYMENT.md](DEPLOYMENT.md) for the complete step-by-step guide.**

### Landing Page (GitHub Pages)

Already configured! Just enable GitHub Pages in repository settings:
1. Go to Settings → Pages
2. Select branch: `copilot/create-event-hall-management-system`
3. Click Save
4. Site will be live at `https://geedoow10.github.io/soma-courier-site/`

### Flask Application (Heroku/PythonAnywhere/Render)

**Files included for deployment:**
- ✅ `Procfile` - Heroku configuration
- ✅ `requirements.txt` - Python dependencies
- ✅ `runtime.txt` - Python version
- ✅ Production-ready `event_hall_app.py` with environment variables

**One-command Heroku deploy:**
```bash
heroku create your-event-hall-app
heroku config:set SECRET_KEY="your-secret-key-here"
git push heroku copilot/create-event-hall-management-system:main
```

**After deployment:**
- Update `APP_CONFIG.flaskAppUrl` in `index.html`
- Set `APP_CONFIG.isAppDeployed = true`
- Push changes to update landing page

### Production Checklist

**Landing Page:**
- ✅ GitHub Pages enabled
- ✅ `APP_CONFIG` updated with Flask URL
- ✅ `isAppDeployed` set to `true`

**Flask Application:**
- ✅ `SECRET_KEY` environment variable set
- ✅ `DATABASE_URL` configured (for PostgreSQL)
- ✅ HTTPS enabled (automatic on most platforms)
- ✅ Debug mode disabled (automatic via env vars)

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

1. **Deploy landing page:** Enable GitHub Pages (see [DEPLOYMENT.md](DEPLOYMENT.md))
2. **Deploy Flask app:** Follow Heroku quick-start guide
3. **Connect the two:** Update APP_CONFIG in index.html
4. **Go live!** Your Event Hall Management System is ready!

## 🎉 Production Status

**✅ READY TO PUBLISH**

This system is production-ready with:
- ✅ Modern, responsive landing page
- ✅ Full-featured booking application
- ✅ Deployment files and configuration
- ✅ Comprehensive documentation
- ✅ Security best practices
- ✅ Environment variable support

**📚 Complete deployment guide:** [DEPLOYMENT.md](DEPLOYMENT.md)

## 📧 Support

For questions, issues, or feature requests:
- Check the [deployment guide](DEPLOYMENT.md)
- Review the [documentation files](README_EVENT_HALL.md)
- See the [code examples](CODE_SNIPPETS.md)
- View the [visual previews](PREVIEW.md)

---

**Built with ❤️ for seamless event planning**

**Status:** ✅ Production-Ready | 🚀 Ready to Deploy  
**Last Updated:** February 2026
