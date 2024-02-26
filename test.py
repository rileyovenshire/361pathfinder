import requests

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
