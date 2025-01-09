import unittest
import requests

class TestCoindeskAPI(unittest.TestCase):
    def test_coindesk_api(self):
        # API endpoint
        url = "https://api.coindesk.com/v1/bpi/currentprice.json"

        # Send GET request
        response = requests.get(url)
        self.assertEqual(response.status_code, 200, f"Failed to fetch API. Status code: {response.status_code}")

        # Parse the response JSON
        data = response.json()
        bpi = data.get("bpi")

        # Verify there are 3 BPIs
        self.assertEqual(len(bpi), 3, f"Expected 3 BPIs, found {len(bpi)}.")

        # Verify USD, GBP, and EUR are present
        for currency in ["USD", "GBP", "EUR"]:
            self.assertIn(currency, bpi, f"{currency} is missing from BPI.")

        # Verify GBP description
        gbp_description = bpi["GBP"].get("description")
        self.assertEqual(gbp_description, "British Pound Sterling", f"Unexpected GBP description: {gbp_description}")

if __name__ == "__main__":
    unittest.main()