import xml.etree.ElementTree as ET

def parse_xml(xml_string):
    # Parse XML string to ElementTree
    root = ET.fromstring(xml_string)

    # Iterate over each child element
    for child in root:
        print(f'Element: {child.tag}, Attributes: {child.attrib}, Text: {child.text}')

# Test the function
xml_string = """
<root>
    <element1 attr="value">Text1</element1>
    <element2 attr="value">Text2</element2>
</root>
"""
parse_xml(xml_string)