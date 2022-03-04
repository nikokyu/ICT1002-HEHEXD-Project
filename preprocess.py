# Preprocessing pcap files to csv files
import pcap2csv
import csvprocess
import servcount

def pcap_to_csv(filename):
    pcap2csv.exec("static/files/input.pcap", "mac")
    csvprocess.exec()
    servcount.exec()
    return True;
