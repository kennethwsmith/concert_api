from fastapi import APIRouter

router = APIRouter(
    tags=["Misc"]
)

@router.get('/')
async def index():
    return {"message":"Home"}

@router.get('/about')
async def about():
    return {"message":"About"}