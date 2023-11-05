#!/usr/bin/python3
"""Handling crud in the state api"""
from flask import Flask, jsonify, abort, request, make_response
from models import storage
from api.v1.views import app_views
from models.state import State


@app_views.route('/states', methods=['GET'], strict_slashes=False)
def all_state():
    """Retrieves all states object"""
    return jsonify([obj.to_dict() for obj in storage.all(State).values()])


@app_views.route('/states/<string:state_id>',
                 methods=['GET'],
                 strict_slashes=False)
def get_state(state_id):
    """making get request on api"""
    state = storage.get(State, state_id)
    if not state:
        abort(404)
    return jsonify(state.to_dict())


@app_views.route('/states/<string:state_id>',
                 methods=['DELETE'],
                 strict_slashes=False)
def delete_state(state_id):
    """making delete request on states api"""
    state = storage.get(State, state_id)
    if not state:
        abort(404)
    state.delete()
    state.save()
    return {}


@app_views.route('/states/', methods=['POST'], strict_slashes=False)
def create_state():
    """making post request on states api"""
    try:
        request.get_json()
    except Exception:
        return make_response(jsonify({"error": "Not a JSON"}), 400)
    if 'name' not in request.get_json():
        return make_response(jsonify({"error": "Missing name"}), 400)

    state = request.get_json()
    obj = State(**state)
    obj.save()
    return jsonify(obj.to_dict()), 201


@app_views.route('/states/', methods=['PUT'], strict_slashes=False)
def update_state(state_id):
    """making update request on states api"""
    try:
        request.get_json()
    except Exception:
        return make_response(jsonify({"error": "Not a JSON"}), 400)
    obj = storage.get(State, state_id)
    if obj is None:
        abort(404)
    for key, value in request.get_json().items():
        if key in ('id', 'created_at', 'updated_at'):
            setattr(obj, key, value)
    storage.save()
    return jsonify(obj.to_dict())
