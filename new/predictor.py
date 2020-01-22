#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 15:58:11 2020

@author: kazzastic
"""

import tensorflow as tf
import os
import pickle
import numpy as np
import cv2
import base64


class MyPredictor(object):
    def __init__(self, model, preprocessor):
        self._model = model
        self._preprocessor = preprocessor
        self._class_names = ["normal", "cancer"]

    def predict(self, instances, **kwargs):
        inputs = instances
        image_str = inputs[0]['b64']
        image_bytes = bytes(image_str, 'utf-8')
        np_arr = np.fromstring(base64.decodebytes(image_bytes), np.uint8)
        image_to_numpy = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)
        preprocessed_inputs = self._preprocessor.preprocess(image_to_numpy)
        outputs = self._model.predict(preprocessed_inputs)

        if kwargs.get('probablities'):
            return outputs.tolist()
        else:
            return [self._class_names[index] for index in np.argmax(outputs, axis=1)]

    @classmethod
    def from_path(cls, model_dir):
        model_path = os.path.join(model_dir, 'saved_model')
        model = tf.compat.v1.saved_model.load_v2(
            export_dir=str(model_path), tags=None)

        preprocessor_path = os.path.join(
            model_dir, 'assets', 'preprocessor.pkl')
        with open(preprocessor_path, 'rb') as f:
            preprocessor = pickle.load(f)

        return cls(model, preprocessor)
