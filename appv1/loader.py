from flask import Blueprint,render_template
import json
from jinja2 import TemplateNotFound
from rdfloader import rdfloader

loader = Blueprint('loader',__name__,template_folder='templates')
@loader.route('/test')
def speak():
	
	nodes_data = json.dumps(rdfloader()[0])
	edges_data = json.dumps(rdfloader()[1])
	
	print nodes_data

	return render_template('test.html',nodes_data=nodes_data,edges_data = edges_data)
