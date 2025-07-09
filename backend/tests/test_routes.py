import unittest
from fastapi.testclient import TestClient
from fastapi import FastAPI
from unittest.mock import patch
from app.api.routes import router

app = FastAPI()
app.include_router(router)

class TestRoutes(unittest.TestCase):

    def setUp(self):
        self.client = TestClient(app)

    @patch("app.api.routes.get_investors_summary")
    def test_get_investors_route_success(self, mock_summary):
        mock_summary.return_value = [
            {
                "id": 101,
                "name": "Investor A",
                "type": "Pension Fund",
                "date_added": "2022-01-01",
                "address": "",
                "total_commitment": "3.0M"
            }
        ]

        response = self.client.get("/investors")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()[0]["name"], "Investor A")
        self.assertEqual(response.json()[0]["total_commitment"], "3.0M")

    @patch("app.api.routes.get_investors_summary")
    def test_get_investors_route_empty(self, mock_summary):
        mock_summary.return_value = []

        response = self.client.get("/investors")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), [])

    @patch("app.api.routes.get_commitments_by_investor")
    def test_get_commitments_route_success(self, mock_commitments):
        mock_commitments.return_value = [
            {
                "id": 1,
                "asset_class": "Private Equity",
                "currency": "GBP",
                "amount": "5.0M"
            }
        ]

        response = self.client.get("/investors/Investor%20A/commitments?asset_class=Private%20Equity")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()[0]["asset_class"], "Private Equity")

    @patch("app.api.routes.get_commitments_by_investor")
    def test_get_commitments_route_no_asset_class(self, mock_commitments):
        mock_commitments.return_value = [
            {
                "id": 2,
                "asset_class": "Infrastructure",
                "currency": "GBP",
                "amount": "10.0M"
            }
        ]

        response = self.client.get("/investors/Investor%20A/commitments")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()[0]["asset_class"], "Infrastructure")

    @patch("app.api.routes.get_commitments_by_investor")
    def test_get_commitments_route_empty(self, mock_commitments):
        mock_commitments.return_value = []

        response = self.client.get("/investors/Unknown/commitments")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), [])

    def test_404_not_found(self):
        response = self.client.get("/invalid-route")
        self.assertEqual(response.status_code, 404)

    def test_405_method_not_allowed(self):
        response = self.client.post("/investors")
        self.assertEqual(response.status_code, 405)