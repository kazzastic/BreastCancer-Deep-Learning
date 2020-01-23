#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 03:17:34 2020

@author: kazzastic
"""

from flask import Flask, render_template, request, jsonify
from flask_cors import CORS, cross_origin
from werkzeug.utils import secure_filename
import os
import numpy as np
import base64
import cv2
from util import convertToJpg, allowed_file
import aws


UPLOAD_FOLDER = os.path.basename('uploads')

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

app.secret_key = "6575fae36288be6d1bad40b99808e37f"
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route("/", methods=["POST"])
@cross_origin()
def process_image():
    image_recieved = request.get_json()

    filename = secure_filename(image_recieved['filename'])
    imgdata = base64.b64decode(image_recieved['data'])

    if (not imgdata) and (filename == '') and (not allowed_file(filename)):
        return jsonify({'message': "Invalid Image.", 'code': 400})

    with open(os.path.join(app.config['UPLOAD_FOLDER'],
                           filename), 'wb') as f:
        f.write(imgdata)

    filepath_for_model = convertToJpg(app, filename)

    response = {}
    prediction_result = aws.invoke_model(filepath_for_model)

    response['data'] = prediction_result
    response['code'] = 200

    return jsonify(response)


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5001))
    app.run(host='127.0.0.1', port=5001)
