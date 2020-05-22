# A very simple Flask Hello World app for you to get started with...

from __future__ import print_function
from flask import Flask
import requests
import json
import cv2

app = Flask(__name__)

@app.route('/')
def hello_world():
    addr = 'http://LINK_SERVER/'
    test_url = addr + '/api/test'

    # prepare headers for http request
    content_type = 'image/jpeg'
    headers = {'content-type': content_type}

    img = cv2.imread('slideshow.jpg')
    # encode image as jpeg
    _, img_encoded = cv2.imencode('.jpg', img)
    # send http request with image and receive response
    response = requests.post(test_url, data=img_encoded.tostring(), headers=headers)
    # decode response
    return json.loads(response.text)