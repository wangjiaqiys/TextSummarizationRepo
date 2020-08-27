from bottle import Bottle, static_file, get
from bottle import template
from bottle import request
import json
from worker import process


root = Bottle()

@root.route('/', method=['GET', 'POST'])
def index():
    print(request.method)
    if request.method == 'GET':
        print("GET")
        name = {}
        name = json.dumps(name)
        return template('index.html', name=name)
    else:
        print("pust")
        string = request.forms.getunicode('string')
        print(string)
        string = string.encode("utf-8")

        title = request.forms.getunicode('title')
        print(title)
        title = title.encode("utf-8")
        
        contents_dict = process(string, title)
        print(contents_dict)
        contents_dict = json.dumps(contents_dict)

        return template('index.html', name=contents_dict)

# Static Routes
@root.route("/static/css/<filepath:re:.*\.css>", method=['GET', 'POST'])
def css(filepath):
    return static_file(filepath, root="static/css")

@root.route("/static/font/<filepath:re:.*\.(eot|otf|svg|ttf|woff|woff2?)>", method=['GET', 'POST'])
def font(filepath):
    return static_file(filepath, root="static/font")

@root.route("/static/img/<filepath:re:.*\.(jpg|png|gif|ico|svg)>", method=['GET', 'POST'])
def img(filepath):
    return static_file(filepath, root="static/img")

@root.route("/static/js/<filepath:re:.*\.js>", method=['GET', 'POST'])
def js(filepath):
    return static_file(filepath, root="static/js")

root.run(host='localhost', port=5055)
