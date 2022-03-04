# ip to geolocation
#from cmath import e
#import re
#from urllib.error import HTTPError
#import urllib.request
#from urllib.request import Request, urlopen
#from urllib.error import URLError, HTTPError
import geocoder

def geolocation(ip):
    #try:
        
        #g = geocoder.ip(ip)
        # Uses access token, increases rate limit to 50k/month. Token: 89b27ac0a6767d      056bd275394e95
        g = geocoder.ip(ip, token = '238eca1d31ff39')
        return {"lat": g.lat, "lng": g.lng, "country":g.country, "hostname":g.hostname, "org":g.org, "city":g.city}        
        
        #req = Request('https://ipinfo.io/1.1.1.1/json?token=238eca1d31ff39s')
        #response = urlopen(req)
        #urllib.request.urlopen(g)
        
'''
    except:
        #if e.code == 403:
        print('2nd API token is being used!')
        print(e.code)
            #g = geocoder.ip(ip)
            # Uses another access token after first 50k exceeds
            #g = geocoder.ip(ip, token = '89b27ac0a6767d')
            #return {"lat": g.lat, "lng": g.lng, "country":g.country, "hostname":g.hostname, "org":g.org, "city":g.city}
'''
    