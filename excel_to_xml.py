# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 20:48:18 2024

@author: rangan r
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
    os.makedirs(opdir) #to create output directory if it is not existing already

# Process each Excel file in the input directory
for filename in os.listdir(inpdir):
    if filename.endswith('.xlsx'):
        # Load Excel data
     try:
        df = pd.read_excel(os.path.join(inpdir, filename))

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
     except (PermissionError, OSError, IOError) as e:
           print(f"Error whil reading input file: {e}")

        # Create a tree object and write to file
     try:   
           output_file = os.path.join(opdir, f'{os.path.splitext(filename)[0]}.xml')
           tree = ET.ElementTree(root)
           tree.write(output_file, encoding='utf-8', xml_declaration=True)

           print(f"XML file has been created at {output_file}")
     except (PermissionError, OSError, IOError) as e:
           print(f"Error while creating xml file: {e}")
