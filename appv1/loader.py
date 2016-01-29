from flask import Blueprint
loader = Blueprint('loader',__name__)

@loader.route('/test')
def speak():
	return "it works"
