from flask import Flask, jsonify, abort, request
from flask_cors import CORS
from utils import get_packages

app = Flask(__name__)
CORS(app)


@app.route('/api/v1/ping')
def hello_world():
    return 'Pong. PS. Hello Reaktor, pls hire'


@app.route('/api/v1/packages')
def package_list():
    packages = get_packages()
    return jsonify(packages)


@app.route('/api/v1/package/<int:id>')
def package_detail(id=None):
    packages = get_packages()
    package = None
    if id is not None:
        for p in packages:
            if p["id"] == id:
                package = p
                break
    if package is None:
        return jsonify(error=404, message="Package not found"), 404
    return jsonify(package)


if __name__ == '__main__':
    app.run(port=5001)
