from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URI = "postgresql://postgres:12345@localhost:5432/QA"
engine = create_engine(DATABASE_URI)
Session = sessionmaker(bind=engine)


def get_db_connection():
    session = Session()
    return session
