from flask import Flask, request, jsonify

app = Flask(__name__)


# ROUTES -----------------------------------------------------------------------------------
@app.route('set_grid', methods=['POST'])
def set_grid():
    """
    Allows the user to set rows and columns of the grid that the path finding algorithm will use.
    """
    # fetch data
    data = request.json
    rows = data.get('rows')
    columns = data.get('columns')

    # error handling
    if not rows or not columns:
        return jsonify({'message': 'Please provide both rows and columns'}), 400

    # return success message
    return jsonify({'message': f'Grid size set to {rows}x{columns}'}), 200


@app.route('calculate_length', methods=['POST'])
def calculate_path_length():
    """
    Allows the user to calculate the length of the path from the start to the end of the grid.

    Path should be passed as a list of coordinates, e.g. [(x1, y1), (x2, y2), ...]
    """
    # fetch data
    data = request.json
    path = data.get('path')
    length = data.get('length')

    # error handling
    if not path:
        return jsonify({'message': 'Please provide a path'}), 400

    # return success message
    return jsonify({'message': f'Path length is {length}'}), 200


# PATH CALCULATION ALGORITHM -------------------------------------------------------------
def calculate_length(path):
    """
    Calculates the length of the path from the start to the end of the grid.
    """
    length = 0
    for i in range(len(path)):
        length += ((path[i][0] - path[i-1][0]) ** 2 + (path[i][1] - path[i-1][1]) ** 2) ** 0.5
    return length


# MAIN -------------------------------------------------------------------------------------
if __name__ == '__main__':
    app.run(debug=True)
