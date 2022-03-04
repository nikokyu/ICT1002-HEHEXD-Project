import csv
import os


def exportCSV(networklogs):
    path = "static/download/output.csv"

    header = ['ip', 'hostname', 'country', 'lat', 'lng', 'org', 'attack']

    os.remove(path)

    with open(path, 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)

        # write the header
        writer.writerow(header)

        # write the data
        for networklog in networklogs:
            data = [networklog.ip, networklog.hostname, networklog.country, networklog.lat, networklog.lng, networklog.org, networklog.attack]
            writer.writerow(data)
