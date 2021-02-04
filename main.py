from flask import Flask, render_template, redirect, request, abort, jsonify
from werkzeug.exceptions import HTTPException
from requests.exceptions import HTTPError
from notion.client import NotionClient
from os import getenv
import json


app = Flask(__name__)
g = {}

width = 380
height = 220
default_labels = ['Not Started', 'In Progress', 'Done']

if 'client' not in g:
    try:
        print('init')
        # Could use this but we need caching and the endpoint is heavily rate limited
        # email='', password=''
        g['client'] = NotionClient(token_v2=getenv('TOKEN_V2'))
    except HTTPError as error:
        if error.response.status_code == 401:
            g['error'] = 'Bad Notion TOKEN_V2.'
        else:
            g['error'] = str(error)
        g['client'] = None

URL_BASE = 'https://www.notion.so/businesstime/{}?v={}'
CHART_URL = f'https://quickchart.io/chart?w={width}&h={height}&bkg=white&c='


def get_client():
    if not g['client'] and 'error' in g:
        raise Exception(g['error'])
    elif not g['client']:
        raise Exception('No client.')
    return g['client']


def remove_non_ascii(string):
    return bytes(string, 'utf-8').decode('ascii', 'ignore')


def get_stats(collection, view, labels, prop):
    try:
        cv = get_client().get_collection_view(URL_BASE.format(collection, view))
    except Exception as e:
        if str(e) == 'Invalid collection view URL':
            raise Exception('Bad view')
        raise

    elems = {label: 0 for label in labels}
    rows = cv.default_query().execute()

    if not rows or not prop in [x['slug'] for x in rows[0].schema]:
        abort(404, f'No {prop} found in the response.')

    for row in rows:
        values = row.get_property(prop)
        if not values:
            continue
        elif not isinstance(values, list):
            values = values.split(',')
        for value in values:
            if value in elems:
                elems[value] += 1
            else:
                elems[list(elems.keys())[-1]] += 1

    return elems, cv.name


def get_labels(request):
    labels = request.args.get('l')

    if labels:
        return labels.split('|')

    return default_labels


@app.errorhandler(Exception)
def handle_error(e):
    code = 500
    if isinstance(e, HTTPException):
        code = e.code
    return jsonify(error=str(e)), code


@app.route('/chart-image/<collection>/<view>')
def get_chart_image(collection, view):
    labels = get_labels(request)
    selector = request.args.get('p', 'status')
    elems, _ = get_stats(collection, view, labels, selector)

    data = {
        'type': 'pie',
        'data': {
                'labels': list(map(remove_non_ascii, elems.keys())),
                'borderWidth': 0,
            'datasets': [{'data': list(elems.values())}]
        },
        'options': {
            'plugins': {'outlabels': {'text': ''}},
            'rotation': 0,
        }
    }

    return redirect(CHART_URL + json.dumps(data))


@app.route('/chart/<collection>/<view>')
def get_chart(collection, view):
    dark_mode = 'dark' in request.args
    labels = get_labels(request)
    selector = request.args.get('p', 'status')
    elems, title = get_stats(collection, view, labels, selector)

    return render_template(
        'chart.html',
        datas=json.dumps(list(elems.items())),
        dark_mode=dark_mode,
        title=request.args.get('title', title),
    )


if __name__ == '__main__':
    app.run()
