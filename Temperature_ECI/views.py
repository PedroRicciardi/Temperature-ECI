"""
Routes and views for the flask application.
"""
from flask import request
import json
import requests
from Temperature_ECI import app


@app.route('/temperature')
def temperatura():
	req = None

	cidade = request.args.get("city_name")
	link = 'https://api.hgbrasil.com/weather?key=283fef9b&=city_name='+cidade
	try:
		req = requests.get(link)
	
	
		texto = req.text
	
		result = dict(json.loads(texto))
		result = result['results']
	
		forecast = result['forecast']
	
		max = forecast[0]['max']
		min = forecast[0]['min']
		#print('bp2')
	
		temp = result['temp']
		return json.dumps({
			"temp_max": max,
			"temp_min": min,
			"temp": temp
			})

	except Exception as er:
		return str(er)
