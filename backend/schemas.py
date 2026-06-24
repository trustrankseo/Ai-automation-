from pydantic import BaseModel

class LeadCreate(BaseModel):
    business_name:str
    website:str | None = None
    email:str | None = None
    niche:str | None = None

class LeadResponse(LeadCreate):
    id:int
    score:int

    class Config:
        from_attributes=True
