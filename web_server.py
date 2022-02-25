from flask import Flask, render_template, jsonify, request,Response
import argparse
import sys
import json
import gevent
import gevent.monkey
from gevent.pywsgi import WSGIServer
from datetime import datetime
from itertools import zip_longest
gevent.monkey.patch_all()



app = Flask(__name__)



class NetworkLog:
    def __init__(self, key, ip, country, lat, lng):
        self.key = key
        self.ip  = ip
        self.country = country
        self.lat  = lat
        self.lng  = lng

networklogs = (
    NetworkLog('0', '192.168.10.21',      'Singapore',   37.9045286, -122.1445772),
    NetworkLog('1', '192.167.21.21', 'Malaysia', 37.8884474, -122.1155922),
    NetworkLog('2', '1.23.12.1',     'Japan', 25.9093673, -126.0580063),
    NetworkLog('3', '192.167.21.212131', 'Korea', 1.43801, 103.789),

)
networklog_by_key = {networklog.country: networklog for networklog in networklogs}


networklogCountry = []
networklogHTML = []
for i in networklogs:
    if i.country not in networklogCountry:
        networklogCountry.append(i.country)



longest = range(len(networklogs))
zipped = zip_longest(networklogs, networklogCountry, longest, fillvalue='?')

for i in zipped:
    networklogHTML.append(i)



@app.route("/")
def home():
    return render_template('index.html', networklogs=networklogHTML)

@app.route("/upload")
def upload():
    return render_template('index2.html', networklogs=networklogHTML)



if __name__ == '__main__':
   try:

        host = '0.0.0.0'
        port = 8000
        parser = argparse.ArgumentParser()        
        parser.add_argument('port',type=int)
        
        args = parser.parse_args()
        if args.port:
            port = args.port
                
        http_server = WSGIServer((host, port), app)
        app.debug = True
        http_server.serve_forever()
   except:
        print("Exception while running web server")
        print(sys.exc_info()[0])
        print(sys.exc_info()[1])
