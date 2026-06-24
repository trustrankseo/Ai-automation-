from sqlalchemy import Column,Integer,String,Text
from database import Base

class Lead(Base):
    __tablename__='leads'

    id = Column(Integer, primary_key=True,index=True)
    business_name = Column(String)
    website = Column(String)
    email = Column(String)
    niche = Column(String)
    score = Column(Integer, default=0)
    notes = Column(Text)
