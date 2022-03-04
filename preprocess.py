# Preprocessing pcap files to csv files
import pcap2csv
import csvprocess
import servcount
import platform

def pcap_to_csv(filename):
    pcap2csv.exec("static/files/input.pcap", platform.platform())
    csvprocess.exec()
    servcount.exec()
    return True
