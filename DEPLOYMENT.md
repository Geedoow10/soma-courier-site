# 🚀 Deployment Guide - Event Hall Management System

This guide will help you deploy both components of the Event Hall Management System.

## Overview

The Event Hall Management System consists of two parts:
1. **Static Landing Page** (`index.html`) - Deploy to GitHub Pages or any static hosting
2. **Flask Application** (`event_hall_app.py`) - Deploy to a Python hosting service

## Part 1: Deploy Static Landing Page to GitHub Pages

### Step 1: Enable GitHub Pages

1. Go to your repository on GitHub: `https://github.com/Geedoow10/soma-courier-site`
2. Click on **Settings** tab
3. Scroll down to **Pages** section (left sidebar)
4. Under **Source**, select the branch: `copilot/create-event-hall-management-system` (or `main` if merged)
5. Click **Save**
6. Wait a few minutes for deployment

Your landing page will be available at:
```
https://geedoow10.github.io/soma-courier-site/
```

### Step 2: Verify Landing Page

Visit the URL above to confirm the landing page is live. You should see the purple gradient Event Hall Management website.

## Part 2: Deploy Flask Application

You have several options for deploying the Flask application:

### Option A: Heroku (Recommended for Beginners)

#### Prerequisites
- Heroku account (free tier available)
- Heroku CLI installed

#### Steps

1. **Create required files in your repository:**

Create `Procfile`:
```bash
web: python event_hall_app.py
```

Create `requirements.txt`:
```bash
Flask==2.3.2
Flask-SQLAlchemy==3.0.5
Flask-Login==0.6.2
gunicorn==21.2.0
```

Create `runtime.txt` (optional):
```
python-3.11.4
```

2. **Update `event_hall_app.py` for production:**

Change the last line from:
```python
if __name__ == '__main__':
    app.run(debug=True)
```

To:
```python
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
```

Also add at the top:
```python
import os
```

And update the SECRET_KEY:
```python
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'change_me_to_a_secret_value')
```

3. **Deploy to Heroku:**

```bash
# Login to Heroku
heroku login

# Create a new Heroku app
heroku create your-event-hall-app

# Set environment variables
heroku config:set SECRET_KEY="your-super-secret-random-key-here"

# Deploy
git push heroku copilot/create-event-hall-management-system:main

# Open your app
heroku open
```

Your Flask app will be available at:
```
https://your-event-hall-app.herokuapp.com
```

### Option B: PythonAnywhere (Free Tier Available)

