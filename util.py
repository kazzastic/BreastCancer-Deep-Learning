#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 03:17:34 2020

@author: kazzastic
"""

import os
from PIL import Image
import json
import numpy as np

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}


class NumpyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return json.JSONEncoder.default(self, obj)


def convertToJpg(app, filename):
    image = Image.open(os.path.join(app.config['UPLOAD_FOLDER'], filename))

    if '.' in filename and \
            filename.rsplit('.', 1)[1].lower() in {'jpg', 'jpeg'}:  # no need for conversion
        return os.path.join(app.config['UPLOAD_FOLDER'], filename)

    new_file_name = filename.rsplit('.', 1)[0]+'.jpg'
    image.save(os.path.join(app.config['UPLOAD_FOLDER'], new_file_name))

    os.remove(os.path.join(app.config['UPLOAD_FOLDER'], filename))

    return os.path.join(app.config['UPLOAD_FOLDER'], new_file_name)


def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def filterResponse(response_body):
    my_json = response_body.decode('utf8').replace("'", '"')
    data = json.loads(my_json)
    formated_response = json.loads(json.dumps(data, indent=4, sort_keys=True))
    return formated_response
