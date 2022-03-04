import csv, os, socket


csv_file = "output.csv"
headers = ["frame number","srcip","sport","dstip","dport","proto","service","tcp flag","frame length","TTL","window size","Duration","ignored"]

if os.path.exists("out.csv"):
    os.remove("out.csv")

with open("out.csv","w",newline='', encoding='utf-8') as g:
        csv_writer = csv.writer(g)
        csv_writer.writerow(headers)



def write(row):
    with open("out.csv","a",newline='', encoding='utf-8') as g:
        csv_writer = csv.writer(g)
        csv_writer.writerow(row)

with open(csv_file, 'r') as f:
    csv_reader = csv.reader(f)
    header = next(csv_reader)
    if header != None:
        for row in csv_reader:

            #for frame number
            frame_num = row[0].split(":")
            row[0] = frame_num[0]

            #for ip protocol
            protocols = row[6].split(":")
            row[5] = protocols[3]

            #for service 
            try:
                row[6] = socket.getservbyport(int(row[2]),row[5])
            except:
                try:
                    row[6] = socket.getservbyport(int(row[4]),row[5])
                except:
                    row[6] = ""
            
            
            #for tcp flag
            if row[7]!="": 
                row[7] = int(row[7],0)
            else:
                row[7] = 0

            #for window size
            if row[10] == "":
                row[10] = 0

            #for duration
            row[11] = float(row[14])

            #ignored values
            row[12] = row[13]

            #empty the rest
            row[13:] = ""
            write(row)
            
