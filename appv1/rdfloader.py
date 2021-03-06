import rdflib
from rdflib import BNode,URIRef,Literal
g = rdflib.Graph()

def getURIRefLabel(obj):
	obj = obj
	if "#" in obj:
		return obj[:obj.rfind("#")]
	else:
		if obj[len(obj)-1] == "/":
			obj = obj[:len(obj)-1]
		return obj[obj.rfind("/")+1:]

def getIdentifier(obj):
	tobj = type(obj)
	if tobj == URIRef:
		return tobj,getURIRefLabel(obj)
	else:
		return tobj,obj

def rdfloader():
	nodes_exist = []
	nodes = []
	edges = []
	g.parse("/home/noor/Documents/repositories/github/rdf_visualizer/appv1/file.rdf",format="nt")
	for subj, pred, obj in g:
		objs = [subj,obj]
		for term in objs:
			str_term = term
			if str_term not in nodes_exist:
				obj_node = {}	
				nodes_exist.append(str_term)
				node_info = getIdentifier(term)
				obj_node["id"] = str_term
				obj_node["label"] = node_info[1]
				if node_info[0] == Literal:
					obj_node["shape"] = "box";
				nodes.append(obj_node)		
		
		#getting predicates info
		pred_label = getURIRefLabel(pred)		
		
		edge = {"from":subj,"to":obj,"label":pred_label}
		
		edge["arrows"] = "to"
		edges.append(edge)

	return nodes,edges

