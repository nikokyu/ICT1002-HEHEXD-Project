from flask import Flask, render_template, jsonify, request,Response, redirect, url_for, abort
import argparse
import sys
import json
import gevent
import gevent.monkey
from gevent.pywsgi import WSGIServer
from datetime import datetime
from itertools import zip_longest
gevent.monkey.patch_all()
import os
from os.path import join, dirname, realpath
import time
import geocoder




app = Flask(__name__)


class NetworkLog:
    def __init__(self, key, ip, country, lat, lng, attack, city, hostname, org):
        self.key = key
        self.ip  = ip
        self.country = country
        self.lat  = lat
        self.lng  = lng
        self.attack = attack
        self.city = city
        self.hostname = hostname
        self.org = org
        

sample_nested_list = [['198.71.247.91', 'ddos'],['8.8.8.8', 'malware'],['116.87.77.81', 'ddos'], ['104.103.236.5', 'ok']]
key = 0
networklogs = []
for log in sample_nested_list:
    attack = log[1]
    ip = log[0]
    g = geocoder.ip(ip)
    lat = g.lat
    lng = g.lng
    country = g.country
    hostname = g.hostname
    org = g.org
    city = g.city
    keyStr=str(key)
    networklogs.append(NetworkLog(keyStr, ip, country, lat, lng, attack, city, hostname, org))
    key+=1



'''
networklogs = [
    NetworkLog('0', '192.168.10.21',      'Singapore',   37.9045286, -122.1445772, 'Ransomware'),
    NetworkLog('1', '192.167.21.21', 'Malaysia', 37.8884474, -122.1155922, 'Ransomware'),
    NetworkLog('2', '1.23.12.1',     'Japan', 25.9093673, -126.0580063, 'Ddos'),
    NetworkLog('3', '192.167.21.25', 'Korea', 1.43801, 103.789, 'Ddos'),
]
'''

# To be confirmed on the final iteration
# Leave all the code here for after backend is done ****
networklog_by_key = {networklog.key: networklog for networklog in networklogs}
networklog_by_attack = {networklog.attack: networklog for networklog in networklogs}
networklogAttack = []
networklogHTML = []
for i in networklogs:
    if i.attack not in networklogAttack:
        networklogAttack.append(i.attack)
longest = range(len(networklogs))
zipped = zip_longest(networklogs, networklogAttack, longest, fillvalue='?')
for i in zipped:
    networklogHTML.append(i)




# For uploading files
# enable debugging mode
app.config["DEBUG"] = True

# Upload folder
UPLOAD_FOLDER = 'static/files'
app.config['UPLOAD_FOLDER'] =  UPLOAD_FOLDER


###################### Upload Page ################################################################
@app.route("/" )
def upload():
    return render_template('upload.html')

# Get the uploaded files
@app.route("/", methods=['POST'])
def uploadFiles():
      # get the uploaded file
      uploaded_file = request.files['file']
      if uploaded_file.filename != '':
           file_path = os.path.join(app.config['UPLOAD_FOLDER'], uploaded_file.filename)
          # set the file path
           uploaded_file.save(file_path)
          # save the file

      return redirect(url_for('home'))

###################### Upload Page END ############################################################

###################### Main Page ################################################################
@app.route("/home")
def home():
    return render_template('index.html', networklogs=networklogHTML)


@app.route("/home/<keycode>")
def homeShowDetails(keycode):
    networklog = networklog_by_key.get(keycode)
    if networklog:
        return render_template('info.html', networklog=networklog)
    else:
        abort(404)


###################### Main Page End############################################################





if __name__ == '__main__':
   try:

        host = '0.0.0.0'
        port = 80
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
