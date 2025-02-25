from flask import Flask, request, jsonify


app = Flask(__file__)

@app.route("/postDemo", methods=["POST"])
def post_demo_api():
    req_body = request.get_json()

    name = req_body["name"]
    age = req_body["age"]

    # insert userinfo to db


    return jsonify({"message": "success", "number": "12345"})

if __name__ == '__main__':
    app.run()