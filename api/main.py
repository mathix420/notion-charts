from flask import Flask, render_template, redirect, request, jsonify
from os.path import abspath, dirname, join, realpath
from werkzeug.exceptions import HTTPException
from requests.exceptions import HTTPError
from notion.client import NotionClient
from itertools import groupby
from os import getenv
import traceback
import json


dir_path = dirname(realpath(__file__))
app = Flask(__name__, template_folder=join(dir_path, abspath('templates')))

g = {}
IMG_WIDTH = 380
IMG_HEIGHT = 220

TYPES_EXCLUDED = ['relation', 'person', 'date']
URL_BASE = 'https://www.notion.so/businesstime/{}?v={}'
CHART_URL = f'https://quickchart.io/chart?w={IMG_WIDTH}&h={IMG_HEIGHT}&bkg=white&c='


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


def get_client():
    if not g['client'] and 'error' in g:
        raise Exception(g['error'])
    elif not g['client']:
        raise Exception('No client.')
    return g['client']


def remove_non_ascii(string):
    return bytes(string, 'utf-8').decode('ascii', 'ignore')


def flatten_row(row):
    res = []

    for field, value in row.items():
        if value and (isinstance(value, list) or (isinstance(value, str) and ',' in value)):
            if not isinstance(value, list):
                value = value.split(',')
            for v in value:
                res += flatten_row({**row, field: v or 'EMPTY'})
        elif value == []:
            return flatten_row({**row, field: 'EMPTY'})

    return res or [row]


def clean_data(rows, fields):
    res = []
    rows = [{field: row.get_property(field)
             for field in fields} for row in rows]
    for row in rows:
        res += flatten_row(row)
    return res


def get_datas(collection, view, columns_schema):
    if not columns_schema:
        raise Exception('Bad schema')
    columns_schema = list(map(lambda x: x.split(':'), columns_schema))

    try:
        cv = get_client().get_collection_view(URL_BASE.format(collection, view))
    except Exception as e:
        if str(e) == 'Invalid collection view URL':
            raise Exception('Bad view')
        raise

    rows = cv.default_query().execute()
    datas = [list(map(lambda x: x[0], columns_schema))]

    flatten = clean_data(rows, set(map(lambda x: x[1], columns_schema)))
    grouped = groupby(sorted(flatten, key=lambda x: x[columns_schema[0][1]]), lambda x: x[columns_schema[0][1]])

    for key, group in grouped:
        datas.append([[]] * len(columns_schema))
        group = list(group)
        datas[-1][0] = key

        for i, schema in enumerate(columns_schema):
            _, field, action = schema

            if action == 'count':
                datas[-1][i] = len(list(filter(lambda x: x[field], group)))
            elif action == 'sum':
                datas[-1][i] = sum(map(lambda x: int(x[field]), group))
            elif action == 'avg':
                lst = list(map(lambda x: int(x[field]), group))
                datas[-1][i] = sum(lst) / len(lst)
            else:
                values = set(map(lambda x: x[field], group))
                datas[-1][i] = ','.join(map(str, values)) if len(values) > 1 else (list(values) or [''])[0]

    return cv, datas


@app.errorhandler(Exception)
def handle_error(e):
    """
    Handle and display errors to client.
    Log error traceback.
    """
    code = 500
    if isinstance(e, HTTPException):
        code = e.code
    print(traceback.format_exc())
    return jsonify(error=str(e)), code


@app.route('/notion-schema/<collection>/<view>')
def get_schema(collection, view):
    """
    Return schema of the current Notion database.
    """
    try:
        cv = get_client().get_collection_view(URL_BASE.format(collection, view))
    except Exception as e:
        if str(e) == 'Invalid collection view URL':
            raise Exception('Bad view')
        raise

    rows = cv.default_query().execute()

    return jsonify({
        'columns': list(filter(lambda x: x['type'] not in TYPES_EXCLUDED, rows[0].schema))
    }), 200


@app.route('/schema-chart/<collection>/<view>')
def build_schema_chart(collection, view):
    """
    Schema chart is the interactive chart.
    """
    dark_mode = 'dark' in request.args
    chart_type = request.args.get('t', 'PieChart')
    columns_schema = request.args.get('s', '').split(',')

    cv, datas = get_datas(collection, view, columns_schema)

    return render_template(
        'schema.html',
        dark_mode=dark_mode,
        chart_type=chart_type,
        datas=json.dumps(datas),
        title=request.args.get('title', cv.name),
    )


@app.route('/image-chart/<collection>/<view>')
def build_image_chart(collection, view):
    """
    Return an image chart generated by quickchart.io.
    """
    chart_type = request.args.get('t', 'PieChart')
    columns_schema = request.args.get('s', '').split(',')

    _, datas = get_datas(collection, view, columns_schema)

    labels = list(map(lambda x: remove_non_ascii(x[0]), datas[1:]))
    datasets = []

    nb_datasets = len(datas[0])

    for index in range(1, nb_datasets):
        datasets.append({
            'label': datas[0][index],
            'data': list(map(lambda x: x[index], datas[1:]))
        })

    data = {
        'type': chart_type.lower().replace('chart', ''),
        'data': {
            'labels': labels,
            'borderWidth': 0,
            'datasets': datasets
        },
        'options': {
            'plugins': {'outlabels': {'text': ''}},
            'rotation': 0,
        }
    }

    return redirect(CHART_URL + json.dumps(data))


if __name__ == '__main__':
    app.run()
