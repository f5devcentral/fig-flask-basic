#!/usr/bin/env python3

# coding=utf-8
# pylint: disable=broad-except,unused-argument,line-too-long, unused-variable
# Copyright (c) 2016-2018, F5 Networks, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
"""
This module contains the Flask application to build ISO9660 ConfigDrives
from posted user_data YAML
"""

import os
import json

from flask import Flask, redirect, url_for

app = Flask(__name__)

APP_URI = '/fig-flask-basic'


@app.route('/')
def index():
    """  Redirects index to application URI """
    return redirect(url_for('helloworld'))


@app.route(APP_URI)
def helloworld():
    """ Implements Main Interface """
    return "Hello f5-icontrol-gateway programmer"
