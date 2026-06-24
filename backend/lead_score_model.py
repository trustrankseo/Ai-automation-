from sqlalchemy import Column,Integer,String
from database import Base

class LeadScore(Base):
    __tablename__='lead_scores'
    id=Column(Integer,primary_key=True,index=True)
    business_name=Column(String)
    score=Column(Integer,default=0)
