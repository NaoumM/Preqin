import pandas as pd
from sqlalchemy.orm import Session
from app.db.models import Commitment
from app.db.session import SessionLocal
from app.db.base import Base
from app.db.session import engine

CSV_FILE = "../../data/data.csv"

def seed():
    Base.metadata.create_all(bind=engine)

    df = pd.read_csv(CSV_FILE)
    db = SessionLocal()

    for _, row in df.iterrows():
        commitment = Commitment(
            investor_name=row["Investor Name"],
            investor_type=row["Investory Type"],
            investor_country=row["Investor Country"],
            investor_date_added=row["Investor Date Added"],
            asset_class=row["Commitment Asset Class"],
            amount=row["Commitment Amount"]
        )
        db.add(commitment)

    db.commit()
    db.close()

if __name__ == "__main__":
    seed()
