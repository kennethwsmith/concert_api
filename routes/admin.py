from fastapi import APIRouter
from database import Session, Base
from models import User, Band, Concert

session = Session()

admin_router = APIRouter(
    prefix='/admin',
    tags=["Admin"]
)

@admin_router.get('/')
async def index():
    return {"message":"Admin"}

@admin_router.get('/full_load')
async def index():
    q = session.query(Band).join(Concert)

    # return join_query.filter(User.email == email).all()
    return q