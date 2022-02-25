'''
A Web application that shows Google Maps around schools, using
the Flask framework, and the Google Maps API.
'''

from flask import Flask, render_template, abort
app = Flask(__name__)


class NetworkLog:
    def __init__(self, ip, country, lat, lng):
        self.ip  = ip
        self.country = country
        self.lat  = lat
        self.lng  = lng

networklogs = (
    NetworkLog('hv',      'Happy Valley Elementary',   37.9045286, -122.1445772),
    NetworkLog('stanley', 'Stanley Middle',            37.8884474, -122.1155922),
    NetworkLog('wci',     'Walnut Creek Intermediate', 37.9093673, -122.0580063)
)
print(networklogs)
networklog_by_key = {networklog.ip: networklog for networklog in networklogs}


@app.route("/")
def index():
    return render_template('index.html', networklogs=networklogs)


@app.route("/<ip_Code>")
def show_school(ip_Code):
    networklog = networklog_by_key.get(ip_Code)
    if networklog:
        return render_template('map.html', networklog=networklog)
    else:
        abort(404)

app.run(host='localhost', debug=True)