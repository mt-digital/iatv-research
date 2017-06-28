import json
import uuid

from pandas import DataFrame

from flask import Flask, render_template, redirect, jsonify

from requests import get

EXAMPLE_ARCHIVE = \
        'https://archive.org/details/tv?q=epa+kill+jobs&time=20151129-20170625'

app = Flask(__name__)
app.config.from_envvar('CONFIG_FILE')


@app.route('/', methods=['GET'])
def hello():
    return render_template('index.html')


@app.route('/export', methods=['POST'])
def export():

    tmp_csv = 'app/static/tmp/' + str(uuid.uuid4()) + '.csv'

    # replace with URL passed in request, tag output=json, and request it
    res = get('http://localhost:5000/archive-mock')

    DataFrame(data=res.json()).to_csv(tmp_csv, index=False)

    return redirect(tmp_csv.replace('app/', ''))


@app.route('/archive-mock')
def archive_mock():

    return jsonify(json.loads(open('strangle-economy-ex.json').read()))
