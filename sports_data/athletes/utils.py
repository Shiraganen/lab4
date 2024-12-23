import os
import json
import xml.etree.ElementTree as ET
from django.core.exceptions import ValidationError

def save_json_to_folder(data, folder_path, filename):
    filepath = os.path.join(folder_path, filename)
    with open(filepath, 'w') as f:
        json.dump(data, f, indent=4)

def save_xml_to_folder(data, folder_path, filename):
    root = ET.Element("athletes")
    for athlete in data:
        athlete_el = ET.SubElement(root, "athlete")
        for key, value in athlete.items():
            ET.SubElement(athlete_el, key).text = str(value)
    tree = ET.ElementTree(root)
    filepath = os.path.join(folder_path, filename)
    tree.write(filepath, encoding='utf-8', xml_declaration=True)

def validate_json_file(filepath):
    try:
        with open(filepath, 'r') as f:
            json.load(f)
        return True
    except json.JSONDecodeError:
        return False

def validate_xml_file(filepath):
    try:
        ET.parse(filepath)
        return True
    except ET.ParseError:
        return False
