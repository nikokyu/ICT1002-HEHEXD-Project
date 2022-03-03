# ip to geolocation
import geocoder

def geolocation(ip):
    g = geocoder.ip(ip)
    return {"lat": g.lat, "lng": g.lng, "country":g.country, "hostname":g.hostname, "org":g.org, "city":g.city}
