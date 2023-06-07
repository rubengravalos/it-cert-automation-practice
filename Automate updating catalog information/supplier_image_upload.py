#!/usr/bin/env python3

import requests
import os

# This example shows how a file can be uploaded using
# The Python Requests module

url = "http://localhost/upload/"

images = os.listdir(os.getcwd()+"/supplier-data/images/")

for image in images:
    if ".jpeg" in image:
        with open('supplier-data/images/'+image, 'rb') as opened:
            r = requests.post(url, files={'file': opened})