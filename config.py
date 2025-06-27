"""
Configuration settings for AI Travel Planner
"""

import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    """Base configuration"""
    SECRET_KEY = os.getenv('FLASK_SECRET_KEY', 'dev-secret-key-change-in-production')
    GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')
    SERP_API_KEY = os.getenv('SERP_API_KEY')
    
    # Database configuration
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///trippy.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # Budget allocation percentages
    FLIGHT_BUDGET_PERCENTAGE = 0.40  # 40% for flights
    HOTEL_BUDGET_PERCENTAGE = 0.35   # 35% for hotels
    ACTIVITY_BUDGET_PERCENTAGE = 0.25 # 25% for activities
    
    # Search limits
    MAX_FLIGHTS_RESULTS = 5
    MAX_HOTELS_RESULTS = 8
    
    # AI Model settings
    GEMINI_MODEL = 'gemini-1.5-flash'
    MAX_CHAT_HISTORY = 10
    
    # API timeouts (seconds)
    SERP_TIMEOUT = 30
    GEMINI_TIMEOUT = 30
    
    # Default interests
    DEFAULT_INTERESTS = [
        'adventure', 'culture', 'food', 'nature', 'history',
        'nightlife', 'shopping', 'relaxation', 'photography', 'sports'
    ]

class DevelopmentConfig(Config):
    """Development configuration"""
    DEBUG = True
    TESTING = False

class ProductionConfig(Config):
    """Production configuration"""
    DEBUG = False
    TESTING = False

class TestingConfig(Config):
    """Testing configuration"""
    DEBUG = True
    TESTING = True

# Configuration dictionary
config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig
}