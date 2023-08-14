# this is where users can actually go to
from flask import Blueprint # So that we don't have views all in one file but split up in multiple files

views = Blueprint('views', __name__)

@views.route('/') # this is our main page
def home(): 
    return "<h1>Test</h1>"

