import flask
from flask import Flask, jsonify, url_for, redirect
from werkzeug.routing import BaseConverter

app = Flask(__name__)


class ListConvertter(BaseConverter):
    def to_python(self, value):
        return value.split("+")


class demo1(BaseConverter):
    regex = '\d*\+\d*'

    # def to_python(self, value):
    #     return value.split("+")

    def to_url(self, value):
        # print(value)
        return "+".join(value)


app.url_map.converters['list'] = ListConvertter
app.url_map.converters['demo1'] = demo1


@app.route('/')
def index():
    url_for("pa")
    return redirect(url_for("base", value=["10", "50"]))


@app.route('/path/<demo1:value>')
def base(value):
    print("base", value)
    return jsonify(value)

@app.route("/pa")
def pa():
    print("== page")
    return "page"

if __name__ == '__main__':
    app.run(debug=True)
