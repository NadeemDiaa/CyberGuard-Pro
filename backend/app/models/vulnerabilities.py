from sqlalchemy import Column, Integer, String, ForeignKey
from app.db.session import Base

class Vulnerability(Base):
    __tablename__ = "vulnerabilities"

    id = Column(Integer, primary_key=True, index=True)
    host_id = Column(Integer, ForeignKey("hosts.id"))
    description = Column(String)
    severity = Column(String)
