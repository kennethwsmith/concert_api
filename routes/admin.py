from fastapi import APIRouter
from database import Session
from models import User, Band, Concert, BandConcert, UserConcert, Venue, Address
from sqlalchemy import Integer, func
from sqlalchemy.dialects.postgresql import ARRAY
from fastapi.responses import HTMLResponse

session = Session()

router = APIRouter(
    prefix='/admin',
    tags=["Admin"]
)

@router.get('/', response_class=HTMLResponse)
async def index():
    return """
    <html>
        <head>
            <title>Admin</title>
        </head>
        <body>
            <h1>Admin</h1>
        </body>
    </html>
    """

@router.get('/full_load')
async def index(skip: int = 0, limit: int = 10):
    concerts_agg = func.array_agg(
        func.json_build_object(
                "showdate",Concert.showdate,"venue",Venue.name,"street",Venue.street,"city",Venue.city,"state",Venue.state,"zip_code",Venue.zip_code,"country",Venue.country
            )
        ).label('concerts'
    )
    q = session.query(Band.name, Band.genre, concerts_agg)\
            .filter(BandConcert.concert_id == Concert.id)\
            .filter(Concert.venue_id == Venue.id)\
            .filter(BandConcert.band_id == Band.id)\
            .group_by(Band.name, Band.genre)\
            .limit(limit)\
            .offset(skip)\
        .all()
    return q

