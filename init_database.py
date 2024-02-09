from database import engine,Base,Session
from models import User, Band, Concert, UserConcert, BandConcert, Address
from enums import BAND_GENRES

CREATE_DATA = True

Base.metadata.create_all(bind=engine)

session = Session()

session.execute("TRUNCATE TABLE band RESTART IDENTITY CASCADE;")
session.execute("TRUNCATE TABLE app_user RESTART IDENTITY CASCADE;")
session.execute("TRUNCATE TABLE concert RESTART IDENTITY CASCADE;")

#Create a user
uData = User(username="fasterfester",email="kennethwsmith@gmail.com",password="password")
session.add(uData)
session.flush()
session.refresh(uData)
user_id = uData.id

if CREATE_DATA:

    BANDS = [
        {"name":"Foo Fighters","genre":"ROCK"},
        {"name":"Tool","genre":"ROCK"},
        {"name":"Nirvana","genre":"ROCK"},
        {"name":"Taylor Swift","genre":"POP"},
        ]

    for b in BANDS:
        bData = Band(name=b["name"],genre=b["genre"])
        session.add(bData)
        session.flush()
        session.refresh(bData)
        print(bData.id)

    CONCERTS = [
        {"showdate":"1/1/2000",
        "setlist_url":"http://www.google.com",
        "venue":"The Summit",
        "band_id":"1",
        "user_id":"1"
        },
        {"showdate":"2/2/1999",
        "setlist_url":"http://www.google.com",
        "venue":"Cynthia Woods",
        "band_id":"2",
        "user_id":"1"
        },
        {"showdate":"3/3/1994",
        "setlist_url":"http://www.google.com",
        "venue":"Verizon Wireless Center",
        "band_id":"2",
        "user_id":"1"
        },
    ]

    for c in CONCERTS:
        cData = Concert(showdate=c["showdate"],setlist_url=c["setlist_url"],venue=c["venue"])
        session.add(cData)
        session.flush()
        session.refresh(cData)

        ucxData = UserConcert(user_id=c["user_id"],concert_id=cData.id)
        session.add(ucxData)
        bcxData = BandConcert(band_id=c["band_id"],concert_id=cData.id)
        session.add(bcxData)

        print("*********************")
        print(cData)

session.commit()