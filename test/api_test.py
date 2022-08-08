import requests
from requests.exceptions import HTTPError

def test_get_locations():
    url = "http://ab104ff421a794c6186fc066153ee785-520651207.us-west-1.elb.amazonaws.com:5000"
    response = requests.get(url)
    assert response.status_code == 200

    print (response)
