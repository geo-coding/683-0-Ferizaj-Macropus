import os
import xml.etree.ElementTree as ET

# Specify the directory containing the XML files
directory = "d:/Ferizaj/Ferizaj/Kadastrale/683-0-Ferizaj-Macropus/per-ne/src/"

# Create an empty Element object to hold the merged data
merged_data = ET.Element("merged_data")

# Loop through all the XML files in the directory
for filename in os.listdir(directory):
    if filename.endswith(".xml"):
        # Parse the XML file and get the root element
        #tree = ET.parse(os.path.join(directory, filename))
        tree = ET.parse(os.path.join(different,filename))
        root = tree.getroot()
        
        # Append all the child elements to the merged_data element
        for child in root:
            merged_data.append(child)

# Write the merged data to a new XML file
merged_tree = ET.ElementTree(merged_data)
merged_tree.write("merged.xml")
"""
In this example, we first specify the directory containing the XML files. Then,
we create an empty Element object called merged_data that will hold the merged
data from all the XML files.

Next, we loop through all the XML files in the directory using the os.listdir()
function. For each file, we parse it using ET.parse(), and get the root element
using tree.getroot().

We then loop through all the child elements of the root element, and append them
to the merged_data element using the append() method.

Finally, we write the merged data to a new XML file called "merged.xml" using
the ET.ElementTree() constructor and the write() method.

Note that this code assumes that all the XML files have the same structure and
use the same root element. If this is not the case, you may need to modify the
code to handle different XML 
"""
