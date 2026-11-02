from sqlalchemy import create_engine ## Step-2 line (1-7)
from sqlalchemy.orm import sessionmaker
from app.core.config import settings

database_url=settings.DATABASE_URL


engine=create_engine(database_url)


SessionLocal=sessionmaker(bind=engine)





