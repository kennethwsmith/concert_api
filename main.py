from fastapi import FastAPI

from routes.auth import auth_router
from routes.concert import concert_router
from routes.band import band_router
from routes.admin import admin_router
from routes.misc import misc_router

# Security Configurations
SECRET_KEY = "your-secret-key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

app = FastAPI(
    title="Concert DB Backend Rest API",
    description="Concert DB Backend - Ken Smith",
    version="0.0.1"
    )

app.include_router(concert_router)
app.include_router(band_router)
app.include_router(admin_router)
app.include_router(misc_router)
app.include_router(auth_router)