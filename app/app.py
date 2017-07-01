import os
import uuid

from glob import glob
from pandas import DataFrame

from flask import Flask, render_template, redirect, request

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

    # remove any previously-exported files
    glb = glob('app/static/tmp/*')
    for f in glb:
        os.remove(f)

    # get search results in json format
    search_url = request.form['iatv-url']

    tmp_csv = 'app/static/tmp/' + str(uuid.uuid4()) + '.csv'

    # replace with URL passed in request, tag output=json, and request it
    res = get(search_url + '&output=json&rows=1000')

    DataFrame(data=res.json()).to_csv(tmp_csv, index=False)

    return redirect(tmp_csv.replace('app/', ''))
