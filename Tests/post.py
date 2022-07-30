import pytest
import requests
import json
def test_posts_positive():
    url = "https://jsonplaceholder.typicode.com/posts"
    data={'id':101,'title':'welcome','body':'hi im sameh','userId':'105'}
    response = requests.post(url,data=data)
    assert response.status_code==201
    response_data = response.json()
    assert response_data==data
def test_posts_negative1():
    url = "https://jsonplaceholder.typicode.com/posts"
    data={'id':101,'title':'welcome','body':'hi im sameh','userId':'105'}
    response = requests.post(url,data=data)
    assert response.status_code==203
    response_data = response.json()
    assert response_data==data

def test_posts_negative2():
        url = "https://jsonplaceholder.typicode.com/posts"
        data = {'id': 151, 'title': 'welcome', 'body': 'hi im sameh', 'userId': '105'}
        response = requests.post(url, data=data)
        assert response.status_code == 201
        response_data = response.json()
        assert response_data == data



