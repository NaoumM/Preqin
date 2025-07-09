from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.crud.investor import get_investors_summary, get_commitments_by_investor
from app.schemas.investor import InvestorOut, CommitmentOut

router = APIRouter()

@router.get("/investors", response_model=list[InvestorOut])
def get_investors(db = Depends(get_db)):
    return get_investors_summary(db)

@router.get("/investors/{investor_name}/commitments", response_model=list[CommitmentOut])
def get_commitments(investor_name, asset_class = Query(None), db = Depends(get_db)):
    return get_commitments_by_investor(db, investor_name, asset_class)
