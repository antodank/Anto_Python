import xml.etree.ElementTree as ET
from pprint import pprint
from xml.etree.ElementTree import fromstring, Element

tree = ET.parse('data1.xml')

def ReadXML():
	print('Calling ReadXML()')
	root = tree.getroot()
	# one specific item attribute
	#pprint(root)
	#print(root.tag)
	#print(root.attrib)
		
def AddXMLNode(ParentNode,ChildNode):
	print('Calling AddXMLNode()')
	nodearray = ParentNode.split(':')
	delem = '/'
	searchNode = delem.join(nodearray)
	print(searchNode)
	for elem in tree.iterfind('doc/bjghug'):
		print('hi')
		if elem is None:
			print('Invalid Parent')
			return
		else:
			elem.append(Element(ChildNode,{'name': 'bluescannerappTypeEndpoint4','Port':"20004"}))
			print('child Added')

	#tree.write('data1.xml')
	#print('AddXMLNode Done')
	
		
def main():
	print('Calling Main()')
	#ReadXML()
	AddXMLNode('doc:branch','sub-branch1')
	
main()