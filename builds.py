#!/usr/bin/env python
# -*- coding: utf-8 -*-

import undockd
from flask import Blueprint, request

db = undockd.db
api = Blueprint("builds", __name__)

@api.route("/")
def getBuilds():
    return "list of builds"

@api.route("/", methods=["POST"])
def createBuild():
    return request.json

@api.route("/<build>", methods=["PATCH"])
def updateBuild(job):
    return request.json + job

class Build(db.Document):
    email = db.StringField(required=True)
    first_name = db.StringField(max_length=50)
    last_name = db.StringField(max_length=50)