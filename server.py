#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 03:17:34 2020

@author: kazzastic
"""

from flask import Flask, render_template, request, jsonify
#import tensorflow as tf
import os
import numpy as np
import base64
import cv2

app = Flask(__name__)
UPLOAD_FOLDER = os.path.basename('uploads')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

classes = ["normal", "cancer"]

@app.route('/', methods = ['GET', 'POST'])
def index_api_call():
    #model  = tf.keras.models.load_model("model/ddsm_vgg16_s10_[512-512-1024]x2_hybrid.h5")
    image_recieved = request.get_json() # here in the image_recieved file we have an image in base64 string form
    
    # What we need to do is to save/read this file into numbers form
    # BAscially the CNN is going to take image in a tensor form(matrix form) and for that purpose we need to convert base 64 into numbers
    
    
    image2 = 'I have won, but at what cost?'
    return jsonify(image2)

if __name__ == '__main__':
    app.run(host = '0.0.0.0',port = '8000')