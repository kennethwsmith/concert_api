from fastapi import APIRouter, HTTPException
from sqlalchemy.exc import SQLAlchemyError
from database import Session, Base
from models import Band, BandGenre_enum

router = APIRouter(
    prefix='/bands',
    tags=["Bands"]
)

session = Session()

@router.get('/')
async def index(skip:int = 0, limit:int = 10):
    q = session.query(Band)\
        .limit(limit)\
        .offset(skip)\
        .all()
    return q

@router.post('/')
async def createBand(name:str, genre:BandGenre_enum = "Rock"):
    try:
        new_band = Band(name=name,genre=genre)
        session.add(new_band)
        session.flush()
        session.refresh(new_band)
        new_band_id = new_band.id
        session.commit()
    except SQLAlchemyError as e:
        raise HTTPException(status_code=422, detail=str(e.__dict__))
    except LookupError as e:
        raise HTTPException(status_code=422, detail="Lookup Error!")
    return {"message":"Created Band, ID: " + str(new_band_id)}

@router.get('/{band_id}')
async def getBand(band_id: int):
    q = session.query(Band).filter(Band.id==band_id).one()
    return q

@router.patch('/{band_id}')
async def updateBand(band_id: int, name:str = None, genre:BandGenre_enum = None):
    b = session.query(Band).filter_by(id=band_id).one()
    if(name != None):
        b.name = name
    if(genre != None):
        b.genre = genre
    session.commit()
    return {"message":"Updated Band, ID: " + str(b.id)}

@router.delete('/{band_id}')
async def deleteBand(band_id:int):
    session.query(Band).filter(Band.id==band_id).delete()
    session.commit()
    return {"message":"Deleted Band ID: " + str(band_id)}