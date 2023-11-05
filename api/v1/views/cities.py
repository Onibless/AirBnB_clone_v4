#!/usr/bin/python3
"""Cities CRUD handling"""
from flask import Flask, jsonify, abort, request, make_response
from models import storage
from api.v1.views import app_views
from models.city import City


@app_views.route('/cities', methods=['GET'], strict_slashes=False)
def all_city():
    """Retrieves all cities object"""
    return jsonify([obj.to_dict() for obj in storage.all(City).values()])


@app_views.route('/cities/<string:city_id>',
                 methods=['GET'],
                 strict_slashes=False)
def get_city(city_id):
    """making get request on api"""
    city = storage.get(City, city_id)
    if not city:
        abort(404)
    return jsonify(city.to_dict())


@app_views.route('/cities/<string:city_id>',
                 methods=['DELETE'],
                 strict_slashes=False)
def delete_city(city_id):
    """making delete request on cities api"""
    city = storage.get(City, city_id)
    if not city:
        abort(404)
    city.delete()
    city.save()
    return {}


@app_views.route('/cities/', methods=['POST'], strict_slashes=False)
def create_city():
    """making post request on cities api"""
    try:
        request.get_json()
    except Exception:
        return make_response(jsonify({"error": "Not a JSON"}), 400)
    if 'name' not in request.get_json():
        return make_response(jsonify({"error": "Missing name"}), 400)

    city = request.get_json()
    obj = City(**city)
    obj.save()
    return jsonify(obj.to_dict()), 201


@app_views.route('/cities/', methods=['PUT'], strict_slashes=False)
def update_city(city_id):
    """making update request on cities api"""
    try:
        request.get_json()
    except Exception:
        return make_response(jsonify({"error": "Not a JSON"}), 400)
    obj = storage.get(City, city_id)
    if obj is None:
        abort(404)
    for key, value in request.get_json().items():
        if key in ('id', 'created_at', 'updated_at'):
            setattr(obj, key, value)
    storage.save()
    return jsonify(obj.to_dict())
