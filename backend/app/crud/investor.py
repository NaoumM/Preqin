from collections import defaultdict
from app.db.models import Commitment

def format_amount(value):
    if value >= 1_000_000_000:
        return f"{round(value / 1_000_000_000, 1)}B"
    return f"{round(value / 1_000_000, 1)}M"

def get_investors_summary(db):
    rows = db.query(Commitment).all()
    grouped = defaultdict(list)  # by investor_name
    for row in rows:
        grouped[row.investor_name].append(row)

    result = []
    for idx, (name, entries) in enumerate(grouped.items(), start=1):
        total_commitment = sum(entry.amount for entry in entries)
        result.append({
            "id": idx * 100 + 1,
            "name": name,
            "type": entries[0].investor_type,
            "date_added": entries[0].investor_date_added,
            "address": "",  # kept empty for now
            "total_commitment": format_amount(total_commitment)
        })
    return result

def get_commitments_by_investor(db, name, asset_class):
    query = db.query(Commitment).filter(Commitment.investor_name == name)
    if asset_class:
        query = query.filter(Commitment.asset_class == asset_class)
    rows = query.all()

    return [
        {
            "id": row.id,
            "asset_class": row.asset_class,
            "currency": "GBP",
            "amount": format_amount(row.amount)
        }
        for row in rows
    ]