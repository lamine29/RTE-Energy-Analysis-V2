import os
import requests
from dotenv import load_dotenv

load_dotenv()

CLIENT_ID = os.getenv("RTE_API_CLIENT_ID")
CLIENT_SECRET = os.getenv("RTE_API_CLIENT_SECRET")

class APIConnector:
    def __init__(self, client_id=None, client_secret=None):
        self.client_id = client_id or CLIENT_ID
        self.client_secret = client_secret or CLIENT_SECRET

    def get_access_token(self, token_url="https://digital.iservices.rte-france.com/token/oauth/"):
        data = {"grant_type": "client_credentials"}
        response = requests.post(token_url, data=data, auth=(self.client_id, self.client_secret))
        response.raise_for_status()
        return response.json()["access_token"]

    def get_api_response(self, url, token):
        headers = {"Authorization": f"Bearer {token}"}
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()

# Example usage:
# connector = APIConnector()
# token = connector.get_access_token()
# data = connector.get_api_response("<API_ENDPOINT>", token)
