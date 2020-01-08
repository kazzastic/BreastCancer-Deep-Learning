#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 03:17:34 2020

@author: kazzastic
"""

from flask import Flask, render_template, request, jsonify
#import tensorflow as tf
import os
import base64
import numpy as np
import json

app = Flask(__name__)
UPLOAD_FOLDER = os.path.basename('uploads')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

classes = ["normal", "cancer"]


@app.route('/', methods = ['GET', 'POST'])
def index_api_call():
    #model  = tf.keras.models.load_model("model/ddsm_vgg16_s10_[512-512-1024]x2_hybrid.h5")
    image_recieved = request.get_json()
    #image = base64.b64decode(image_recieved)
    #image = cv2.imdecode(np.fromstring(image_recieved.read(), np.uint8), cv2.IMREAD_UNCHANGED)
    print("******************")
    print(image_recieved)
    print("******************")
    image2 = 'nothing'
    return jsonify(image2)

if __name__ == '__main__':
    app.run(host = '0.0.0.0',port = '8000')