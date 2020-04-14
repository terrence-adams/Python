import requests
import json
import xml.etree.ElementTree as ET


class DNARequestAlpha:

    def load_xml(self):
        tree = ET.parse('whoisreq.xml')
        root = tree.getroot()
        print(root.attrib)
        print(root)
        if tree != None:
           for e in tree.iter():
               print(e)




if __name__ == '__main__':
    dna = DNARequestAlpha()
    dna.load_xml()