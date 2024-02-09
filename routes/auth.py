from fastapi import APIRouter

auth_router = APIRouter(
    prefix='/auth',
    tags=["Authentication"]
)

@auth_router.get('/')
async def index():
    return {"message":"auth"}

@auth_router.post('/session')
async def login():
    return {"message":"login"}

@auth_router.delete('/session')
async def logout():
    return {"message":"logout"}

@auth_router.get('/session')
async def state():
    return {"message":"session state: unknown"}
