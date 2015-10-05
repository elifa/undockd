#!/usr/bin/env python
# -*- coding: utf-8 -*-

import undockd
from flask import Blueprint, request

db = undockd.db
api = Blueprint("jobs", __name__)

@api.route("/")
def getJobs():
    return "list of accounts"

@api.route("/", methods=["POST"])
def createJob():
    return request.json

@api.route("/<job>", methods=["PATCH"])
def updateJob(job):
    return request.json + job

class User(db.Document):
    email = db.StringField(required=True)
    first_name = db.StringField(max_length=50)
    last_name = db.StringField(max_length=50)