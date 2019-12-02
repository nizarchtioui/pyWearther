# -*- coding: utf-8 -*-
"""
    flask-weather-app
    ~~~~~~~~~~~~

    A weather application.
  
    :copyright: (2019-2022) by NizarCht.
    :license: MIT, see LICENSE for more details.

"""

import os
from flask import Flask, request, render_template, g, jsonify
from datetime import date, timedelta
from src.api.WeatherMANGER import WeatherManager



# create app
app = Flask(__name__)
app.config['DEBUG'] = True
@app.route('/')
def index():
    try:
         place = request.args['place']
         current_ip = request.args['ip']
    except:
        current_ip = WeatherManager.get_ip()
        place = WeatherManager.getCountryName(current_ip)

    temper = WeatherManager.getWeatherByCountry(place)
    return render_template('index.html', country=place, C_Wearher = temper)
# @app.route('/temper')
# def getcountry():
#       ip = request.args['ip']
#       place = WeatherManager.getCountryName(ip)
#       return place
    

if __name__ == '__main__':
        import os  
        port = int(os.environ.get('PORT', 5000)) 
        app.run(host='0.0.0.0', port=port)