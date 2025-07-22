
import os
from dotenv import load_dotenv
load_dotenv()



class Config:
    # Use DATABASE_URL for production, fallback to SQLite for local development
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///api.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv('SECRET_KEY','my_strong_secret')
    BASE_API_URL = os.getenv('API_URL')  
    SECURITY_PASSWORD_SALT = os.getenv("SECURITY_PASSWORD_SALT", "default_salt")
    SECURITY_PASSWORD_HASH = os.getenv("SECURITY_PASSWORD_HASH", "bcrypt")

    SECURITY_REGISTERABLE = True
    SECURITY_SEND_REGISTER_EMAIL = False
    SECURITY_POST_REGISTER_VIEW = '/login'
    SECURITY_POST_CONFIRM_VIEW = '/login'
    SECURITY_POST_LOGOUT_VIEW = '/'
    SECURITY_POST_LOGIN_VIEW = '/user/dashboard'
    SECURITY_AUTO_LOGIN_AFTER_REGISTER = True
    SECURITY_LOGIN_WITHOUT_CONFIRMATION = True
    SECURITY_CONFIRMABLE = False