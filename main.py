import random
import string
import json

from flask import Flask, jsonify, redirect
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


with open("urls.json", "r") as file:
    urls = json.load(file)


def generateURL():
    url = ""
    for i in range(10):
        if random.randint(0,2) < 2 : # letter, 2/3 chance
            url += random.choice(string.ascii_lowercase)
        else: # number 1/3 chance
            url += str(random.randint(0,9))
    return url


class Retrieve(Resource):
    def get(self, shortened):
        if shortened not in urls:
            print(f"Tried forwarding {shortened}, does not exist")
            return jsonify({"message": "The url does not exist"})
        else:
            print(f"Forwarding {shortened} to {urls[shortened]}")
            return redirect(urls[shortened])

class Add(Resource):
    def get(self, url):
        shortened = generateURL()

        urls[shortened] = url
        json_str = json.dumps(urls, indent=4)
        with open("urls.json", "w") as file:
            file.write(json_str)

        print(f"Added {url} as {shortened}")
        return jsonify({"url:": shortened})


api.add_resource(Retrieve, "/<shortened>")
api.add_resource(Add, "/add/<path:url>")


if __name__ == "__main__":
    app.run(debug=True)
