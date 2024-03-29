import jsonschema
import requests
from requests import Response
from utils.utils import load_schema


def test_get_single_user(url_api):
    url = f"{url_api}/users/2"
    schema = load_schema("get_single_user.json")

    result: Response = requests.get(url)

    assert result.status_code == 200
    jsonschema.validate(result.json(), schema)


def test_post_create(url_api):
    url = f"{url_api}/users"
    schema = load_schema("post_create.json")

    result = requests.post(
        url,
        {
            "name": "morpheus",
            "job": "leader"
        }
    )

    assert result.status_code == 201
    jsonschema.validate(result.json(), schema)
    assert result.json()['name'] == 'morpheus'
    assert result.json()['job'] == 'leader'


def test_post_login_successful(url_api):
    url = f"{url_api}/login"
    schema = load_schema("post_login_successful.json")

    result = requests.post(
        url,
        {
            "email": "eve.holt@reqres.in",
            "password": "cityslicka"
        }
    )

    jsonschema.validate(result.json(), schema)
    assert result.status_code == 200
    assert result.json()['token'] == 'QpwL5tke4Pnpja7X4'


def test_put_update(url_api):
    url = f"{url_api}/users/2"
    schema = load_schema("put_update.json")

    result = requests.put(
        url,
        {
            "name": "morpheus",
            "job": "zion resident"
        }
    )

    assert result.status_code == 200
    jsonschema.validate(result.json(), schema)
    assert result.json()['name'] == 'morpheus'
    assert result.json()['job'] == 'zion resident'


def test_delete(url_api):
    url = f"{url_api}/users/2"

    result = requests.delete(url)

    assert result.status_code == 204
    assert result.text == ""


def test_get_single_user_not_found(url_api):
    url = f"{url_api}/users/23"

    result = requests.get(url)

    assert result.status_code == 404
    assert result.text == '{}'


def test_post_register_unsuccessful(url_api):
    url = f"{url_api}/register"
    schema = load_schema("post_register_unsuccessful.json")

    result = requests.post(
        url,
        {
            "email": "sydney@fife"
        }
    )

    assert result.status_code == 400
    jsonschema.validate(result.json(), schema)
    assert result.json()['error'] == 'Missing password'


def test_get_list_users(url_api):
    url = f"{url_api}/users?page=1"
    schema = load_schema("get_list_users.json")

    result: Response = requests.get(url)

    assert result.status_code == 200
    jsonschema.validate(result.json(), schema)
    assert result.json()['total_pages'] == 2


def test_patch_update(url_api):
    url = f"{url_api}/users/2"
    schema = load_schema("patch_update.json")

    result = requests.patch(
        url,
        {
            "name": "morpheus",
            "job": "zion resident"
        }
    )

    assert result.status_code == 200
    jsonschema.validate(result.json(), schema)
    assert result.json()['name'] == 'morpheus'
    assert result.json()['job'] == 'zion resident'
