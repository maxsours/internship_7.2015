from flask import Flask, request
from operations import operation
from operations import add, subtract, multiply, divide
from parser import get_random_number_from_website
from timer import Timer

app = Flask(__name__)

@app.route("/<int:number_1>/<int:number_2>/")
def operate(number_1, number_2):
    try:
        return "{}".format(
            operation[request.args.get('operation')](number_1, number_2)
        )
    except KeyError:
        return "Error: need an operation for two numbers. After the url, type " \
               "'?operation=', then the operation. Operations are: " \
               "{}".format(operation)

@app.route('/<int:number>/')
def rand_operate(number):
    try:
        random = get_random_number_from_website(
            request.args.get("min"),
            request.args.get("max"),
        )
        return "{}".format(
            operation[request.args.get('operation')](number, random[0])
        )
    except KeyError:
        return "Error: need an operation for two numbers. After the url, " \
               "type '?operation=', then the operation. " \
               "Operations are: {}".format(operation)

@app.route('/ifthen/<int:number_1>/<int:number_2>/')
def ifthen_operate(number_1, number_2):
    operation = request.args.get('operation')
    if operation == "addition":
        return "{}".format(add(number_1, number_2))
    elif operation == "subtraction":
        return "{]".format(subtract(number_1, number_2))
    elif operation == "multiplication":
        return "{}".format(multiply(number_1, number_2))
    elif operation == "division":
        return "{}".format(divide(number_1, number_2))
    else:
        return "Error: need an operation for two numbers. After the url, type 'operation=', then the operation. Operations are: addition, subtraction, multiplication, and division."

if __name__ == "__main__":
    app.run(debug=True)
