# Put your app in here.
from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)


@app.route('/add')
def add_nums():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    results = add(a,b)
    return f"{a} + {b} = {results}"

@app.route('/sub')
def add_nums():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    results = sub(a,b)
    return f"{a} - {b} = {results}"

@app.route('/mult')
def add_nums():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    results = mult(a,b)
    return f"{a} * {b} = {results}"

@app.route('/div')
def add_nums():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    results = div(a,b)
    return f"{a} / {b} = {results}"


operations = {
    "add": add,
    "sub": sub,
    "mult": mult,
    "div": div,
}

@app.route('/math/<operation>')
def math(operation):
    math_func = operations.get(operation, 'None')
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    results = math_func(a,b)
    return f"{results}"
