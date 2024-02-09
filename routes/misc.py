from fastapi import APIRouter

misc_router = APIRouter(
    tags=["Misc"]
)

@misc_router.get('/')
async def index():
    return {"message":"Home"}

@misc_router.get('/about')
async def about():
    return {"message":"About"}