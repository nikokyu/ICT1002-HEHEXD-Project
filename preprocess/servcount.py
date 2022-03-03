import pandas


df = pandas.read_csv("out.csv")
service = df.service.to_list()
source_ip = df["source ip"].to_list()
dest_ip = df["dest ip"].to_list()
source_port = df["source port"].to_list()
dest_port = df["dest port"].to_list()
ip_service_source = list()
ip_service_dest = list()
dest_sport = list()

def count100(x):
    dict = {}
    for i in x: 
        if i not in dict:
            dict[i] = 1
        else:
            dict[i] += 1
    return dict

def repeat(ip_service):
    chunked_list = list()   
    chunk_size = 100

    for i in range(len(ip_service)):
        ip_service[i] = tuple(ip_service[i])

    for i in range(0,len(ip_service),chunk_size):
        chunked_list.append(ip_service[i:i+chunk_size])

    full_list = list()

    for i in range(len(chunked_list)):
        dict_temp = count100(chunked_list[i])
        full_list += [*map(dict_temp.get, chunked_list[i])]
    return full_list





for i in range(len(service)):
    ip_service_source.append([source_ip[i],service[i]])

for i in range(len(service)):
    ip_service_dest.append([dest_ip[i],service[i]])

for i in range(len(service)):
    dest_sport.append([dest_ip[i],source_port[i]])

full_list = repeat(ip_service_source)
df["count_svc_src"] = full_list
full_list = repeat(ip_service_dest)
df["count_svc_dest"] = full_list
full_list = repeat(source_ip)
df["count_src"] = full_list
full_list = repeat(dest_sport)
df["count_dest_sport"] = full_list
df.to_csv("out.csv")
