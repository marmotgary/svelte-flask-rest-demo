from flask import Flask, jsonify, abort, request, Response
from flask_cors import CORS
from utils import get_packages

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_world():
    return 'Hello Reaktor, pls hire'


@app.route('/api/v1/packages')
def package_list():
    packages = get_packages()
    return jsonify(packages)


@app.route('/api/v1/package/<int:id>')
@app.route('/api/v1/package')
def package_detail(id=None):
    packages = get_packages()
    package = None
    if id:
        for p in packages:
            if p["id"] == id:
                package = p
                break
    elif "name" in request.args:
        name = request.args['name']
        for p in packages:
            if p["name"] == name:
                package = p
                break
    if package is None:
        abort(404)
    return jsonify(package)


if __name__ == '__main__':
    app.run(port=5001)
