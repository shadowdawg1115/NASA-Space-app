from flask import Flask, jsonify, render_template, request
import json
import random

app = Flask(__name__)
constellations = []

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
    stars = []
    for i in range(50):
        star = {
            "name": f"Star-{i}",
            "right_ascension": random.uniform(0, 24),
            "declination": random.uniform(-90, 90)
        }
        stars.append(star)
    return jsonify(stars)

@app.route('/save_constellation', methods=['POST'])
def save_constellation():
    data = request.json
    constellations.append(data)
    return jsonify({'message': 'Constellation saved successfully!'})

@app.route('/get_constellations', methods=['GET'])
def get_constellations():
    return jsonify(constellations)

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)
