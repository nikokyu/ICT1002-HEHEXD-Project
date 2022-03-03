# NetworkLog class to store results from analysis
class NetworkLog:
    def __init__(self, key, ip, hostname, country, lat, lng, org, attack):
        self.key = key
        self.ip  = ip
        self.hostname = hostname
        self.country = country
        self.lat  = lat
        self.lng  = lng
        self.org = org
        self.attack = attack
