from flask import Blueprint,render_template
import json
from jinja2 import TemplateNotFound

loader = Blueprint('loader',__name__,template_folder='templates')
@loader.route('/test')
def speak():
	nodes_data = [
    {"id": 1, "label": 'Node 1'},
    {"id": 2, "label": 'Node 2'},
    {"id": 3, "label": 'Node 3'},
    {"id": 4, "label": 'Node 4'},
    {"id": 5, "label": 'Node 5'}
  ]
	edges_data = [
    {"from": 1, "to": 3},
    {"from": 1, "to": 2},
    {"from": 2, "to": 4},
    {"from": 2, "to": 5}
  ]
	nodes_data = json.dumps(nodes_data)
	edges_data = json.dumps(edges_data)
	return render_template('test.html',nodes_data=nodes_data,edges_data = edges_data)
