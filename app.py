# Import dependencies
import datetime as dt
import numpy as np
import pandas as pd
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify

# Create engine
engine = create_engine("sqlite:///hawaii.sqlite")

# Reflect the database
Base = automap_base()

Base.prepare(engine, reflect=True)

# Save table references
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create session
session = Session(engine)

# Set up Flask
app = Flask(__name__)

# Create routes
@app.route("/")

def welcome():
    return(
    '''
    Welcome to the Climate Analysis API!
    Available Routes:
    /api/v1.0/precipitation
    /api/v1.0/stations
    /api/v1.0/tobs
    /api/v1.0/temp/start/end
    ''')