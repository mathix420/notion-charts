import json
import requests
from os import getenv
from notion.client import NotionClient
from flask import Flask, render_template, redirect

app = Flask(__name__)

width = 380
height = 220
labels = ['Done', 'In Progress', 'Todo']

client = NotionClient(token_v2=getenv('TOKEN_V2'))
URL_BASE = 'https://www.notion.so/businesstime/{}?v={}'
CHART_URL = f"https://quickchart.io/chart?w={width}&h={height}&bkg=white&c="


def get_stats(collection, view):
	try:
		cv = client.get_collection_view(URL_BASE.format(collection, view))
	except Exception as e:
		if str(e) == 'Invalid collection view URL':
			raise Exception('Bad view')
		else:
			raise

	todo, done, en_cours = 0, 0, 0

	rows = cv.default_query().execute()

	for row in rows:
		if row.status == 'In Progress':
			en_cours += 1
		elif row.status == 'Not Started':
			todo += 1
		else:
			done += 1

	d = done / len(rows) * 100
	p = en_cours / len(rows) * 100
	t = todo / len(rows) * 100
	return d, p, t, cv.name


@app.route('/robots.txt')
def robots():
	return 'User-agent: *\nDisallow: /'


@app.route('/chart-image/<collection>/<view>')
def get_chart_image(collection, view):
	d, p, t, _ = get_stats(collection, view)

	data = {
		'type': 'pie',
		'data': {
			'labels': labels,
			'borderWidth': 0,
			'datasets': [{'data': [d, p, t]}]
		},
		'options': {'plugins': {'outlabels': {'text': ''}}}
	}

	return redirect(CHART_URL + json.dumps(data))


@app.route('/chart/<collection>/<view>')
def get_chart(collection, view):
	d, p, t, title = get_stats(collection, view)

	return render_template('chart.html', datas=json.dumps([
		[labels[0], d],
		[labels[1], p],
		[labels[2], t]
	]), title=title)


@app.route('/')
def home():
	return '''Visit <a href="https://github.com/mathix420/notion-charts">
github.com/notion-charts
</a> for documentation.'''


if __name__ == "__main__":
	app.run()
