# -*- coding: utf-8 -*-


import os
import sys

from lxml import etree

from opendriveparser import parse_opendrive

from GraphVisualizer import graphvisualize as gviz

# Input file
path = os.path.dirname(os.path.abspath(__file__)) + sys.argv[1]

#print(path)
with open(path, 'r') as fh:
    parser = etree.XMLParser()
    rootNode = etree.parse(fh, parser).getroot()
    roadNetwork = parse_opendrive(rootNode)

gviz_ = gviz.GraphVisualization()

junc = 0
for road in roadNetwork.roads:
	#print(road.link.neighbors)
	current_name = "r_"+str(road.id)
	if(road.link.predecessor != None):# and road.junction == None):
		if(road.link.predecessor.elementType =="junction"):
			pred_name = "J_"+str(road.link.predecessor.elementId)
			gviz_.addEdge(pred_name, current_name)
		if(road.link.predecessor.elementType =="road"):
			pred_name = "r_"+str(road.link.predecessor.elementId)
			gviz_.addEdge(pred_name, current_name)

	
	if(road.link.successor != None):# and road.junction == None):
		if(road.link.successor.elementType =="junction"):
			succ_name = "J_"+str(road.link.successor.elementId)

		if(road.link.successor.elementType =="road"):
			succ_name = "r_"+str(road.link.successor.elementId)

		gviz_.addEdge(current_name, succ_name)



gviz_.visualize() 

for road in roadNetwork.roads:
	#if(road.link.predecessor.elementType =="road" and road.link.predecessor.elementId ==9 or road.link.successor.elementType =="road" and road.link.successor.elementId ==9 ):
	if(road.junction != None):
		print(road.name)
		print(road.junction)

#for junc in roadNetwork.roads:
#	print(junc.name)
