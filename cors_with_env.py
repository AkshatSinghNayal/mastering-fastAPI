from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import os

app = FastAPI()

load_dotenv

SECRET_KEY = os.getenv("SECRET_KEY")
ORIGINS = os.getenv("ORIGINS")