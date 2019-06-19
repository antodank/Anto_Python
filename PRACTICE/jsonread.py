import json, csv, sys
import xml.etree.ElementTree as ET
from pprint import pprint
from xml.etree.ElementTree import fromstring, Element

#pkg\myappPkg\ServiceManifest.xml
#class automation:
# tree = None             
	#datastore = None
    #def __init__(self, JSONpath,serviceXMLpath):
     #   self.JSONpath = JSONpath
		#self.serviceXMLpath = serviceXMLpath
	
	#def ReadFile(JSONpath,serviceXMLpath)
	
# Applicationtree = ET.parse('Release\pkg\ApplicationManifest.xml')
# Servicetree = ET.parse('pkg\myappPkg\ServiceManifest.xml')
# data_storage = json.load(open('json\example.json'))
tree = None

def ReadJson():
	print('Calling ReadJson()')
	#pprint(data)
	for obj in data.keys():
		for obj1 in (data[obj].values()).keys():
			print(obj1.values())
			
def ReadCSV():
	filename = 'json\servicemanifest.csv'
	input_file = csv.DictReader(open(filename))
	for row in input_file:
		ColTemplate = str(row["ColTemplate"])
		ColType = str(row["ColType"])
		ColPNode = str(row["ColPNode"])
		ColCNode = str(row["ColCNode"])
		ColVal = str(row["ColVal"])
		
		if "Service" in ColTemplate:
			tree = ET.parse('pkg\myappPkg\ServiceManifest.xml')
		elif "Application" in ColTemplate:
			tree = ET.parse('Release\pkg\ApplicationManifest.xml')
		else:
			print('Tree Error')
			
		if ColType == 'NodeValue':
			SetXMLNodeValue(ColPNode,ColCNode,ColVal)
		elif ColType == 'NodeText':
			SetXMLNodeText(ColPNode,ColVal)
		elif ColType == 'Node':
			AddXMLNode(ColPNode,ColCNode)
			SetXMLNodeValue(ColPNode,ColCNode,ColVal)
		else:
			print('ColType Error')
			
		
	print('ReadCSV Done')
	
def ReadXML():
	print('Calling ReadXML()')
	root = tree.getroot()
	# one specific item attribute
	print(root.tag)
	print(root.attrib)
		
def AddXMLNode(ParentNode,ChildNode):
	print('Calling UpdateXML()')
	for elem in tree.iterfind(ParentNode):
		elem.append(Element('Endpoint',{'name': 'bluescannerappTypeEndpoint4','Port':"20004", 'Protocol':'http', 'UriScheme':'http'}))
		#elem.append(Element(ChildNode))
		print('Added')
		
	tree.write('pkg\myappPkg\ServiceManifest.xml')
	print('AddXMLNode Done')
	
def SetXMLNodeText(node,textval):
	for elem in root.iter(node):
		elem.text = str(textval)
		
def SetXMLNodeValue(node,nodeatr,nodeval):
	for elem in root.iter(node):
		elem.set('updated', 'yes')
		
def main():
	print('Calling Main()')
	#ReadCSV()
	AddXMLNode('Resources\Endpoints','Endpoint')
main()