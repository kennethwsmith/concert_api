from fastapi import APIRouter
from database import Session, Base
from models import Band

band_router = APIRouter(
    prefix='/bands',
    tags=["Bands"]
)

session = Session()

@band_router.get('/')
async def index():
    q = session.query(Band).all()
    return q

@band_router.get('/{band_id}')
async def getBand(band_id: int):
    q = session.query(Band).filter(Band.id==band_id).all()
    return q

@band_router.put('/')
async def createBand():
    return {"message":"createBand"}