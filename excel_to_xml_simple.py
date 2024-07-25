# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 20:48:18 2024

@author: sys-user
"""

import os
import xml.etree.ElementTree as ET
import pandas as pd

# Read directories from file
with open('xls_dirfile.txt', "r") as dirfile:
    lines = dirfile.readlines()
    inpdir = lines[0].rstrip('\n')
    opdir = lines[1].rstrip('\n')

if not os.path.exists(opdir):
    os.makedirs(opdir)

# Load Excel data
df = pd.read_excel(os.path.join(inpdir, 'poc.xlsx'))  # Replace 'data.xlsx' with your Excel file name

# Create the root element
root = ET.Element("root")

# Build XML tree from DataFrame
for _, row in df.iterrows():
    tags = row[0].split('.')
    value = row[1]

    # Create XML elements
    parent = root
    for tag in tags:
        # Check if the tag already exists
        child = parent.find(tag)
        if child is None:
            child = ET.SubElement(parent, tag)
        parent = child
    parent.text = str(value)

# Create a tree object and write to file
tree = ET.ElementTree(root)
output_file = os.path.join(opdir, 'output.xml')  # Change 'output.xml' if needed
tree.write(output_file, encoding='utf-8', xml_declaration=True)

print(f"XML file has been created at {output_file}")
