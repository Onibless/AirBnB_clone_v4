#!/usr/bin/python3
""" Starts a Flash Web Application """
from models import storage
from models.state import State
from models.amenity import Amenity
from models.place import Place
from os import environ
from flask import Flask, render_template
import uuid
app = Flask(__name__)
# app.jinja_env.trim_blocks = True
# app.jinja_env.lstrip_blocks = True


@app.teardown_appcontext
def close_storage(error):
    """ Remove the current SQLAlchemy Session """
    storage.close()


@app.route('/1-hbnb/', strict_slashes=False)
def hbnb_home():
    """ HBNB home page and activation"""
    states = sorted(storage.all(State).values(),
                    key=lambda val: val.name)
    states_list = []
    for state in states:
        states_list.append([sorted(state.cities, key=lambda val: val.name)])
    amenities = sorted(storage.all(Amenity).values(),
                       key=lambda val: val.name)
    places = sorted(storage.all(Place).values(),
                    key=lambda val: val.name)

    return render_template('1-hbnb.html', states=states_list,
                           amenities=amenities, places=places,
                           cache_id=uuid.uuid4())


if __name__ == "__main__":
    """ Main Function """
    app.run(host='0.0.0.0', port=5000)
