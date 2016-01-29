from flask import Blueprint,render_template
from jinja2 import TemplateNotFound
loader = Blueprint('loader',__name__,template_folder='templates')

@loader.route('/test')
def speak():
	return render_template('test.html')
