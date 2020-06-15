from flask import Flask, render_template, redirect, request
from notion.client import NotionClient
from os import getenv

import requests
import json


app = Flask(__name__)

width = 380
height = 220
default_labels = ['Not Started', 'In Progress', 'Done']

client = NotionClient(token_v2=getenv('TOKEN_V2'))
URL_BASE = 'https://www.notion.so/businesstime/{}?v={}'
CHART_URL = f"https://quickchart.io/chart?w={width}&h={height}&bkg=white&c="


def get_stats(collection, view, labels):
	try:
		cv = client.get_collection_view(URL_BASE.format(collection, view))
	except Exception as e:
		if str(e) == 'Invalid collection view URL':
			raise Exception('Bad view')
		raise

	elems = {label: 0 for label in labels}
	rows = cv.default_query().execute()

	for row in rows:
		if row.status in elems:
			elems[row.status] += 1
		else:
			elems[list(elems.keys())[-1]] += 1

	elems = dict(map(
		lambda kv: (kv[0], kv[1] / len(rows) * 100),
		elems.items()
	))

	return elems, cv.name


def get_labels(request):
	labels = request.args.get('l')

	if labels:
		return labels.split('|')

	return default_labels


@app.route('/chart-image/<collection>/<view>')
def get_chart_image(collection, view):
	labels = get_labels(request)
	elems, _ = get_stats(collection, view, labels)

	data = {
		'type': 'pie',
		'data': {
				'labels': list(elems.keys()),
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
	elems, title = get_stats(collection, view, labels)

	return render_template('chart.html',
		datas=json.dumps(list(elems.items())),
		dark_mode=dark_mode,
		title=title,
	)


if __name__ == "__main__":
	app.run()
