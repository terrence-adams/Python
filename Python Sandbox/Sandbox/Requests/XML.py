import xml.etree.ElementTree as ET


def run_xml():
    tree = ET.parse('Lge2467.xml')
    root = tree.getroot()
    print(root.tag)
    for child in root:
        print(child.tag, child.attrib)
        print([elem.tag for elem in root.iter()])


def display_xml():
    tree = ET.parse('Lge2467.xml')
    root = tree.getroot()
    print(ET.tostring(root, encoding='utf-8').decode('utf-8'))


if __name__ ==  '__main__':
    #run_xml()
    display_xml()