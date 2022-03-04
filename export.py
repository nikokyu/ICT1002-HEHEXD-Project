import csv
import os


def exportCSV(networklogs):
    path = "static/files/export.csv"

    header = ['srcip', 'sport', 'dstip', 'dport', 'hostname', 'country', 'lat', 'lng', 'org', 'attack']

    if os.path.exists(path):
        os.remove(path)

    with open(path, 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)

        # write the header
        writer.writerow(header)

        # write the data
        for networklog in networklogs:
            data = [networklog.srcip, networklog.sport, networklog.dstip, networklog.dport, networklog.hostname, networklog.country, networklog.lat, networklog.lng, networklog.org, networklog.attack]
            writer.writerow(data)
