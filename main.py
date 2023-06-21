import xml.etree.ElementTree as ET

# Load and parse the input KML file
tree = ET.parse('input.kml')
root = tree.getroot()

# Extract the namespace from the root element (we'll need this to find elements)
ns = {'kml': 'http://www.opengis.net/kml/2.2'}

# Find the coordinates element in the input file
coordinates = root.find('.//kml:coordinates', ns)

# Create the output KML file structure
kml = ET.Element('kml', {'xmlns': 'http://www.opengis.net/kml/2.2'})
doc = ET.SubElement(kml, 'Document')

style = ET.SubElement(doc, 'Style', {'id': 'transBluePoly'})
line_style = ET.SubElement(style, 'LineStyle')
ET.SubElement(line_style, 'width').text = '1.5'
poly_style = ET.SubElement(style, 'PolyStyle')
ET.SubElement(poly_style, 'color').text = '7dff0000'

placemark = ET.SubElement(doc, 'Placemark')
ET.SubElement(placemark, 'name').text = 'QGISexport'
ET.SubElement(placemark, 'styleUrl').text = '#transBluePoly'

polygon = ET.SubElement(placemark, 'Polygon')
ET.SubElement(polygon, 'extrude').text = '1'
ET.SubElement(polygon, 'altitudeMode').text = 'relativeToGround'
outer_boundary = ET.SubElement(polygon, 'outerBoundaryIs')
linear_ring = ET.SubElement(outer_boundary, 'LinearRing')

# Copy the coordinates from the input file to the output file
linear_ring.append(coordinates)

# Write the output KML file
tree = ET.ElementTree(kml)
tree.write('output.kml', encoding='utf-8', xml_declaration=True)