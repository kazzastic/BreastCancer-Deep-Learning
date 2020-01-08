#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 03:17:34 2020

@author: kazzastic
"""

from flask import Flask, render_template, request, jsonify
from flask import Request
import tensorflow as tf
import os
import cv2
import math

app = Flask(__name__)
UPLOAD_FOLDER = os.path.basename('uploads')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

classes = ["normal", "cancer"]


@app.route('/', methods = ['GET', 'POST'])
def index_api_call():
    #model  = tf.keras.models.load_model("model/ddsm_vgg16_s10_[512-512-1024]x2_hybrid.h5")
    if Request.json:
        image_recieved = Request.get_json()
    print(image_recieved)
    result = "bhai result aaagya mubarook"
    return jsonify(result)

if __name__ == '__main__':
    app.run(host = '0.0.0.0',port = '8000')