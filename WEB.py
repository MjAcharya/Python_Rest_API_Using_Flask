from os import abort
from flask import Flask, jsonify
from flask import request
from flask import make_response

app = Flask(__name__)

employee_details = [{'id': 1, 'description': 'salary', 'amount': 9000}]


@app.route("/")
@app.route("/getAll")
def get_income():
    return jsonify(employee_details)


@app.route("/add", methods=['POST'])
def add_income():
    if not request.json or not 'id' in request.json:
        abort(400)
    description = {
        'id': employee_details[-1]['id'] + 1,
        'description': request.json.get('description', '')
    }
    employee_details.append(description)
    return jsonify(employee_details)


@app.route("/update/<int:idx>", methods=['PUT'])
def update_description(idx):
    if not request.json or not 'description' in request.json:
        abort(400)
    demo1 = [demo1 for demo1 in employee_details if demo1['id'] == idx]
    demo1[0]['description'] = request.json.get('description', demo1[0]['description'])
    return jsonify(demo1)


@app.route("/delete/<int:idx>", methods=['DELETE'])
def delete_description(idx):
    if not request.json:
        abort(400)
    employee_details.remove(idx)
    return jsonify(employee_details)


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 505)


if __name__ == "__main__":
    app.run()
