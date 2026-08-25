# Local Development Setup Guide

This guide will help you set up the Support Ticket Hub locally for development.

## 🎯 Quick Start (5 minutes)

### Prerequisites
- Python 3.8+
- Node.js 14+
- PostgreSQL 12+ (see [DATABASE_SETUP.md](DATABASE_SETUP.md))
- Git

### Step 1: Clone the Repository
```bash
git clone https://github.com/learningwithmike/support-ticket-hub.git
cd support-ticket-hub
```

### Step 2: Backend Setup
```bash
cd backend

# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Copy environment file and configure
cp .env.example .env
# Edit .env with your database credentials

# Run the application
python run.py
```

Backend will run on: http://localhost:5000

### Step 3: Frontend Setup
```bash
cd frontend

# Install dependencies
npm install

# Create environment file
cp .env.example .env

# Start development server
npm start
```

Frontend will run on: http://localhost:3000

### Step 4: Database Setup
Follow the [DATABASE_SETUP.md](DATABASE_SETUP.md) guide for:
1. Installing PostgreSQL
2. Creating database and user
3. Configuring `.env` file
4. Initializing tables
5. (Optional) Seeding sample data

## 📁 Project Structure

```
support-ticket-hub/
├── backend/                    # Flask API
│   ├── app/
│   │   ├── models/            # Database models
│   │   ├── routes/            # API endpoints
│   │   └── __init__.py        # App factory
│   ├── config.py              # Configuration
│   ├── requirements.txt        # Python dependencies
│   ├── run.py                 # Entry point
│   ├── seed_db.py             # Sample data script
│   └── .env.example           # Environment variables template
│
├── frontend/                   # React App
│   ├── public/                # Static files
│   ├── src/
│   │   ├── pages/             # Page components
│   │   ├── services/          # API calls
│   │   ├── App.js             # Main component
│   │   └── index.js           # React entry
│   ├── package.json           # NPM dependencies
│   └── .env.example           # Environment variables
│
├── DATABASE_SETUP.md          # Database configuration guide
├── CONTRIBUTING.md            # Contribution guidelines
└── README.md                  # Project overview
```

## 🔧 Development Workflow

### First Time Setup
1. Clone repository
2. Follow Backend Setup
3. Follow Frontend Setup
4. Follow Database Setup (DATABASE_SETUP.md)
5. Seed sample data (optional): `python seed_db.py`

### Running Both Servers
**Terminal 1 (Backend):**
```bash
cd backend
source venv/bin/activate  # Windows: venv\Scripts\activate
python run.py
```

**Terminal 2 (Frontend):**
```bash
cd frontend
npm start
```

### Making Changes
- **Backend changes**: Restart Flask server (it may auto-reload)
- **Frontend changes**: React dev server auto-reloads

## 📝 Environment Variables

### Backend (.env)
```
FLASK_ENV=development
FLASK_APP=run.py
SECRET_KEY=your_secret_key_here
DATABASE_URL=postgresql://user:password@localhost:5432/ticket_hub_db
JWT_SECRET_KEY=your_jwt_secret
FRONTEND_URL=http://localhost:3000
```

### Frontend (.env)
```
REACT_APP_API_URL=http://localhost:5000/api
```

## 🧪 Testing

### Test Backend API
```bash
# Get all tickets (requires authentication)
curl -H "Authorization: Bearer YOUR_TOKEN" http://localhost:5000/api/tickets

# Health check (no auth needed)
curl http://localhost:5000/api/health
```

### Test Frontend
- Open http://localhost:3000
- Register a new account or login with demo credentials
- Navigate through pages to verify everything works

## 🐛 Common Issues

### Port Already in Use
**Backend (5000):**
```bash
# Find process using port 5000
lsof -i :5000  # macOS/Linux
netstat -ano | findstr :5000  # Windows

# Kill process
kill -9 <PID>
```

**Frontend (3000):**
```bash
# Find process using port 3000
lsof -i :3000  # macOS/Linux
netstat -ano | findstr :3000  # Windows
```

### Database Connection Error
1. Verify PostgreSQL is running
2. Check DATABASE_URL in `.env`
3. Ensure credentials are correct
4. See DATABASE_SETUP.md troubleshooting section

### Module Not Found
```bash
# Backend
pip install -r requirements.txt

# Frontend
npm install
```

### CORS Errors
Ensure `FRONTEND_URL` in backend `.env` matches your frontend URL (http://localhost:3000)

## 📚 API Documentation

See API endpoints in main [README.md](README.md#api-endpoints)

## 🚀 Ready to Deploy?

When ready to deploy:
1. See [README.md](README.md#deployment) for deployment instructions
2. Use Railway.app or Render.com for backend
3. Use GitHub Pages for frontend

## 💡 Tips

- Install VS Code extensions: Python, ES7+ React/Redux/React-Native snippets
- Use Postman for API testing
- Check browser console for frontend errors (F12)
- Check terminal for backend errors
- Use `git status` to track changes

## ❓ Need Help?

1. Check the main [README.md](README.md)
2. See [DATABASE_SETUP.md](DATABASE_SETUP.md) for database issues
3. Check GitHub Issues for similar problems
4. Read error messages carefully!

---

**Happy coding! 🎉**
