import xml.etree.ElementTree as ET

xml_data = ""
for _ in range(int(input())):
    xml_data += input()
    xml_data += "\n"

# Parse XML
root = ET.fromstring(xml_data)
score = 0
for elem in root.iter():
    score += len(elem.attrib)

print(score)