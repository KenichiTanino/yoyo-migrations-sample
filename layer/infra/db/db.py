import sqlalchemy

from app.settings.settings import Settings
settings = Settings()

engine = sqlalchemy.create_engine(settings.DATABASE_URI, echo=False)
