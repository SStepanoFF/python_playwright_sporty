import pytest

from api.dto.requests.search_request import SearchRequest
from api.steps.api_base_steps import map_to_cat_image, get_request


def test_get_image_by_id():
    search_request = SearchRequest()
    #getting existed image_id
    resp = get_request(search_request.search_endpoint)
    data_list = resp.json()
    image_id=""
    for data in data_list:
        search_cat = map_to_cat_image(data)
        image_id=search_cat.id

    resp = get_request(search_request.search_endpoint_by_id.format(id=image_id))
    assert resp.status_code == 200

    search_cat_by_id = map_to_cat_image(resp.json())
    assert search_cat_by_id.id == image_id
    assert search_cat_by_id.url.startswith("http")
    assert search_cat_by_id.width > 0
    assert search_cat_by_id.height > 0

    # Optional breeds validation
    for breed in search_cat_by_id.breeds:
        assert breed.id
        assert breed.name
        assert breed.temperament
        assert breed.origin


@pytest.mark.parametrize("id", ["wrong"])
def test_get_image_by_wrong_id(id):
    search_request = SearchRequest()
    resp = get_request(search_request.search_endpoint_by_id.format(id=id))
    assert resp.status_code == 400
    assert resp.text == f"Couldn't find an image matching the passed 'id' of {id}"

