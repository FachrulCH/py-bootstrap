from berapi.apy import berAPI


def test_chaining():
    (berAPI()
     .get('https://swapi.dev/api/people/1')
     .assert_2xx()
     .assert_value('name', 'Luke Skywalker')
     .assert_response_time_less_than(seconds=3)
     )