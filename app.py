import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify


#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
Climate = Base.classes.climate

#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    """List all available Climate api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations"
        f"/api/v1.0/tobs"
    )


@app.route("/api/v1.0/precipitations")
def names():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of all prcp """
    # Query all passengers
    results = session.query(Climate.prcp).all()

    session.close()

    # Convert list of tuples into normal list
    all_results = list(np.ravel(results))

    return jsonify(all_results)


@app.route("/api/v1.0/station")
def passengers():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of stations"""
    # Query all stations
    results = session.query(Climate.station).all()

    session.close()

    # Create a dictionary from the row data and append to a list of all_stations
    all_stations = []
    for station in results:
        station_dict["name"] = name
  
        all_stations.append(station_dict)

    return jsonify(all_passengers)

@app.route("/api/v1.0/tobs")
def passengers():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of tobs"""
    # Query all tobs
    results = session.query(Climate.tobs).all()

    session.close()

    all_tobs = []
    for tmin,tavg,tmax in results:
        tmin["tmin"] = name
  
        all_tobs.append(station_dict)

    return jsonify(all_passengers)


if __name__ == '__main__':
    app.run(debug=True)
