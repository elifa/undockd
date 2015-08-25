#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Blueprint, request

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