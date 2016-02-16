import rdflib
from rdflib import BNode
g = rdflib.Graph()
def rdfloader():
	g.parse("/home/noor/Documents/repositories/github/rdf_visualizer/appv1/file.rdf",format="nt")
	for subj, pred, obj in g:
		print str(subj)
		print str(pred)
		print str(obj)
rdfloader()
