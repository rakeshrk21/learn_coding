import pytest
import requests
import json
import logging as logger

from videogamerequest import VideoGameRequest

# Configure logging
logger.basicConfig(level=logger.DEBUG)


def test_something():
        print("my life")

    
def test_get_videogames():

        url = 'https://videogamedb.uk/api/v2/videogame'
        headers = {'accept': 'application/json'}
        response = requests.get(url=url, headers=headers)
        print(response.status_code)
        logger.info(f"Status code is {response.status_code}")

        if response.status_code == 200:

            json_response = response.json()
            print(isinstance(json_response, list))
            if isinstance(json_response, list):
                for item in json_response:
                    logger.info(f"item is {item}")
                    print(item)
        
        else: 
            logger.debug(f"failed: {response.status_code}")
            print("failed!")


def test_post_create_videogame():
    url = 'https://videogamedb.uk/api/v2/videogame'
    request = VideoGameRequest.Builder().category("test").name("james").rating("Universal").releaseDate("2015-10-01 23:59:59").reviewScore(99).build()
    json_body = json.dumps(request.to_dict()) #python object to a string object
    print(f"request: {json_body}")
    headers = {'accept': 'application/json', 'Content-Type':'application/json'}
    response = requests.post(url=url, headers=headers, data=json_body)
    # Print the response
    print(f"Status Code: {response.status_code}")
    print(f"Response Body: {response.json()}")
    assert response.status_code == 200
    data = json.loads(response.text) # deserialization
    print(type(data))
    print(data['name'])
    assert data['name'] == 'james'
    