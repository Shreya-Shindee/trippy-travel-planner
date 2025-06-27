#!/usr/bin/env python3
"""
Test script to verify AI Travel Planner setup
"""

import os
import sys
from dotenv import load_dotenv

def test_imports():
    """Test if all required packages can be imported"""
    print("🧪 Testing package imports...")
    
    try:
        import flask
        print(f"✅ Flask {flask.__version__}")
    except ImportError:
        print("❌ Flask not installed")
        return False
    
    try:
        import google.generativeai as genai
        print("✅ Google Generative AI")
    except ImportError:
        print("❌ Google Generative AI not installed")
        return False
    
    try:
        from serpapi import GoogleSearch
        print("✅ SerpAPI")
    except ImportError:
        print("❌ SerpAPI not installed")
        return False
    
    try:
        import requests
        print("✅ Requests")
    except ImportError:
        print("❌ Requests not installed")
        return False
    
    return True

def test_env_variables():
    """Test if environment variables are set"""
    print("\n🔧 Testing environment variables...")
    
    load_dotenv()
    
    gemini_key = os.getenv('GEMINI_API_KEY')
    serp_key = os.getenv('SERP_API_KEY')
    
    if not gemini_key or gemini_key == 'your_gemini_api_key_here':
        print("❌ GEMINI_API_KEY not properly set")
        return False
    else:
        print("✅ GEMINI_API_KEY configured")
    
    if not serp_key or serp_key == 'your_serp_api_key_here':
        print("❌ SERP_API_KEY not properly set")
        return False
    else:
        print("✅ SERP_API_KEY configured")
    
    return True

def test_api_connections():
    """Test API connections"""
    print("\n🌐 Testing API connections...")
    
    load_dotenv()
    
    # Test Gemini AI
    try:
        import google.generativeai as genai
        genai.configure(api_key=os.getenv('GEMINI_API_KEY'))
        model = genai.GenerativeModel('gemini-1.5-flash')
        response = model.generate_content("Hello, this is a test.")
        print("✅ Gemini AI connection successful")
    except Exception as e:
        print(f"❌ Gemini AI connection failed: {e}")
        return False
    
    # Test SERP API (simple check)
    try:
        from serpapi import GoogleSearch
        # Just test if we can create a search object
        search = GoogleSearch({"q": "test", "api_key": os.getenv('SERP_API_KEY')})
        print("✅ SERP API configuration successful")
    except Exception as e:
        print(f"❌ SERP API configuration failed: {e}")
        return False
    
    return True

def test_file_structure():
    """Test if all required files exist"""
    print("\n📁 Testing file structure...")
    
    required_files = [
        'app.py',
        'requirements.txt',
        'templates/index.html',
        '.env'
    ]
    
    for file_path in required_files:
        if os.path.exists(file_path):
            print(f"✅ {file_path}")
        else:
            print(f"❌ {file_path} missing")
            return False
    
    return True

def main():
    """Main test function"""
    print("🧪 AI Travel Planner Setup Test")
    print("=" * 40)
    
    tests = [
        ("File Structure", test_file_structure),
        ("Package Imports", test_imports),
        ("Environment Variables", test_env_variables),
        ("API Connections", test_api_connections)
    ]
    
    passed = 0
    total = len(tests)
    
    for test_name, test_func in tests:
        print(f"\n🔍 Running {test_name} test...")
        try:
            if test_func():
                passed += 1
                print(f"✅ {test_name} test passed")
            else:
                print(f"❌ {test_name} test failed")
        except Exception as e:
            print(f"❌ {test_name} test error: {e}")
    
    print(f"\n📊 Test Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All tests passed! Your setup is ready.")
        print("Run 'python app.py' to start the application.")
    else:
        print("⚠️  Some tests failed. Please check the setup.")
        if passed < 2:
            print("Run 'python setup.py' to fix common issues.")

if __name__ == "__main__":
    main()