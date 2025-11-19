import requests
import json

class ApiClient:
    def __init__(self, base_url, headers=None, log=True):
        self.base_url = base_url
        self.headers = headers or {}
        self.log = log

    def _log_request(self, method, url, **kwargs):
        if not self.log:
            return
        print("\n===== REQUEST =====")
        print(f"METHOD: {method}")
        print(f"URL: {url}")
        if "headers" in kwargs:
            print("HEADERS:", json.dumps(kwargs["headers"], indent=2))
        if "params" in kwargs:
            print("PARAMS:", json.dumps(kwargs["params"], indent=2))
        if "data" in kwargs:
            print("DATA:", kwargs["data"])
        if "json" in kwargs:
            print("JSON:", json.dumps(kwargs["json"], indent=2))

    def _log_response(self, response):
        if not self.log:
            return
        print("\n===== RESPONSE =====")
        print(f"STATUS: {response.status_code}")
        try:
            print("BODY:", json.dumps(response.json(), indent=2))
        except ValueError:
            print("BODY:", response.text)

    def request(self, method, endpoint, **kwargs):
        url = f"{self.base_url}{endpoint}"

        self._log_request(method, url, **kwargs)

        response = requests.request(method, url, **kwargs)

        self._log_response(response)

        return response