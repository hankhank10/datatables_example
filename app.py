from flask import Flask, jsonify, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/getmyjson')
def getmyjson():

    json_example = {
        'data': [
            {
                "id": 1,
                "name": "Tiger Nixon",
                "position": "System Architect",
                "office": "Edinburgh",
            },
            {
                "id": 2,
                "name": "Bill Smith",
                "position": "Flask Designer",
                "office": "Edinburgh",
            },
            {
                "id": 3,
                "name": "Eric Jones",
                "position": "Javascript Expert",
                "office": "London",
            },
            {
                "id": 4,
                "name": "Tom Williams",
                "position": "Reddit Lurker",
                "office": "Manchester",
            },
            {
                "id": 5,
                "name": "Amyrah Nixon",
                "position": "System Architect",
                "office": "Manchester",
            },
        ]
    }

    return jsonify(json_example)


if __name__ == '__main__':
    app.run(debug=True)
