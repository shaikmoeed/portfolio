#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# from py import primos
from flask import Flask, request, render_template
import git  # GitPython library
import os


app = Flask(__name__)

# Route for the GitHub webhook


@app.route('/git_update', methods=['POST'])
def git_update():
    repo = git.Repo('./portfolio')
    origin = repo.remotes.origin
    repo.create_head('main',
                     origin.refs.main).set_tracking_branch(origin.refs.main).checkout()
    origin.pull()
    return '', 200


@app.route('/')
def index():
    # print(os.getcwd())
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
    """  app.run(host='0.0.0.0', port=80) """