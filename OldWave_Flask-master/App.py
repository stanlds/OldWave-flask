from flask import Flask, render_template, request, redirect, url_for, flash,jsonify
from flask_mysqldb import MySQL
import json
import os

app = Flask(__name__)

@app.route('/api/search', methods=['GET'])
def search():
    user = request.args.get('q')

    SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
    json_url = os.path.join(SITE_ROOT, "jsonBusqueda.json")
    data = json.load(open(json_url))
    return data

@app.route('/api/item/<id>',methods=['GET'])
def detalle(id):

    SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
    json_url = os.path.join(SITE_ROOT, "jsonDetalle.json")
    data = json.load(open(json_url))

    return data

if __name__ == '__main__':
    app.run(port = 8008, debug = True)

    
