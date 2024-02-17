from fastapi import FastAPI

from routes.auth import router as auth_router
from routes.concert import router as concert_router
from routes.band import router as band_router
from routes.admin import router as admin_router
from routes.misc import router as misc_router
from routes.user import router as user_router

app = FastAPI(
    title="Concert DB Backend Rest API",
    description="Description of Concert DB Backend",
    version="0.0.2",
    summary="this is a summary",
    terms_of_service="http://example.com/terms/",
    contact={
        "name": "Ken Smith",
        "url": "http://ksmith.example.com/contact/",
        "email": "kennethwsmith@gmail.com",
    },
    license_info={
        "name": "Apache 2.0",
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
    },
    )

app.include_router(concert_router)
app.include_router(band_router)
app.include_router(admin_router)
app.include_router(misc_router)
app.include_router(auth_router)
app.include_router(user_router)