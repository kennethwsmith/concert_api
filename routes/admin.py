from fastapi import APIRouter
from database import Session, Base
from models import User, Band, Concert, BandConcert, UserConcert
from sqlalchemy import Integer, func
from sqlalchemy.dialects.postgresql import ARRAY
from fastapi.responses import HTMLResponse

session = Session()

admin_router = APIRouter(
    prefix='/admin',
    tags=["Admin"]
)

@admin_router.get('/', response_class=HTMLResponse)
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

@admin_router.get('/full_load')
async def index():
    concerts_agg = func.array_agg(func.json_build_object("showdate",Concert.showdate,"venue",Concert.venue,"State","TX")).label('concerts')
    q = session.query(Band.name, concerts_agg)\
            .filter(BandConcert.concert_id == Concert.id)\
            .filter(BandConcert.band_id == Band.id)\
            .group_by(Band.name)\
        .all()
    return q

# @admin_router.get('/full_load')
# async def index():
#     concerts_agg = func.array_agg(func.json_build_object("showdate",Concert.showdate,"venue",Concert.venue,"State","TX")).label('concerts')
#     q = session.query(Band.name, concerts_agg)\
#             .filter(BandConcert.concert_id == Concert.id)\
#             .filter(BandConcert.band_id == Band.id)\
#             .group_by(Band.name)\
#         .all()
#     return q