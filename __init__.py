#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from flask import Flask, redirect
from flask.ext.mongoengine import MongoEngine

app = Flask(__name__)

app.config["PROPAGATE_EXCEPTIONS"] = True
app.config["SEND_FILE_MAX_AGE_DEFAULT"] = 1
app.config["MONGODB_SETTINGS"] = {
    "db": __name__,
    "host": os.environ.get("MONGO_PORT_27017_TCP_ADDR", "127.0.0.1"),
    "port": int(os.environ.get("MONGO_PORT_27017_TCP_PORT", 27017))
}

db = MongoEngine(app)

from undockd import jobs, users, builds, sessions

app.register_blueprint(jobs.api, url_prefix="/jobs")
app.register_blueprint(users.api, url_prefix="/users")
app.register_blueprint(builds.api, url_prefix="/builds")
app.register_blueprint(sessions.api, url_prefix="/sessions")

@app.route("/")
def index():
    return redirect("static/index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)), debug=True)
