import os

from assertpy import assert_that
from berapi.apy import berAPI

from helper.file_utility import API_SCHEMA, PROJECT_ROOT


def test_list_of_users():
    (berAPI()
     .get('https://gorest.co.in/public/v1/users')
     .assert_2xx()
     .assert_response_time_less_than(seconds=3)
     .assert_schema(API_SCHEMA + '/get_users.json')
     )


def test_search_users_with_pagination():
    header = {'Authorization': os.getenv('API_TOKEN', 'ABC')}
    response = (berAPI()
                .get('https://gorest.co.in/public/v1/users?page=2&per_page=6&name=Khan', headers=header)
                .assert_2xx()
                .assert_response_time_less_than(seconds=3)
                .assert_schema(PROJECT_ROOT+'/tests/api/schema/get_users.json')
                .parse_json()
                )
    assert_that(response['meta']['pagination']['page']).is_equal_to(2)
    assert_that(response['data']).is_length(6)
    assert_that(response['data'][0]['name']).contains('Khan')
