import unittest
from unittest.mock import MagicMock
from app.crud import investor
from app.db.models import Commitment
from datetime import date

class TestInvestorCrud(unittest.TestCase):

    def test_format_amount_millions(self):
        self.assertEqual(investor.format_amount(1_200_000), "1.2M")
        self.assertEqual(investor.format_amount(9_999_999), "10.0M")

    def test_format_amount_billions(self):
        self.assertEqual(investor.format_amount(2_000_000_000), "2.0B")
        self.assertEqual(investor.format_amount(3_450_000_000), "3.5B")

    def test_get_investors_summary(self):
        mock_db = MagicMock()
        mock_commitments = [
            Commitment(
                investor_name="Investor A",
                investor_type="Pension Fund",
                investor_date_added=date(2022, 1, 1),
                amount=1_000_000
            ),
            Commitment(
                investor_name="Investor A",
                investor_type="Pension Fund",
                investor_date_added=date(2022, 1, 1),
                amount=2_000_000
            ),
            Commitment(
                investor_name="Investor B",
                investor_type="Sovereign Wealth Fund",
                investor_date_added=date(2023, 5, 10),
                amount=3_000_000_000
            ),
        ]
        mock_db.query().all.return_value = mock_commitments

        result = investor.get_investors_summary(mock_db)

        self.assertEqual(len(result), 2)
        self.assertEqual(result[0]["name"], "Investor A")
        self.assertEqual(result[0]["total_commitment"], "3.0M")
        self.assertEqual(result[1]["name"], "Investor B")
        self.assertEqual(result[1]["total_commitment"], "3.0B")

    def test_get_commitments_with_asset_class(self):
        mock_db = MagicMock()
        mock_commitment = Commitment(
            id=1,
            investor_name="Investor A",
            asset_class="Private Equity",
            amount=5_000_000
        )
        mock_db.query().filter().filter().all.return_value = [mock_commitment]

        result = investor.get_commitments_by_investor(mock_db, "Investor A", "Private Equity")

        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]["asset_class"], "Private Equity")
        self.assertEqual(result[0]["amount"], "5.0M")
        self.assertEqual(result[0]["currency"], "GBP")

    def test_get_commitments_without_asset_class(self):
        mock_db = MagicMock()
        mock_commitments = [
            Commitment(
                id=1,
                investor_name="Investor A",
                asset_class="Private Equity",
                amount=5_000_000
            ),
            Commitment(
                id=2,
                investor_name="Investor A",
                asset_class="Infrastructure",
                amount=10_000_000
            ),
        ]
        mock_db.query().filter().all.return_value = mock_commitments

        result = investor.get_commitments_by_investor(mock_db, "Investor A", None)

        self.assertEqual(len(result), 2)
        self.assertEqual(result[0]["asset_class"], "Private Equity")
        self.assertEqual(result[0]["amount"], "5.0M")
        self.assertEqual(result[1]["asset_class"], "Infrastructure")
        self.assertEqual(result[1]["amount"], "10.0M")