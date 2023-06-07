#! /usr/bin/env python3

import os
import requests
import json

text_files = os.listdir(os.getcwd()+"/supplier-data/descriptions/")

dict = {"name": "name",
        "weight": 0,
        "description": "description",
        "image_name": "image"}

for file in text_files:
    with open('supplier-data/descriptions/'+file, 'rb') as opened:
        
        dict["name"] = opened.readline().decode("utf-8")
        dict["weight"] = int(opened.readline().decode("utf-8")[:-4])
        dict["description"] = opened.readline().decode("utf-8")
        dict["image_name"] = file[:-3]+"jpeg"

        """ Post the data to the REST url """
        response = requests.post("http://34.172.207.212/fruits/", json=dict)
        response.raise_for_status()