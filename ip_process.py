# ip to geolocation
import geocoder

def geolocation(ip):
    g = geocoder.ip(ip)
    # Uses access token, increases rate limit to 50k/month
    #g = geocoder.ip(ip, token = '238eca1d31ff39')
    return {"lat": g.lat, "lng": g.lng, "country":g.country, "hostname":g.hostname, "org":g.org, "city":g.city}
