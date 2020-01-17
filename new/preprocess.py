#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 15:57:57 2020

@author: kazzastic
"""

import cv2

class MySimpleScaler(object):
  def __init__(self):
    self.new_array = None
    
  def preprocess(self, image):
      
      new_array = cv2.resize(image, (1152, 896))
      return new_array.reshape(-1, 1152, 896, 3)
  