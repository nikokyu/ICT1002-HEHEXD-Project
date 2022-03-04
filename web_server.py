from flask import Flask, render_template, jsonify, request, Response, redirect, url_for, abort, session, send_file
import argparse
import sys
import json
import gevent
import gevent.monkey
import pandas as pd
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
import getAttackCounterDictionary
import getCountryDictionary

global networklogs
global networklog_by_key
global dictAttack
global dictCountry

# For pagination
class PageResult:
   def __init__(self, data, page = 1, number = 15):
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
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], "input.pcap")
        # set the file path
        uploaded_file.save(file_path)
        # save the file
        return redirect(url_for('processing'))
    else:
        return redirect(url_for('/'))


###################### Upload Page END ############################################################


###################### Processing #################################################################
@app.route("/processing")
def processing():
    # do all processing here
    global networklogs
    global networklog_by_key
    global dictAttack
    global dictCountry
    networklogs = []
    dictIP = {}
    # Preprocess data, output to static/files/out.csv
    preprocess.pcap_to_csv("static/files/input.pcap")
    # Feed into AI model
    dataset = ai_process.predict("static/files/out.csv")
    # Drop rows with non attack
    dataset = dataset.drop(dataset[dataset.attackcat == "Normal"].index)
    # Feed into IP api
    ipaddrs = list(set(dataset['srcip'].values.tolist()))
    for ip in ipaddrs:
        dictIP[ip] = ip_process.geolocation(ip)
    # generate networklogs
    i = 0
    for index, row in dataset.iterrows():
        dict = dictIP[row['srcip']]
        networklogs.append(NetworkLog(str(i), row['srcip'], row['sport'], row['dstip'], row['dport'], dict['hostname'],
        dict['country'], dict['lat'], dict['lng'], dict['org'], row['attackcat']))
        i += 1
    networklog_by_key = {networklog.key: networklog for networklog in networklogs}
    dictAttack = getAttackCounterDictionary.getAttack(networklogs)
    dictCountry = getCountryDictionary.getCountry(networklogs)
    # Go to home page
    return redirect(url_for('home', pagenum=1))
###################### Processing End #############################################################
###################### Main Page ################################################################

# @app.route("/home")
# def home1():
#     return render_template('home.html', networklogs=networklogs)

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
    return render_template('heatmap.html', networklogs=networklogs, dictCountry = dictCountry, dictAttack = dictAttack)

@app.route('/home/heatmap/download')
def download():
    path = "static/files/export.csv"
    export.exportCSV(networklogs)
    return send_file(path , as_attachment=True)

###################### Main Page End############################################################

app.route('/end')
def end():
    # cleanup when end
    global networklogs
    global networklog_by_key
    global dictAttack
    global dictCountry
    networklogs = []
    networklog_by_key = {}
    dictAttack = {}
    dictCountry = {}
    redirect(url_for('/'))


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
