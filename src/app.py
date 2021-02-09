from flask import Flask
import requests
import json
import os

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello, world!"

@app.route('/open_prs')
def open_prs():
    github_username = os.environ['GITHUB_USERNAME']
    github_token = os.environ['GITHUB_TOKEN']
    response = requests.get(
        f"https://api.github.com/search/issues?q=repo:CamelotVG/data-engineering+type:pr+state:open&per_page=1",
        auth=(github_username, github_token))

    response2 = requests.get(
        f"https://api.github.com/search/issues?q=repo:CamelotVG/data-engineering+type:pr+state:closed&per_page=1",
        auth=(github_username, github_token))

    open_prs = response.json()['total_count']

    closed_prs = response2.json()['total_count']

    dictionary = {
        "frames": [
            {
                "text": "{} open prs!!".format(open_prs),
                #"icon": "a21223"
                "icon": "9766"
            },
            {
                "text": "{} closed prs!!".format(closed_prs),
                "icon": "9767"
            }
        ]
    }
    json_object = json.dumps(dictionary, indent=4)
    return json_object


if __name__ == "__main__":
    app.run()

