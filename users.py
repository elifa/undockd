#!/usr/bin/env python
# -*- coding: utf-8 -*-

import undockd
from flask import Blueprint, request

db = undockd.db
api = Blueprint("users", __name__)

@api.route("/")
def getUsers():
    return "list of users"

@api.route("/", methods=["POST"])
def createUser():
    return request.json

@api.route("/<user>", methods=["PATCH"])
def updateUser(job):
    return request.json + job

class User(db.Document):
    email = db.StringField(required=True)
    first_name = db.StringField(max_length=50)
    last_name = db.StringField(max_length=50)