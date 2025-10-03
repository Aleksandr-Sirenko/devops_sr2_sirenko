from abc import ABC, abstractmethod
import json
import xml.etree.ElementTree as ET
import csv

class DataSaver(ABC):
    @abstractmethod
    def save(self, data, filename):
        pass

class JsonSaver(DataSaver):
    def save(self, data, filename):
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)

class XmlSaver(DataSaver):
    def save(self, data, filename):
        root = ET.Element('student_data')
        for key, value in data.items():
            if isinstance(value, list):
                sub_elem = ET.SubElement(root, key)
                for item in value:
                    item_elem = ET.SubElement(sub_elem, 'item')
                    item_elem.text = str(item)
            else:
                elem = ET.SubElement(root, key)
                elem.text = str(value)
        tree = ET.ElementTree(root)
        tree.write(filename, encoding='utf-8', xml_declaration=True)

class CsvSaver(DataSaver):
    def save(self, data, filename):
        with open(filename, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            for key, value in data.items():
                writer.writerow([key, value])