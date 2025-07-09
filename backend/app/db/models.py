from sqlalchemy import Column, Integer, String, Float
from app.db.base import Base

class Commitment(Base):
    __tablename__ = "commitments"

    id = Column(Integer, primary_key=True, index=True)
    investor_name = Column(String, index=True)
    investor_type = Column(String)
    investor_country = Column(String)
    investor_date_added = Column(String)
    asset_class = Column(String)
    amount = Column(Float)
