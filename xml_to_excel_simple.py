# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 22:38:01 2024

@author: sys-user
"""

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

# Load XML data
input_file = os.path.join(inpdir, 'customer.xml')  # Replace 'input.xml' with your XML file name
tree = ET.parse(input_file)
root = tree.getroot()

# Function to extract XML data
def extract_data(element, path=''):
    data = []
    for child in element:
        new_path = f"{path}.{child.tag}" if path else child.tag
        if len(child):
            data.extend(extract_data(child, new_path))
        else:
            data.append((new_path, child.text))
    return data

# Extract data from XML
data = extract_data(root)

# Convert data to DataFrame
df = pd.DataFrame(data, columns=['Element', 'Value'])

# Save DataFrame to Excel
output_file = os.path.join(opdir, 'output.xlsx')  # Change 'output.xlsx' if needed
df.to_excel(output_file, index=False)

print(f"Excel file has been created at {output_file}")
