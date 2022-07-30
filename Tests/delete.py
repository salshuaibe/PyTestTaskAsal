import pytest
import requests
import json

def test_posts_positive():
    url = "https://jsonplaceholder.typicode.com/posts/1"

    response = requests.delete(url)
    assert response.status_code==200
def test_posts_negative1():
    url = "https://jsonplaceholder.typicode.com/posts/1"
    response = requests.delete(url)

    assert response.status_code==203



