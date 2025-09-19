# io/export.py
import json
import csv

def export_to_json(data, filename="results.json"):
    """
    Exporte les résultats de l'analyse en fichier JSON
    """
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)

def export_to_csv(data, filename="results.csv"):
    """
    Exporte les résultats de l'analyse en fichier CSV
    Chaque ligne = step, colonnes = routes avec avg_speed
    """
    if not data:
        print("No data to export")
        return

    roads = list(data[0].keys())
    # on n'exporte que la vitesse moyenne pour simplifier
    with open(filename, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=roads)
        writer.writeheader()
        for step in data:
            writer.writerow({road: step[road]["avg_speed"] for road in roads})
