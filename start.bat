@echo off
echo 🌍 AI Travel Planner
echo ==================

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python is not installed or not in PATH
    echo Please install Python 3.8+ from https://python.org
    pause
    exit /b 1
)

REM Check if .env file exists
if not exist .env (
    echo ❌ .env file not found!
    echo Running setup...
    python setup.py
    echo.
    echo ⚠️  Please edit .env file with your API keys and run this script again.
    pause
    exit /b 1
)

REM Install requirements if needed
if not exist venv (
    echo 📦 Creating virtual environment...
    python -m venv venv
)

echo 🔧 Activating virtual environment...
call venv\Scripts\activate.bat

echo 📦 Installing/updating requirements...
pip install -r requirements.txt

echo 🚀 Starting AI Travel Planner...
python app.py

pause