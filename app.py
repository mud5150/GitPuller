from flask import Flask, request
from urllib.parse import urlparse
from collections import namedtuple
from pathlib import Path, PureWindowsPath
from git import Repo
import json
import re

app = Flask('GitPuller')


@app.route("/")
def home():
    return "I am waiting for new git commits"

@app.route("/pull", methods=['POST'])
def new_commit():
    reqJson = request.get_json()
    commitId = reqJson["resource"]["commits"][0]["commitId"]
    author = reqJson["resource"]["commits"][0]["author"]["name"]
    date = reqJson["resource"]["commits"][0]["author"]["date"]
    print("Pulling commit " + commitId + " by " + author + " from " + date)
    print("git pull " + path._str)
    repo.remotes.origin.pull()
    return ("", 200, None)

if __name__ == '__main__':
    from argparse import ArgumentParser
    parser = ArgumentParser()
    parser.add_argument('-p')
    args = parser.parse_args()
    path = PureWindowsPath(args.p)
    repo = Repo(path)
    app.run('0.0.0.0', 5000)