import requests
import datetime
from flask import json
import os

# Creating a user
pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": os.getenv("TOKEN"),
    "username": os.getenv("USERNAME"),
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
# response = requests.post(pixela_endpoint, json=user_params)
# print(response.text)

#-----------------------------------#

#Creating a graph
graph_endpoint = f"{pixela_endpoint}/{user_params['username']}/graphs"

graph_config = {
    "id": "graph1",
    "name": "ReadingGraph",
    "unit": "page(s)",
    "type": "int",
    "color": "momiji"
}

headers = {
    "X-USER-TOKEN": user_params['token'],
}
# response = requests.post(graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

#-----------------------------------#

#Creating a pixel
pixel_endpoint = f"{pixela_endpoint}/{user_params['username']}/graphs/{graph_config['id']}"

today = datetime.date.today()
today = today.strftime("%Y%m%d")
book = {"Book": "Shield of Sparrows"}

pixel_config = {
    "date": today,
    "quantity": "100",
    "optionalData": json.dumps(book),
}

# response = requests.post(pixel_endpoint, json=pixel_config, headers=headers)
# print(response.text)

#-----------------------------------#

#Editing a pixel
edit_endpoint = f"{pixel_endpoint}/{today}"

edit_config = {
    "quantity": "20",
    "optionalData": json.dumps(book),
}

# response = requests.put(edit_endpoint, json=edit_config, headers=headers)
# print(response.text)

#-----------------------------------#

#Deleting a pixel
delete_endpoint = f"{pixel_endpoint}/{today}"
response = requests.delete(delete_endpoint, headers=headers)
print(response.text)

