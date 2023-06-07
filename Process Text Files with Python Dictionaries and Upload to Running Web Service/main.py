#! /usr/bin/env python3

import os
import requests

""" Directory where the feedback files ".txt" are stored """
dir = "/data/feedback/"

""" Get the list of all the files inside the directory """
fb_files = os.listdir(dir)

""" Create a dictionary where will store the data readed from each file """
dict = {"title":"",
        "name":"",
        "date":"",
        "feedback":""}

""" Iterate over each file """
for item in fb_files:
    """ Get rid of hidden files """
    if not item[0]==".":
      """ Open the file """
      with open(dir+item, "r") as file:
         """ Read line by line storing the content into the corresponding key in the dictionary """
         dict["title"] = file.readline()
         dict["name"] = file.readline()
         dict["date"] = file.readline()
         dict["feedback"] = file.readline()

    """ Post the data to the REST url """
    response = requests.post("http://34.70.198.39/feedback/", json=dict)
    """ Check the status of the response """
    print(response.status_code)