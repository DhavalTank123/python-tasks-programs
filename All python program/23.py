'''Given a xml file(sample.xml) print out all the files and folders hierarchically.
 Take the filename as an argument. Use OOPS concepts.
 Python script should contain class and all the required definitions should be defined within that class.
(\\10.0.1.22\CrestData\UserData\Jay Joshi\Python handson\demo.xml)
'''
import sys
import xml.etree.ElementTree as ET

class XMLHierarchyParser:
    def __init__(self, filename):
        self.filename = filename
        self.tree = ET.parse(filename)
        self.root = self.tree.getroot()

    def print_hierarchy(self, element=None, level=0):
        if element is None:
            element = self.root

        indent = ' ' * (level * 2)
        print(f"{indent}{element.tag}: {element.attrib.get('name', '')}")

        for child in element:
            self.print_hierarchy(child, level + 1)

    def run(self):
        self.print_hierarchy()

if __name__ == "__main__":
  

    if len(sys.argv) != 2:
        print("Usage: python script.py <sample.xml>")
        sys.exit(1)

    filename = sys.argv[1]
    parser = XMLHierarchyParser(filename)
    parser.run()
