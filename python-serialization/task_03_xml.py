#!/usr/bin/python3
"""Serializing and Deserializing with XML module."""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """Serialize a Python dictionary into XML and save it to a file."""
    root = ET.Element("data")

    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)

    tree = ET.ElementTree(root)
    tree.write(filename, encoding="utf-8", xml_declaration=True)


def deserialize_from_xml(filename):
    """Read XML data from a file and return a deserialized Python dictionary."""
    try:
        tree = ET.parse(filename)
        root = tree.getroot()

        return {child.tag: child.text for child in root}
    except Exception:
        return None
