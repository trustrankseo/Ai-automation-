from sqlalchemy import Column,Integer,String,Text
from database import Base

class OutreachMessage(Base):
    __tablename__='outreach_messages'
    id=Column(Integer,primary_key=True,index=True)
    channel=Column(String)
    subject=Column(String)
    content=Column(Text)
