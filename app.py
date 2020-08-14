import os
from flask import Flask, Response, render_template, request, jsonify

from utils import add_member

app = Flask(__name__)


@app.route('/', methods=['GET'])
def main():
  data = dict(
    org_name=os.environ['ORGANIZATION_NAME'],
    join_key=None
  )

  if "JOIN_KEY" in os.environ:
    data['join_key'] = os.environ['JOIN_KEY']

  return render_template("main.html", data=data)


@app.route('/add', methods=['PUT'])
def add():
  if "JOIN_KEY" in os.environ:
    join_key = request.json['join_key']
    if join_key != os.environ['JOIN_KEY']:
      return render_template("wrong_key.html")

  org_name = os.environ['ORGANIZATION_NAME']
  github_token = os.environ['GITHUB_ACCESS_TOKEN']
  username = request.json['username']

  success = add_member(username, org_name, github_token)

  if not success:
    return render_template("error.html")

  result = dict(
    org_url="https://github.com/orgs/{org_name}/invitation".format(org_name=org_name)
  )

  return jsonify(result), 200

if __name__ == "__main__":
  app.run(host="0.0.0.0")