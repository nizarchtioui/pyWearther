# -*- coding: utf-8 -*-
"""
    flask-weather-app
    ~~~~~~~~~~~~

    A weather application.
  
    :copyright: (2016) by solcis.
    :license: MIT, see LICENSE for more details.

"""

import os
from flask import Flask, request, render_template, g, jsonify
from datetime import date, timedelta
from src.api.WeatherMANGER import WeatherManager

port = int(os.environ.get('PORT', 5000))


# create app
app = Flask(__name__)

@app.route('/')
def index():
    current_ip = WeatherManager.get_ip()
    country = WeatherManager.getCountryName(current_ip)
    temper = WeatherManager.getWeatherByCountry(country)
    return render_template('index.html', country=country, C_Wearher = temper)

app.run(host='0.0.0.0', port=port, debug=True)
