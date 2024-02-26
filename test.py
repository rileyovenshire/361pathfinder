import json
from wsgiref import headers

from flask import Flask, request, jsonify
import requests
from urllib3.util import url

BASE_URL = "http://localhost:5000"


def set_grid(rows, columns):
    url = f"{BASE_URL}/set_grid"
    data = {"rows": rows, "columns": columns}
    response = requests.post(url, json=data)
    print(response.json())


def calculate_path_length(path):
    url = f"{BASE_URL}/calculate_path_length"
    data = {"path": path}
    response = requests.post(url, json=data)
    print(response.json())


if __name__ == "__main__":
    # take in grid size, rows x columns
    set_grid(5, 5)

    # simple coordinate path
    path = [[0, 0], [1, 2], [2, 3]]

    # calculate and return path length
    calculate_path_length(path)

    # DEBUG PRINT ---------------------------------
    response = requests.post(url, json={'path': path}, headers=headers)
    print(f"Status Code: {response.status_code}, Response Text: '{response.text}'")
    if response.status_code == 200:
        try:
            print(response.json())
        except json.decoder.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}")
    else:
        print("Request failed.")
    # ---------------------------------------------