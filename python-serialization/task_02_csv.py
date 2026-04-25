#!/usr/bin/python3
"""Converting CSV Data to JSON Format module."""
import csv
import json


def convert_csv_to_json(csv_filename):
    """Convert a CSV file to a JSON file."""
    try:
        data_list = []
        with open(csv_filename, mode="r", encoding="utf-8") as csv_f:
            csv_reader = csv.DictReader(csv_f)
            for row in csv_reader:
                data_list.append(row)

        with open("data.json", mode="w", encoding="utf-8") as json_f:
            json.dump(data_list, json_f)

        return True
    except FileNotFoundError:
        return False
    except Exception:
        return False
