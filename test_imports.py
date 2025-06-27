#!/usr/bin/env python3
"""
Test all imports used in app.py
"""

print("Testing imports...")

try:
    from flask import Flask, render_template, request, jsonify, session
    print("✅ Flask imports successful")
except ImportError as e:
    print(f"❌ Flask import failed: {e}")

try:
    from datetime import datetime, timedelta
    print("✅ datetime imports successful")
except ImportError as e:
    print(f"❌ datetime import failed: {e}")

try:
    import os
    print("✅ os import successful")
except ImportError as e:
    print(f"❌ os import failed: {e}")

try:
    import json
    print("✅ json import successful")
except ImportError as e:
    print(f"❌ json import failed: {e}")

try:
    import google.generativeai as genai
    print("✅ google.generativeai import successful")
except ImportError as e:
    print(f"❌ google.generativeai import failed: {e}")

try:
    from serpapi import GoogleSearch
    print("✅ serpapi import successful")
except ImportError as e:
    print(f"❌ serpapi import failed: {e}")

try:
    import requests
    print("✅ requests import successful")
except ImportError as e:
    print(f"❌ requests import failed: {e}")

try:
    from werkzeug.security import generate_password_hash
    print("✅ werkzeug import successful")
except ImportError as e:
    print(f"❌ werkzeug import failed: {e}")

try:
    import uuid
    print("✅ uuid import successful")
except ImportError as e:
    print(f"❌ uuid import failed: {e}")

try:
    from dotenv import load_dotenv
    print("✅ dotenv import successful")
except ImportError as e:
    print(f"❌ dotenv import failed: {e}")

print("\nAll imports tested!")