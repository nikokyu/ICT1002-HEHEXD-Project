from flask import Flask, render_template, jsonify, request, Response, redirect, url_for, abort, session, send_file
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
import preprocess
import ip_process
import ai_process
from networklog import NetworkLog
import secrets
import export

class PageResult:
   def __init__(self, data, page = 1, number = 3):
     self.__dict__ = dict(zip(['data', 'page', 'number'], [data, page, number]))
     self.full_listing = [self.data[i:i+number] for i in range(0, len(self.data), number)]
   def __iter__(self):
     for i in self.full_listing[self.page-1]:
       yield i
   def __repr__(self): #used for page linking
     return "/home/page/{}".format(self.page+1) #view the next page

app = Flask(__name__)
# For uploading files
# enable debugging mode
app.config["DEBUG"] = True

# Upload folder
app.config['UPLOAD_FOLDER'] =  'static/files'
app.config['SECRET_KEY'] =  secrets.token_hex(16)

# To be confirmed on the final iteration
# Leave all the code here for after backend is done ****
#networklog_by_key = {networklog.key: networklog for networklog in networklogs}
#networklog_by_attack = {networklog.attack: networklog for networklog in networklogs}
#networklogAttack = []
#networklogHTML = []
#for i in networklogs:
    #if i.attack not in networklogAttack:
        #networklogAttack.append(i.attack)
#longest = range(len(networklogs))
#zipped = zip_longest(networklogs, networklogAttack, longest, fillvalue='?')
#for i in zipped:
    #networklogHTML.append(i)

# temporary only
networklogs = [
    NetworkLog('0', '192.168.10.21', 'example.com', 'Singapore',   37.9045286, -122.1445772, 'org', 'Ransomware'),
    NetworkLog('1', '192.167.21.21', 'example.com', 'Malaysia', 37.8884474, -122.1155922, 'org', 'Ransomware'),
    NetworkLog('2', '1.23.12.1', 'example.com', 'Japan', 25.9093673, -126.0580063, 'org', 'Ddos'),
    NetworkLog('3', '192.167.21.25', 'example.com', 'Korea', 1.43801, 103.789, 'org', 'Ddos'),
    NetworkLog('0', '192.168.10.21', 'example.com', 'Singapore',   37.9045286, -122.1445772, 'org', 'Ransomware'),
    NetworkLog('1', '192.167.21.21', 'example.com', 'Malaysia', 37.8884474, -122.1155922, 'org', 'Ransomware'),
    NetworkLog('2', '1.23.12.1', 'example.com', 'Japan', 25.9093673, -126.0580063, 'org', 'Ddos'),
    NetworkLog('3', '192.167.21.25', 'example.com', 'Korea', 1.43801, 103.789, 'org', 'Ddos'),
    NetworkLog('0', '192.168.10.21', 'example.com', 'Singapore',   37.9045286, -122.1445772, 'org', 'Ransomware'),
    NetworkLog('1', '192.167.21.21', 'example.com', 'Malaysia', 37.8884474, -122.1155922, 'org', 'Ransomware'),
    NetworkLog('2', '1.23.12.1', 'example.com', 'Japan', 25.9093673, -126.0580063, 'org', 'Ddos'),
    NetworkLog('3', '192.167.21.25', 'example.com', 'Korea', 1.43801, 103.789, 'org', 'Ddos'),
    NetworkLog('0', '192.168.10.21', 'example.com', 'Singapore',   37.9045286, -122.1445772, 'org', 'Ransomware'),
    NetworkLog('1', '192.167.21.21', 'example.com', 'Malaysia', 37.8884474, -122.1155922, 'org', 'Ransomware'),
    NetworkLog('2', '1.23.12.1', 'example.com', 'Japan', 25.9093673, -126.0580063, 'org', 'Ddos'),
    NetworkLog('3', '192.167.21.25', 'example.com', 'Korea', 1.43801, 103.789, 'org', 'Ddos'),
    NetworkLog('0', '192.168.10.21', 'example.com', 'Singapore',   37.9045286, -122.1445772, 'org', 'Ransomware'),
    NetworkLog('1', '192.167.21.21', 'example.com', 'Malaysia', 37.8884474, -122.1155922, 'org', 'Ransomware'),
    NetworkLog('2', '1.23.12.1', 'example.com', 'Japan', 25.9093673, -126.0580063, 'org', 'Ddos'),
    NetworkLog('3', '192.167.21.25', 'example.com', 'Korea', 1.43801, 103.789, 'org', 'Ddos'),
]
# Example IP API process
ip_list = [['1.1.1.1',"Ddos"], ['2.2.2.2', "Ransomware"], ['3.3.3.3', "WannaCry"], ['4.4.4.4', "WannaDie"]]
i = 4
for ip in ip_list:
    geo_dict = ip_process.geolocation(ip[0])
    networklogs.append(NetworkLog(str(i), ip[0], geo_dict['hostname'], geo_dict['country'], geo_dict['lat'], geo_dict['lng'], geo_dict['org'], ip[1]))
    i = i+1

networklog_by_key = {networklog.key: networklog for networklog in networklogs}

###################### Upload Page ################################################################
@app.route("/" )
def upload():
    return render_template('index.html')

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

      return redirect(url_for('processing'))

###################### Upload Page END ############################################################


###################### Processing #################################################################
@app.route("/processing")
def processing():
    # do all processing here
    # Preprocess data
    # Feed into IP api
    # Feed into AI model
    # Generate CSV
    # Return networklogs and go to home page

    print(ip_process.geolocation("223.25.69.206"))
    return redirect(url_for('home', pagenum=1))
###################### Processing End #############################################################
###################### Main Page ################################################################
#@app.route("/home")
#def home():
    #return render_template('home.html', networklogs=networklogs)

@app.route("/home/page/<int:pagenum>")
def home(pagenum):
    return render_template('home.html', listing = PageResult(networklogs, pagenum))

@app.route("/home/networklog/<keycode>")
def info(keycode):
    networklog = networklog_by_key.get(keycode)
    if networklog:
        return render_template('info.html', networklog=networklog)
    else:
        abort(404)

@app.route("/home/heatmap")
def heatmap():
    return render_template('heatmap.html', networklogs=networklogs)

@app.route('/home/download')
def download():
    path = "static/download/output.csv" 
    export.exportCSV(networklogs)
    return send_file(path , as_attachment=True)

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
