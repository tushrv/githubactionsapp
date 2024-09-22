import os
import sys

root = os.path.dirname(os.path.dirname(__file__))
sys.path.append(root)

from app import app

def test_home():
    response=app.test_client().get("/")

    assert response.status_code==200
    assert response.data== b"Hello World!"