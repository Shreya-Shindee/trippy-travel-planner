# 🚀 Deployment Guide for Trippy Travel Planner

## 🌐 Deploy to Heroku (Recommended)

### Step 1: Prerequisites
1. Create a Heroku account at [heroku.com](https://heroku.com)
2. Install [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli)
3. Get your API keys:
   - **Gemini AI API**: [Get here](https://makersuite.google.com/app/apikey)
   - **SERP API**: [Get here](https://serpapi.com/dashboard)

### Step 2: Create Heroku App
```bash
# Login to Heroku
heroku login

# Create new app (replace 'your-app-name' with unique name)
heroku create trippy-travel-planner

# Or if you prefer a random name
heroku create
```

### Step 3: Set Environment Variables
```bash
# Set your API keys as environment variables
heroku config:set GEMINI_API_KEY=your_actual_gemini_api_key
heroku config:set SERP_API_KEY=your_actual_serp_api_key
heroku config:set FLASK_SECRET_KEY=your_secure_random_secret_key
heroku config:set FLASK_ENV=production

# Optional: Set database URL (Heroku will auto-provide)
# heroku addons:create heroku-postgresql:hobby-dev
```

### Step 4: Deploy to Heroku
```bash
# Initialize git repository (if not already done)
git init
git add .
git commit -m "Initial commit - Trippy Travel Planner"

# Add Heroku remote
heroku git:remote -a your-app-name

# Deploy to Heroku
git push heroku main
```

### Step 5: Access Your Live App
```bash
# Open your deployed app
heroku open

# Or visit: https://your-app-name.herokuapp.com
```

## 🔧 Alternative Deployments

### Render.com
1. Connect your GitHub repository to [Render](https://render.com)
2. Set environment variables in Render dashboard
3. Deploy with one click

### Railway.app
1. Connect repository to [Railway](https://railway.app)
2. Set environment variables
3. Deploy automatically

### PythonAnywhere
1. Upload code to [PythonAnywhere](https://pythonanywhere.com)
2. Configure WSGI file
3. Set environment variables

## 🔐 Environment Variables Required

| Variable | Description | Required |
|----------|-------------|----------|
| `GEMINI_API_KEY` | Google Gemini AI API key | Yes |
| `SERP_API_KEY` | SERP API key for flight/hotel search | Yes |
| `FLASK_SECRET_KEY` | Secret key for Flask sessions | Yes |
| `FLASK_ENV` | Set to 'production' | Yes |
| `DATABASE_URL` | Database connection (auto-set by Heroku) | Auto |

## 🎯 Quick Heroku Deploy Commands

```bash
# 1. Create and configure
heroku create trippy-travel-planner
heroku config:set GEMINI_API_KEY=your_key_here
heroku config:set SERP_API_KEY=your_key_here
heroku config:set FLASK_SECRET_KEY=your_secret_key
heroku config:set FLASK_ENV=production

# 2. Deploy
git add .
git commit -m "Deploy Trippy"
git push heroku main

# 3. Open app
heroku open
```

## 🐛 Troubleshooting

### Common Issues:
1. **Build fails**: Check requirements.txt has all dependencies
2. **App crashes**: Check heroku logs with `heroku logs --tail`
3. **Database errors**: Ensure DATABASE_URL is set
4. **API errors**: Verify your API keys are correct

### Useful Commands:
```bash
# View logs
heroku logs --tail

# Restart app
heroku restart

# Check config
heroku config

# Scale dynos
heroku ps:scale web=1
```

## ✅ Post-Deployment Checklist

- [ ] App loads successfully
- [ ] Flight search works
- [ ] Hotel search works
- [ ] Chat assistant responds
- [ ] User registration/login works
- [ ] Trip saving works
- [ ] All API integrations functional

## 🌟 Live Demo

Once deployed, your app will be available at:
**https://your-app-name.herokuapp.com**

Share this link with users to access your live travel planner!
