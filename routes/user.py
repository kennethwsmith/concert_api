from fastapi import APIRouter, HTTPException
from sqlalchemy.exc import SQLAlchemyError
from database import Session
from models import User

router = APIRouter(
    prefix='/users',
    tags=["Users"]
)

session = Session()

@router.get('/')
async def index():
    q = session.query(User).all()
    return q

@router.get('/active')
async def getUser():
    q = session.query(User).filter(User.is_active==True).all()
    return q

@router.get('/{user_id}')
async def getUser(user_id: int):
    q = session.query(User).filter(User.id==user_id).one()
    return q

@router.post('/')
async def createUser(username:str, email:str, password:str, is_active:bool = True, is_staff:bool = False):
    try:
        new_user = User(username=username,email=email,password=password,is_active=is_active,is_staff=is_staff)
        session.add(new_user)
        session.flush()
        session.refresh(new_user)
        new_user_id = new_user.id
        session.commit()
    except SQLAlchemyError as e:
        raise HTTPException(status_code=422, detail=str(e.__dict__['orig']))
    return {"message":"Created User, ID: " + str(new_user_id)}

@router.delete('/')
async def deleteUser():
    return {"message":"deleteBand"}