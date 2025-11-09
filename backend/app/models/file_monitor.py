from sqlalchemy import Column, Integer, String, DateTime
from app.db.session import Base
from datetime import datetime

class FileMonitor(Base):
    __tablename__ = "file_monitor"

    id = Column(Integer, primary_key=True, index=True)
    file_path = Column(String)
    hash_value = Column(String)
    last_modified = Column(DateTime, default=datetime.utcnow)
