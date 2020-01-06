#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 03:17:34 2020

@author: kazzastic
"""

from flask import Flask, render_template, request, jsonify
import tensorflow as tf
import os
import cv2
import math

app = Flask(__name__)
UPLOAD_FOLDER = os.path.basename('uploads')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

classes = ["normal", "cancer"]


def prepare(filepath): 
    img_array = cv2.imread(filepath)
    new_array = cv2.resize(img_array, (height, width))

    return new_array.reshape(-1, height, width, 3)


model = tf.keras.models.load_model("ddsm_vgg16_s10_[512-512-1024]x2_hybrid.h5")
height = model.input.shape[1]
width = model.input.shape[2]

prediction = model.predict([prepare('cancer.jpg')])
print(prediction)  # will be a list in a list.
normal = math.ceil(prediction[0][1]*100)
cancer = math.ceil(prediction[0][0]*100)
result = [{'id': 0, 'title':'Normal', 'Prediction': normal},
          {'id': 1, 'title':'Cancer', 'Prediction': cancer}]
print("normal {0}\ncancer {1}".format(normal, cancer))

@app.route('/')
def index_api_call():
    return jsonify(result)

if __name__ == '__main__':
    app.run(host = '0.0.0.0',port = '8000')