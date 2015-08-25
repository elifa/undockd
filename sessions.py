#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Blueprint

api = Blueprint("sessions", __name__)

@api.route("/")
def getSession():
    return "get session"