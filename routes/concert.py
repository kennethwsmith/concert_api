from fastapi import APIRouter

concert_router = APIRouter(
    prefix='/concerts',
    tags=["Concerts"]
)

@concert_router.get('/')
async def index():
    return {"message":"concert info"}

@concert_router.put('/')
async def createConcert():
    return {"message":"createConcert"}