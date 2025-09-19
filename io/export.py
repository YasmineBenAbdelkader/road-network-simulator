# io/export.py
import json
import csv

def export_to_json(data, filename="results.json"):
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)

def export_to_csv(data, filename="results.csv"):
    if not data:
        return
    roads = list(data[0].keys())
    with open(filename, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=roads)
        writer.writeheader()
        for step in data:
            writer.writerow(step)
