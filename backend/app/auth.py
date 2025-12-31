from passlib.context import CryptContext
from jose import jwt, JWTError
from fastapi.security import OAuth2PasswordBearer
import time
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Password hashing setup
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    # bcrypt supports max 72 characters, so truncate if longer
    return pwd_context.hash(password[:72])

def verify_password(plain: str, hashed: str) -> bool:
    return pwd_context.verify(plain[:72], hashed)

# JWT setup
SECRET_KEY = os.getenv("SECRET_KEY", "supersecretvalue123")  # fallback if .env missing
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60

def create_access_token(email: str, role: str) -> str:
    now = int(time.time())
    payload = {
        "sub": email,
        "role": role,
        "iat": now,
        "exp": now + ACCESS_TOKEN_EXPIRE_MINUTES * 60,
    }
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)

def decode_access_token(token: str):
    try:
        return jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    except JWTError:
        return None

# OAuth2 scheme for extracting Bearer tokens
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="api/v1/login")