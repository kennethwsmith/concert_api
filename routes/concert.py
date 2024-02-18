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

@router.get('/',description="Get array of concerts")
async def get_all_concerts(skip: int = 0, limit: int = 10):
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

@router.post('/search')
async def search_concert(showdate:str = None,venue_id:int = None,setlist_url:str = None,skip: int = 0, limit: int = 10):
    #FIXME: showdate to DateTime
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
            .group_by(Concert.id, Concert.showdate, Concert.setlist_url, Band.name, Venue.name)
    if(showdate != None):
        q.where(Concert.showdate == showdate)
    if(venue_id != None):
        q.where(Concert.venue_id == venue_id)
    q.limit(limit)
    q.offset(skip)
    return q.all()
        

@router.get('/{concert_id}')
async def get_concert(concert_id: int):
    q = session.query(Concert).filter(Concert.id==concert_id).one()
    return q

@router.patch('/{concert_id}')
async def update_concert(concert_id: int, setlist_url:str = None, showdate:str = None, venue_id:int = None):
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
async def delete_concert(concert_id:int):
    session.query(Concert).filter(Concert.id==concert_id).delete()
    session.commit()
    return {"message":"Deleted Concert ID: " + str(concert_id)}