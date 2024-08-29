# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 22:53:01 2024

@author: Dell
"""# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 22:00:31 2024

@author: Dell
"""

# app.py
from flask import Flask, jsonify, render_template
import random

app = Flask(__name__)

# Mock dataset of exoplanets
exoplanets = [
    {"name": "Kepler-22b", "star": "Kepler-22", "distance": 600, "right_ascension": 19.44, "declination": 47.64},
    {"name": "Proxima Centauri b", "star": "Proxima Centauri", "distance": 4.2, "right_ascension": 14.29, "declination": -62.67},
    {"name": "TRAPPIST-1e", "star": "TRAPPIST-1", "distance": 39.5, "right_ascension": 23.22, "declination": -5.28},
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/exoplanets', methods=['GET'])
def get_exoplanets():
    return jsonify(exoplanets)

@app.route('/stars/<exoplanet>', methods=['GET'])
def get_stars(exoplanet):
    # For now, we generate random stars
    stars = []
    for i in range(50):
        star = {
            "name": f"Star-{i}",
            "right_ascension": random.uniform(0, 24),
            "declination": random.uniform(-90, 90)
        }
        stars.append(star)
    return jsonify(stars)

if __name__ == '__main__':
    app.run(debug=True)
@app.route('/stars/<exoplanet>', methods=['GET'])
def get_stars1(exoplanet):
    # Mock data - replace with real star positions
    stars = [
        {"name": "Alpha Centauri", "right_ascension": 14.66, "declination": -60.83},
        {"name": "Betelgeuse", "right_ascension": 5.92, "declination": 7.41},
        # Add more real data here...
    ]
    return jsonify(stars)
