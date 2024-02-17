from fastapi import APIRouter, HTTPException
from sqlalchemy.exc import SQLAlchemyError
from database import Session
from models import Concert, Band, BandConcert, Venue, UserConcert
from sqlalchemy import func

router = APIRouter(
    prefix='/concerts',
    tags=["Concerts"]
)

session = Session()

@router.get('/')
async def index(skip: int = 0, limit: int = 10):
    attendees_agg = func.array_agg(
                UserConcert.user_id
        ).label('attendee_user_ids'
    )
    q = session.query(Concert.id, Concert.showdate, Concert.setlist_url,
                Band.name.label("band_name"),
                Venue.name.label("venue_name"),
                attendees_agg)\
            .filter(Concert.venue_id == Venue.id)\
            .filter(BandConcert.concert_id == Concert.id)\
            .filter(BandConcert.band_id == Band.id)\
            .filter(UserConcert.concert_id == Concert.id)\
            .group_by(Concert.id, Concert.showdate, Concert.setlist_url, Band.name, Venue.name)\
            .limit(limit)\
            .offset(skip)\
        .all()
    return q

@router.post('/')
async def createConcert(showdate:str,venue_id:int,setlist_url:str = None):
    #FIXME: showdate to DateTime
    try:
        new_concert = Concert(showdate=showdate,venue_id=venue_id,setlist_url=setlist_url)
        session.add(new_concert)
        session.flush()
        session.refresh(new_concert)
        new_concert_id = new_concert.id
        session.commit()
    except SQLAlchemyError as e:
        raise HTTPException(status_code=422, detail=str(e.__dict__))
    except LookupError as e:
        raise HTTPException(status_code=422, detail="Lookup Error!")
    return {"message":"Created Concert, ID: " + str(new_concert_id)}

@router.get('/{concert_id}')
async def getConcert(concert_id: int):
    q = session.query(Concert).filter(Concert.id==concert_id).one()
    return q

@router.patch('/{concert_id}')
async def updateConcert(concert_id: int, setlist_url:str = None, showdate:str = None, venue_id:int = None):
    c = session.query(Concert).filter_by(id=concert_id).one()
    if(showdate != None):
        c.showdate = showdate
    if(venue_id != None):
        c.venue_id = venue_id
    if(setlist_url != None):
        c.setlist_url = setlist_url
    session.commit()
    return {"message":"Updated Concert, ID: " + str(c.id)}

@router.delete('/{concert_id}')
async def deleteConcert(concert_id:int):
    session.query(Concert).filter(Concert.id==concert_id).delete()
    session.commit()
    return {"message":"Deleted Concert ID: " + str(concert_id)}