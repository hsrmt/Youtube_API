from urllib.request import urlopen
import urllib.request 
#from urllib import *
import json
import datetime
import time


token = ""
access_url = "https://api.github.com/gists"

filename = "file.txt"
description = "the description for this gist"
public = "true"

information = "some info"
date = datetime.date.today()
current_time = time.strftime("%H:%M:%S")

data = """{
  "description": "%s",
  "public": %s,
  "files": {
    "%s": {
      "content": "info : %s,date: %s, current_time: %s"
    }
  }
}"""

json_data = data % (description, public, filename, information, date, current_time)
json_data = bytes(json_data,'utf-8')

req = urllib.request.Request(access_url)
req.add_header("Authorization", "token {}".format(token))
req.add_header("Content-Type", "application/json")
html = urlopen(req, data=json_data)
print(html)
print(access_url)
    