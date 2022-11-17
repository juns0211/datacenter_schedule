from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.engine import URL

class Database:
    def __init__(self, DB_SETTING):
        # 讀取設定檔
        database_url = URL.create(**DB_SETTING)
        self.engine = create_engine(
            database_url,
            pool_size=5,
            max_overflow=0,
            pool_pre_ping=True,
            pool_reset_on_return=False
        )
        self.Session = sessionmaker(bind=self.engine)