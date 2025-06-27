#!/bin/bash

echo "🌍 AI Travel Planner"
echo "=================="

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed"
    echo "Please install Python 3.8+ from https://python.org"
    exit 1
fi

# Check if .env file exists
if [ ! -f .env ]; then
    echo "❌ .env file not found!"
    echo "Running setup..."
    python3 setup.py
    echo ""
    echo "⚠️  Please edit .env file with your API keys and run this script again."
    exit 1
fi

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    echo "📦 Creating virtual environment..."
    python3 -m venv venv
fi

echo "🔧 Activating virtual environment..."
source venv/bin/activate

echo "📦 Installing/updating requirements..."
pip install -r requirements.txt

echo "🚀 Starting AI Travel Planner..."
python app.py