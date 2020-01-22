#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 15:58:31 2020

@author: kazzastic
"""

from setuptools import setup

setup(
    name='kazims_custom_code',
    version='0.1',
    install_requires=['opencv-python', 'pybase64'],
    scripts=['predictor.py', 'preprocess.py'])
