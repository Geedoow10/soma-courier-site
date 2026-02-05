# Soma Courier Limited - Website & Event Hall Management System

Welcome to the Soma Courier Limited repository! This project contains both the company website and an event hall booking management system.

## 🌐 Live Website

**Domain:** [somacourier.com](http://somacourier.com)

## 📦 Repository Contents

This repository includes two main components:

### 1. Soma Courier Limited Website
A professional business website for cleaning and delivery services in London.

**Main File:** `index.html` (also available as `soma_courier_site.html`)

**Features:**
- 🏠 Modern, responsive design
- 📱 Mobile-friendly layout using Tailwind CSS
- 🎨 Clean, professional interface
- 📞 Contact information and booking forms
- 💼 Service descriptions and pricing
- 🖼️ Gallery with service images
- 💳 PayPal payment integration

**Services Offered:**
- Regular cleaning (homes and offices)
- Deep cleaning (end of tenancy, after builders)
- Window and carpet cleaning
- Same day delivery (London wide)
- Next day delivery (business to business)
- Pay as you go or contract options

### 2. Event Hall Management System
A Flask-based web application for managing event hall bookings.

**Main File:** `event_hall_app.py`

**Features:**
- 👤 User registration and authentication
- 📅 Create, edit, and delete hall bookings
- ⚠️ Real-time conflict detection (prevents double bookings)
- 📊 Personal dashboard showing upcoming appointments
- 🎨 Modern purple gradient design theme
- 🔒 Secure password hashing and session management

**Documentation:**
- **[README_EVENT_HALL.md](README_EVENT_HALL.md)** - Setup and usage guide
- **[FEATURES_OVERVIEW.md](FEATURES_OVERVIEW.md)** - Detailed feature documentation
- **[CODE_SNIPPETS.md](CODE_SNIPPETS.md)** - Key implementation examples
- **[PREVIEW.md](PREVIEW.md)** - Visual preview with ASCII mockups
- **[PURPLE_THEME.md](PURPLE_THEME.md)** - Complete design theme guide

## 🚀 Quick Start

### Viewing the Soma Courier Website

The website is ready to deploy and can be viewed by:

1. **Local Preview:**
   ```bash
   # Open index.html in your browser
   open index.html
   # or on Linux
   xdg-open index.html
   ```

2. **Static Hosting:**
   - Deploy to GitHub Pages, Netlify, or Vercel
   - The site uses CDN resources (Tailwind CSS)
   - No build process required

### Running the Event Hall Management System

1. **Install dependencies:**
   ```bash
   pip install flask flask_sqlalchemy flask_login
   ```

2. **Run the application:**
   ```bash
   python event_hall_app.py
   ```

3. **Access the app:**
   - Open `http://127.0.0.1:5000` in your browser
   - Register a new account
   - Start creating hall bookings!

## 📂 Project Structure

```
soma-courier-site/
├── index.html                 # Main Soma Courier website
├── soma_courier_site.html     # Copy of main website
├── CNAME                      # Custom domain configuration
│
├── event_hall_app.py          # Event hall booking system
├── README_EVENT_HALL.md       # Event hall documentation
├── FEATURES_OVERVIEW.md       # Feature details
├── CODE_SNIPPETS.md           # Code examples
├── PREVIEW.md                 # Visual preview
├── PURPLE_THEME.md            # Design theme guide
│
├── carpet.png                 # Gallery image
├── cleaning.png               # Gallery image
├── delivery.png               # Gallery image
│
└── .gitignore                 # Git ignore rules
```

## 🎨 Design & Branding

### Soma Courier Website
- **Color Scheme:** Blue (#3b82f6) and white
- **Typography:** System fonts for clean, modern look
- **Framework:** Tailwind CSS 2.2.19
- **Layout:** Responsive grid with mobile-first approach

### Event Hall App
- **Color Scheme:** Purple gradient (#667eea to #764ba2)
- **Typography:** Apple, Segoe UI, Roboto system fonts
- **Framework:** Custom CSS with embedded templates
- **Layout:** Card-based design with modern aesthetics

## 💻 Technologies Used

### Website
- HTML5
- CSS3 (via Tailwind CSS)
- JavaScript (inline)
- FormSubmit.co for contact forms
- PayPal integration for payments

### Event Hall App
- **Backend:** Python 3.x, Flask
- **Database:** SQLite with SQLAlchemy ORM
- **Authentication:** Flask-Login
- **Security:** Werkzeug password hashing
- **Frontend:** Embedded HTML templates with CSS

## 📧 Contact Information

**Company:** Soma Courier Limited  
**Phone:** [07799558037](tel:+447799558037)  
**Email:** [adanawale6@gmail.com](mailto:adanawale6@gmail.com)  
**Address:** 163 Cranleigh Gardens, Southall, UB1 2BY  
**Company Number:** 14326871

**Hours:** Monday to Saturday, 8:00 to 20:00

## 🚢 Deployment

### GitHub Pages (Website)

The Soma Courier website is configured for GitHub Pages with a custom domain:

1. Repository is already configured with `CNAME` file
2. GitHub Pages serves `index.html` automatically
3. Custom domain: somacourier.com

### Event Hall App Deployment

For production deployment of the event hall app:

1. **Update Configuration:**
   - Change `SECRET_KEY` to a secure random value
   - Use environment variables for sensitive data
   - Switch from SQLite to PostgreSQL/MySQL
   - Disable debug mode

2. **Hosting Options:**
   - Heroku
   - PythonAnywhere
   - DigitalOcean
   - AWS/GCP/Azure

3. **Production Checklist:**
   - ✅ Set secure SECRET_KEY
   - ✅ Use production database
   - ✅ Enable HTTPS
   - ✅ Set DEBUG = False
   - ✅ Configure proper logging
   - ✅ Set up backup strategy

## 📚 Documentation Links

### Main Website
- See `index.html` source code for implementation details
- Contact forms use [FormSubmit.co](https://formsubmit.co/)
- Payment integration via [PayPal](https://www.paypal.com/)

### Event Hall System
- **[README_EVENT_HALL.md](README_EVENT_HALL.md)** - Complete setup guide
- **[FEATURES_OVERVIEW.md](FEATURES_OVERVIEW.md)** - All features explained
- **[PREVIEW.md](PREVIEW.md)** - Visual mockups and design
- **[PURPLE_THEME.md](PURPLE_THEME.md)** - Color system and theming
- **[CODE_SNIPPETS.md](CODE_SNIPPETS.md)** - Implementation reference

## 🛠️ Development

### Local Development

**Website:**
```bash
# No build required - just open index.html
# Or serve with Python
python -m http.server 8000
# Visit http://localhost:8000
```

**Event Hall App:**
```bash
# Install dependencies
pip install flask flask_sqlalchemy flask_login

# Run in debug mode
python event_hall_app.py

# Visit http://127.0.0.1:5000
```

### Testing

**Website:**
- Test all navigation links
- Verify contact form submission
- Check PayPal payment flow
- Test on different devices/browsers

**Event Hall App:**
- Test user registration and login
- Create test bookings
- Verify conflict detection
- Check edit and delete operations

## 🔐 Security Notes

### Website
- Contact forms handled by FormSubmit.co (third-party service)
- PayPal handles payment processing securely
- No sensitive data stored client-side

### Event Hall App
- Passwords hashed using Werkzeug PBKDF2
- SQL injection protection via SQLAlchemy ORM
- XSS protection through template escaping
- Session management with Flask-Login
- **Important:** Change SECRET_KEY before production deployment

## 🤝 Contributing

This is a commercial project for Soma Courier Limited. For inquiries or contributions, please contact the company directly.

## 📄 License

© 2024 Soma Courier Limited. All rights reserved.

This project contains proprietary business information for Soma Courier Limited, a registered company in the UK (Company Number: 14326871).

## 🎉 Project Status

**Status:** ✅ **READY FOR PRODUCTION**

Both the Soma Courier website and Event Hall Management System are fully functional and ready for deployment.

### Website ✅
- [x] Complete design and layout
- [x] All sections implemented
- [x] Contact forms functional
- [x] Payment integration working
- [x] Responsive design
- [x] Domain configured (somacourier.com)

### Event Hall App ✅
- [x] User authentication complete
- [x] Booking CRUD operations
- [x] Conflict detection working
- [x] Dashboard implemented
- [x] Modern UI with purple theme
- [x] Comprehensive documentation
- [x] Security features in place

---

**Last Updated:** February 2026  
**Maintained by:** Soma Courier Limited

For questions or support, please contact: [adanawale6@gmail.com](mailto:adanawale6@gmail.com)
