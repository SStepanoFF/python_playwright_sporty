import configparser

from api.dto.responses.breed_dto import BreedDto
from api.dto.responses.cat_dto import CatImage
from api.utils.api_client import ApiClient

API_KEY = "DEMO_API_KEY"
HEADERS = {"x-api-key": API_KEY}
API_CLIENT = None


def api_client():
    global API_CLIENT
    config = configparser.ConfigParser()
    config.read('pytest.ini')
    base_url = config["pytest"]["api_base_url"]
    if API_CLIENT is None:
        API_CLIENT = ApiClient(
            base_url=base_url,
            headers=HEADERS,
            log=True
        )
    return API_CLIENT

def get_request(endpoint, params=None):
    response = api_client().request("get", endpoint, params=params)
    return response


def map_to_cat_image(data: dict) -> CatImage:
    return CatImage.from_json(data)
