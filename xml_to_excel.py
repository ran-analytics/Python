import os
import xml.etree.ElementTree as ET
import pandas as pd

# Read directories from file
with open('xml_dirfile.txt', "r") as dirfile:
    lines = dirfile.readlines()
    inpdir = lines[0].rstrip('\n')
    opdir = lines[1].rstrip('\n')

if not os.path.exists(opdir):
    os.makedirs(opdir)

def parse_element(element, parent_path=''):
    """
    Recursively parse XML elements and build a list of tag-value pairs with fully qualified tags.
    """
    tag_value_pairs = [] #This list will store tuples of tag names and their corresponding text values as we parse the XML elements.
    if element.text and element.text.strip(): #  we only consider non-empty text content.
        tag_value_pairs.append((parent_path + element.tag, element.text.strip()))

    for child in element:
        tag_value_pairs.extend(parse_element(child, parent_path + element.tag + '.'))
        #child is the current child element being processed.
        #parent_path + element.tag + '.' constructs the new parent path for the child element by appending the current element's tag and a dot (.) to the existing parent path
        #parse_element returns a list of tag-value pairs for the child element and its descendants.
    return tag_value_pairs

# Process each XML file in the input directory
for filename in os.listdir(inpdir):
    if filename.endswith('.xml'):
        # Parse the XML file
        tree = ET.parse(os.path.join(inpdir, filename))
        root = tree.getroot()

        # Parse the XML tree into tag-value pairs
        tag_value_pairs = parse_element(root)

        # Convert to DataFrame
        df = pd.DataFrame(tag_value_pairs, columns=['Tag', 'Value'])

        # Write DataFrame to Excel
        output_file = os.path.join(opdir, f'{os.path.splitext(filename)[0]}.xlsx')
        df.to_excel(output_file, index=False)

        print(f"Excel file has been created at {output_file}")