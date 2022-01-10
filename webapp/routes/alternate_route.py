from flask import render_template, request, jsonify, Blueprint


alternate_route = Blueprint('alternate_route', __name__)
#alternate_route = Blueprint('alternate_route', __name__, url_prefix='/api')
@alternate_route.route('/secret')
def home_page():
    return "You found secret page"
