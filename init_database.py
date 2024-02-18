from database import engine,Base,Session
from models import User, Band, Concert, UserConcert, BandConcert, Address, Venue

def ReloadDatabase(DropAllTables = True, CreateTables = True, TruncateTables = False, CreateData = True):

    session = Session()

    if(DropAllTables):
        Base.metadata.drop_all(bind=engine)
    
    if(CreateTables):
        Base.metadata.create_all(bind=engine)

    if (TruncateTables):
        session.execute("TRUNCATE TABLE band RESTART IDENTITY CASCADE;")
        session.execute("TRUNCATE TABLE app_user RESTART IDENTITY CASCADE;")
        session.execute("TRUNCATE TABLE concert RESTART IDENTITY CASCADE;")

    if (CreateData):
        USERS = [
            {"username":"fasterfester","email":"kennethwsmith@gmail.com","password":"password"},
            {"username":"blah1","email":"blah1@gmail.com","password":"password"},
            {"username":"blah2","email":"blah2@gmail.com","password":"password"},
            {"username":"blah3","email":"blah3@gmail.com","password":"password"},
        ]

        for u in USERS:
            #Create a user
            uData = User(username=u["username"],email=u["email"],password=u["password"])
            session.add(uData)
            session.flush()
            session.refresh(uData)

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

        ADDRESSES = [
            {"street":"123 Main","city":"Houston","state":"TX","zip_code":"77002","country":"USA"},
            {"street":"1000 Draper","city":"Oklahoma City","state":"OK","zip_code":"84556","country":"USA"},
            {"street":"6400 Westheimer","city":"Houston","state":"TX","zip_code":"77052","country":"USA"},
            {"street":"11931 Valencia","city":"Meadows Place","state":"TX","zip_code":"77477","country":"USA"},
        ]

        for a in ADDRESSES:
            aData = Address(street=a["street"],city=a["city"],state=a["state"],zip_code=a["zip_code"],country=a["country"])
            session.add(aData)
            session.flush()
            session.refresh(aData)

        VENUES = [
            {"name":"Verizon Wireless Center","street":"123 Main","city":"Houston","state":"TX","zip_code":"77002","country":"USA"},
            {"name":"Roy Rogers Center","street":"1000 Draper","city":"Oklahoma City","state":"OK","zip_code":"84556","country":"USA"},
            {"name":"Club 6400","street":"6400 Westheimer","city":"Houston","state":"TX","zip_code":"77052","country":"USA"},
            {"name":"The Summit","street":"11931 Valencia","city":"Meadows Place","state":"TX","zip_code":"77477","country":"USA"}
        ]
        
        for v in VENUES:
            vData = Venue(name=v["name"],street=v["street"],city=v["city"],state=v["state"],zip_code=v["zip_code"],country=v["country"])
            session.add(vData)
            session.flush()
            session.refresh(vData)

        CONCERTS = [
            {"showdate":"1/1/2000",
            "setlist_url":"http://www.google.com",
            "venue_id":1,
            "band_id":"1",
            "user_id":"1"
            },
            {"showdate":"2/2/1999",
            "setlist_url":"http://www.google.com",
            "venue_id":2,
            "band_id":"2",
            "user_id":"2"
            },
            {"showdate":"3/3/1994",
            "setlist_url":"http://www.google.com",
            "venue_id":3,
            "band_id":"2",
            "user_id":"3"
            },
            {"showdate":"2/3/1999",
            "setlist_url":"http://www.google.com",
            "venue_id":4,
            "band_id":"2",
            "user_id":"1"
            },
            {"showdate":"3/4/1994",
            "setlist_url":"http://www.google.com",
            "venue_id":1,
            "band_id":"2",
            "user_id":"2"
            },
            {"showdate":"2/5/1999",
            "setlist_url":"http://www.google.com",
            "venue_id":2,
            "band_id":"2",
            "user_id":"1"
            },
            {"showdate":"3/6/1994",
            "setlist_url":"http://www.google.com",
            "venue_id":3,
            "band_id":"2",
            "user_id":"3"
            },
            {"showdate":"4/5/1992",
            "setlist_url":"http://www.google.com",
            "venue_id":4,
            "band_id":"3",
            "user_id":"1"
            },
            {"showdate":"5/6/1995",
            "setlist_url":"http://www.google.com",
            "venue_id":1,
            "band_id":"3",
            "user_id":"1"
            },
            {"showdate":"5/6/1995",
            "setlist_url":"http://www.google.com",
            "venue_id":1,
            "band_id":"3",
            "user_id":"2"
            },
            {"showdate":"5/6/1995",
            "setlist_url":"http://www.google.com",
            "venue_id":1,
            "band_id":"3",
            "user_id":"3"
            },
            {"showdate":"5/6/1995",
            "setlist_url":"http://www.google.com",
            "venue_id":1,
            "band_id":"3",
            "user_id":"4"
            }
        ]

        for c in CONCERTS:
            cData = Concert(showdate=c["showdate"],setlist_url=c["setlist_url"],venue_id=c["venue_id"])
            session.add(cData)
            session.flush()
            session.refresh(cData)

            ucxData = UserConcert(user_id=c["user_id"],concert_id=cData.id)
            session.add(ucxData)
            bcxData = BandConcert(band_id=c["band_id"],concert_id=cData.id)
            session.add(bcxData)

    session.commit()