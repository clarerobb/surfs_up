import datetime as dt
import numpy as np
import pandas as pd
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify

#access and query database
engine = create_engine("sqlite:///hawaii.sqlite")

#reflect database into classes
Base = automap_base()

#reflect db
Base.prepare(engine, reflect=True)

#save references
Measurement = Base.classes.measurement
Station = Base.classes.station

# create a sessions link
session = Session(engine)

# define flask app
app = Flask(__name__)

#define welcome route
@app.route('/')

def welcome():
    return(
    '''
    Welcome to the Climate Analysis API! <br>
    Available Routes: <br>
    /api/v1.0/precipitation <br>
    /api/v1.0/stations <br>
    /api/v1.0/tobs <br>
    /api/v1.0/temp/start/end <br>
    ''')

#make precipitation route
@app.route('/api/v1.0/precipitation')

#make precipitation function
def precipitation():
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    precipitation = session.query(Measurement.date, Measurement.prcp).\
        filter(Measurement.date >= prev_year).all()
    precip = {date: prcp for date, prcp in precipitation}
    return jsonify(precip)

#make stations route
@app.route('/api/v1.0/stations')

#make stations function
def stations():
    results = session.query(Station.station).all()
    stations = list(np.ravel(results))
    return jsonify(stations=stations)

#make tobs route
@app.route('/api/v1.0/tobs')

#make tobs function
def temp_monthly():
    prev_year = dt.date( 2017, 8, 23) - dt.timedelta(days=365)
    results = session.query(Measurement.tobs).\
        filter(Measurement.station == 'USC00519281').\
        filter(Measurement.date >= prev_year).all()
    temps = list(np.ravel(results))
    return jsonify(temps=temps)

#make min, ave, and max temps route
@app.route("/api/v1.0/temp/<start>")
@app.route("/api/v1.0/temp/<start>/<end>")

#stats function
def stats(start=None, end=None):
    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]

    if not end:
        results = session.query(*sel).\
            filter(Measurement.date >= start).all()
        temps = list(np.ravel(results))
        return jsonify(temps)

    results = session.query(*sel).\
        filter(Measurement.date >= start).\
        filter(Measurement.date <= end).all()
    temps = list(np.ravel(results))
    return jsonify(temps)