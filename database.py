from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

#FIXME: Secure this
engine=create_engine('postgresql://kensmith:banana@localhost/concerts',
    echo=True
    )

Base = declarative_base()

Session = sessionmaker(bind=engine)