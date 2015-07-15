from flask import Flask, request
from operations import *
from parser import *
app = Flask(__name__)

@app.route('/<int:number_1>/<int:number_2>/')
def operate(number_1, number_2):
    try:
        return "%r" % operation[request.args.get('operation')](number_1, number_2)
    except KeyError:
        return "Error: need an operation for two numbers. After the url, type '?operations=', then the operation. Operations are: %s" % operation

@app.route('/<int:number>')
def rand_operate(number):
    try:
        return "%r" % operation[request.args.get('operation')](number, result)
    except KeyError:
        return "Error: need an operation for two numbers. After the url, type '?operations=', then the operation. Operations are: %s" % operation
    
if __name__ == "__main__":
    app.run(debug=True)
