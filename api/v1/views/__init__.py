#!/usr/bin/python3
"""sharing app_views Blueprint"""

from flask import Blueprint
from api.v1.views.index import app_views
app_views = Blueprint('app_views', __name__)
from api.v1.views.users import *
from api.v1.views.amenities import *
from api.v1.views.cities import *
from api.v1.views.states import *
