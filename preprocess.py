# Preprocessing pcap files to csv files
import pcap2csv
import csvprocess
import servcount

def pcap_to_csv(filename):
    pcap2csv.exec("static/files/input.pcap", "win")
    csvprocess.exec()
    servcount.exec()
    return True;
