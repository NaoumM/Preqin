from pydantic import BaseModel

class InvestorOut(BaseModel):
    id: int
    name: str
    type: str
    date_added: str
    address: str
    total_commitment: str

    class Config:
        orm_mode = True

class CommitmentOut(BaseModel):
    id: int
    asset_class: str
    currency: str
    amount: str

    class Config:
        orm_mode = True
