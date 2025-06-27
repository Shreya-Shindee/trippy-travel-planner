#!/usr/bin/env python3
"""
Setup script for AI Travel Planner
"""

import os
import sys
import subprocess
import shutil

def check_python_version():
    """Check if Python version is 3.8 or higher"""
    if sys.version_info < (3, 8):
        print("❌ Python 3.8 or higher is required!")
        print(f"Current version: {sys.version}")
        return False
    print(f"✅ Python version: {sys.version.split()[0]}")
    return True

def install_requirements():
    """Install required packages"""
    print("📦 Installing required packages...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("✅ All packages installed successfully!")
        return True
    except subprocess.CalledProcessError:
        print("❌ Failed to install packages!")
        return False

def setup_env_file():
    """Set up environment file"""
    env_file = ".env"
    example_file = ".env.example"
    
    if os.path.exists(env_file):
        print("⚠️  .env file already exists!")
        response = input("Do you want to overwrite it? (y/N): ").lower()
        if response != 'y':
            print("📝 Keeping existing .env file")
            return True
    
    if os.path.exists(example_file):
        shutil.copy(example_file, env_file)
        print("✅ Created .env file from template")
        print("📝 Please edit .env file and add your API keys:")
        print("   - GEMINI_API_KEY (from https://makersuite.google.com/app/apikey)")
        print("   - SERP_API_KEY (from https://serpapi.com/dashboard)")
        return True
    else:
        print("❌ .env.example file not found!")
        return False

def main():
    """Main setup function"""
    print("🌍 AI Travel Planner Setup")
    print("=" * 40)
    
    # Check Python version
    if not check_python_version():
        sys.exit(1)
    
    # Install requirements
    if not install_requirements():
        sys.exit(1)
    
    # Setup environment file
    if not setup_env_file():
        sys.exit(1)
    
    print("\n🎉 Setup completed successfully!")
    print("\n📋 Next steps:")
    print("1. Edit the .env file and add your API keys")
    print("2. Run: python app.py")
    print("3. Open http://localhost:5000 in your browser")
    print("\n🚀 Happy traveling!")

if __name__ == "__main__":
    main()