1. Create account at [pythonanywhere.com](https://www.pythonanywhere.com)
2. Upload `event_hall_app.py` via Files tab
3. Install dependencies in Bash console:
   ```bash
   pip install --user flask flask_sqlalchemy flask_login
   ```
4. Configure web app in Web tab
5. Set WSGI file to point to your app
6. Reload web app

### Option C: Render (Modern Alternative)

1. Create account at [render.com](https://render.com)
2. Create new "Web Service"
3. Connect your GitHub repository
4. Configure:
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `python event_hall_app.py`
5. Add environment variables (SECRET_KEY)
6. Deploy

## Part 3: Connect Landing Page to Flask App

Once your Flask app is deployed, update the landing page configuration:

### Step 1: Update APP_CONFIG in index.html

Edit `index.html` and find the `APP_CONFIG` section near the top:

```javascript
const APP_CONFIG = {
  // Update this with your deployed Flask app URL
  flaskAppUrl: 'https://your-event-hall-app.herokuapp.com',
  // Set to true when Flask app is deployed
  isAppDeployed: true
};
```

### Step 2: Commit and Push Changes

```bash
git add index.html
git commit -m "Update Flask app URL for production"
git push origin copilot/create-event-hall-management-system
```

GitHub Pages will automatically redeploy with the updated configuration.

## Part 4: Verification

### Test the Complete System

1. **Visit your landing page:**
   - `https://geedoow10.github.io/soma-courier-site/`

2. **Click "Get Started Free"** - Should redirect to Flask app registration
   - `https://your-event-hall-app.herokuapp.com/register`

3. **Register a new account** on the Flask app

4. **Create a test booking** to ensure everything works

5. **Verify conflict detection** by trying to book the same hall at overlapping times

## Production Checklist

Before going live, ensure:

### Landing Page
- [ ] GitHub Pages is enabled and site is accessible
- [ ] APP_CONFIG points to deployed Flask app
- [ ] isAppDeployed is set to `true`
- [ ] All links work correctly
- [ ] Site loads properly on mobile devices

### Flask Application
- [ ] SECRET_KEY is set to a secure random value
- [ ] DEBUG is set to False
- [ ] Database is configured (SQLite for small scale, PostgreSQL for production)
- [ ] HTTPS is enabled (most platforms do this automatically)
- [ ] Environment variables are properly set
- [ ] Registration and login work
- [ ] Booking creation, editing, deletion work
- [ ] Conflict detection works

## Database Considerations

### For Production Use

The default SQLite database works for development but for production you should:

1. **Upgrade to PostgreSQL** (Heroku has free tier)

2. **Update database URI:**
   ```python
   app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///event_hall.db')
   ```

3. **Set on Heroku:**
   ```bash
   heroku addons:create heroku-postgresql:mini
   ```

## Troubleshooting

### Landing Page Issues

**Problem:** Page doesn't load on GitHub Pages
- Check that GitHub Pages is enabled in settings
- Verify the correct branch is selected
- Wait a few minutes for deployment

**Problem:** Buttons show "Setup Required" notice
- Update APP_CONFIG in index.html
- Set isAppDeployed to true
- Push changes to GitHub

### Flask App Issues

**Problem:** App crashes on startup
- Check Heroku logs: `heroku logs --tail`
- Verify all dependencies in requirements.txt
- Ensure PORT environment variable is used

**Problem:** Database errors
- Run database initialization on first deploy
- For Heroku: `heroku run python`
  ```python
  from event_hall_app import app, db
  with app.app_context():
      db.create_all()
  ```

**Problem:** Can't register users
- Check that SECRET_KEY is set
- Verify database is initialized
- Check logs for specific errors

## Maintenance

### Updating the Site

**For Landing Page:**
```bash
# Make changes to index.html
git add index.html
git commit -m "Update landing page"
git push origin copilot/create-event-hall-management-system
# GitHub Pages auto-deploys
```

**For Flask App:**
```bash
# Make changes to event_hall_app.py
git add event_hall_app.py
git commit -m "Update Flask app"
git push heroku copilot/create-event-hall-management-system:main
```

### Monitoring

- **GitHub Pages:** Check GitHub Actions tab for deployment status
- **Heroku:** Use `heroku logs --tail` to monitor application
- **Database:** Regularly backup your database

## Security Notes

1. **Never commit sensitive data:**
   - Use environment variables for secrets
   - Add `.env` to `.gitignore`

2. **Use strong SECRET_KEY:**
   ```python
   import secrets
   secrets.token_hex(32)
   ```

3. **Enable HTTPS:**
   - GitHub Pages: Automatic
   - Heroku: Automatic
   - Other platforms: Check documentation

4. **Regular updates:**
   - Keep Flask and dependencies updated
   - Monitor security advisories

## Support

If you encounter issues:

1. Check the logs (GitHub Actions, Heroku logs)
2. Review this deployment guide
3. Consult platform-specific documentation:
   - [GitHub Pages Docs](https://docs.github.com/pages)
   - [Heroku Python Docs](https://devcenter.heroku.com/categories/python-support)
   - [PythonAnywhere Help](https://help.pythonanywhere.com/)

## Next Steps

After successful deployment:

1. Test all features thoroughly
2. Set up database backups
3. Configure custom domain (optional)
4. Add monitoring/analytics (optional)
5. Create user documentation
6. Plan for scaling if needed

---

**Congratulations! Your Event Hall Management System is now live! 🎉**
