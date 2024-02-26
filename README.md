# Pathfinder Microservice

A Flask-based web application that allows users to submit a grid size and a path defined by a list of coordinates. It calculates the length of the provided path and returns it to the user. Here you will find information on setting up the application, its endpoints and how to interact with it.


## Application Structure
The application is structured around two primary endpoints:

- /set_grid: Accepts a POST request with JSON data specifying the rows and columns of the grid.
- /calculate_path_length: Accepts a POST request with a list of coordinates representing the path and calculates its length.


### Key Code Snippets
Setting Grid Size: receives the grid size in rows and columns:

```sh
@app.route('/set_grid', methods=['POST'])
def set_grid():
    data = request.json
    rows = data.get('rows')
    columns = data.get('columns')
    return jsonify({'message': f'Grid size set to {rows}x{columns}'}), 200
```
Key Points:
The grid size is received as JSON data.
The endpoint responds with a confirmation message.

Calculating Path Length: calculates the length of the provided path:
```sh
@app.route('/calculate_path_length', methods=['POST'])
def calculate_path_length():
    data = request.json
    path = data.get('path')
    length = calculate_length(path)
    return jsonify({'length': length}), 200
```

The calculate_length function computes the Euclidean distance between consecutive points:
```sh
def calculate_length(path):
    length = 0
    for i in range(1, len(path)):
        length += ((path[i][0] - path[i-1][0]) ** 2 + (path[i][1] - path[i-1][1]) ** 2) ** 0.5
    return length
```

Key Points:
The path length is calculated using Euclidean distance formula.
The response includes the calculated length of the path.


## Interacting with the Application
### Setting the Grid Size
Use a tool like curl or Postman to send a POST request:

```sh
curl -X POST -H "Content-Type: application/json" -d '{"rows": 5, "columns": 5}' http://localhost:5000/set_grid
```

### Calculating the Path Length
To calculate the length of a path, send a POST request with the path coordinates:
```
sh
curl -X POST -H "Content-Type: application/json" -d '{"path": [[0, 0], [1, 1], [2, 2]]}' http://localhost:5000/calculate_path_length
```

And that's all there is to it - reach out to me if you have any questions/troubles. Best!

