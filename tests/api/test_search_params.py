import pytest

from api.dto.requests.search_request import SearchRequest
from api.steps.api_base_steps import map_to_cat_image, get_request



@pytest.mark.parametrize("limit", [1, 10])
def test_search_random_images_limit(limit):
    search_request = SearchRequest()
    # resp = requests.get(f"{api_base_url}/images/search?limit={limit}")
    resp = get_request(search_request.search_endpoint, {"limit": limit})

    assert resp.status_code == 200

    data_list = resp.json()
    assert len(data_list) == limit

    for data in data_list:
        cat_image = map_to_cat_image(data)
        # Validation based on DTO
        assert cat_image.id
        assert cat_image.url.startswith("http")
        assert cat_image.width > 0
        assert cat_image.height > 0


@pytest.mark.parametrize("has_breeds", [1, 0])
def test_search_random_images_has_breeds(has_breeds):
    search_request = SearchRequest()
    # resp = requests.get(f"{api_base_url}/images/search?limit={limit}")
    resp = get_request(search_request.search_endpoint, {"has_breeds": has_breeds})

    assert resp.status_code == 200

    data_list = resp.json()

    for data in data_list:
        cat_image = map_to_cat_image(data)
        # Validation based on DTO
        assert cat_image.id
        assert cat_image.url.startswith("http")
        assert cat_image.width > 0
        assert cat_image.height > 0

        #  Breeds validation
        image_id=cat_image.id
        resp = get_request(search_request.search_endpoint_by_id.format(id=image_id))
        assert resp.status_code == 200
        search_cat_by_id = map_to_cat_image(resp.json())
        for breed in search_cat_by_id.breeds:
            if has_breeds==1:
                assert breed.origin
                assert breed.id
                assert breed.name
                assert breed.temperament
            else:
                assert breed is None


