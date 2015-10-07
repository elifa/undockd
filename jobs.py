#!/usr/bin/env python
# -*- coding: utf-8 -*-

import undockd
from flask import Blueprint, request, jsonify
from docker import Client

db = undockd.db
api = Blueprint("jobs", __name__)
docker = Client(base_url="unix://var/run/docker.sock")

@api.route("/")
def getJobs():
    return jsonify(data=Job.objects)

@api.route("/", methods=["POST"])
def createJob():
    return request.json

@api.route("/<job>", methods=["PATCH"])
def updateJob(job):
    return request.json + job

class Image(db.EmbeddedDocument):
    id = db.StringField(required=True)
    name = db.StringField(required=True)

class Container(db.EmbeddedDocument):
    id = db.StringField(required=True)
    name = db.StringField(required=True)
    branch = db.StringField(required=True)

class Repository(db.EmbeddedDocument):
    url = db.StringField(required=True)
    auth = db.StringField()

class Job(db.Document):
    id = db.StringField(required=True)
    name = db.StringField(required=True)
    image = db.EmbeddedDocumentField(Image)
    repository = db.EmbeddedDocumentField(Repository)
    containers = db.EmbeddedDocumentListField(Container)