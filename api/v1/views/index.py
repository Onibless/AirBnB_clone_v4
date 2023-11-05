#!/usr/bin/python3
"""index.py module"""
from api.v1.views import app_views
from flask import Flask
from flask import jsonify
from models import storage


@app_views.route('/status', strict_slashes=False)
def status():
    """
    loads a JSON status
    """
    return jsonify({"status": "OK"})


@app_views.route('/stats', strict_slashes=False)
def counts():
    """returns the number of each objects by type"""
    count = {
        "amenities": storage.count("Amenity"),
        "cities": storage.count("City"),
        "places": storage.count("Place"),
        "reviews": storage.count("Review"),
        "states": storage.count("State"),
        "users": storage.count("User")
        }
    return jsonify(count)


if __name__ == "__main__":
    pass
