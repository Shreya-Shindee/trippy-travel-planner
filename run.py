#!/usr/bin/env python3
"""
Simple runner script for AI Travel Planner
"""

import os
import sys
from dotenv import load_dotenv

def check_env_file():
    """Check if .env file exists and has required keys"""
    if not os.path.exists('.env'):
        print("❌ .env file not found!")
        print("Please run: python setup.py")
        return False
    
    load_dotenv()
    
    gemini_key = os.getenv('GEMINI_API_KEY')
    serp_key = os.getenv('SERP_API_KEY')
    
    if not gemini_key or gemini_key == 'your_gemini_api_key_here':
        print("❌ GEMINI_API_KEY not set in .env file!")
        print("Get your key from: https://makersuite.google.com/app/apikey")
        return False
    
    if not serp_key or serp_key == 'your_serp_api_key_here':
        print("❌ SERP_API_KEY not set in .env file!")
        print("Get your key from: https://serpapi.com/dashboard")
        return False
    
    print("✅ Environment variables configured")
    return True

def main():
    """Main runner function"""
    print("🌍 Starting AI Travel Planner...")
    
    # Check environment
    if not check_env_file():
        sys.exit(1)
    
    # Import and run the app
    try:
        from app import app
        print("🚀 Server starting at http://localhost:5000")
        print("Press Ctrl+C to stop the server")
        app.run(debug=True, host='0.0.0.0', port=5000)
    except ImportError as e:
        print(f"❌ Import error: {e}")
        print("Please run: python setup.py")
        sys.exit(1)
    except KeyboardInterrupt:
        print("\n👋 Server stopped. Goodbye!")
    except Exception as e:
        print(f"❌ Error starting server: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()