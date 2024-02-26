import requests


def set_grid(base_url, grid_size):
    """Sends a POST request to set the grid size."""
    url = f"{base_url}/set_grid"
    response = requests.post(url, json=grid_size)
    return response.json()


def calculate_path_length(base_url, path):
    """Sends a POST request to calculate the length of a path."""
    url = f"{base_url}/calculate_length"
    response = requests.post(url, json={"path": path})
    return response.json()


if __name__ == "__main__":
    base_url = 'http://127.0.0.1:5000'  # Adjust if your Flask app is running on a different URL/port
    grid_size = {"rows": 5, "columns": 5}
    path = [[0, 0], [1, 1], [2, 2]]

    # Set grid size
    grid_response = set_grid(base_url, grid_size)
    print("Grid Response:", grid_response)

    # Calculate path length
    path_length_response = calculate_path_length(base_url, path)
    print("Path Length Response:", path_length_response)
