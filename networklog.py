# NetworkLog class to store results from analysis
class NetworkLog:
    def __init__(self, key, srcip, sport, dstip, dport, hostname, country, lat, lng, org, attack):
        self.key = key
        self.srcip  = srcip
        self.sport  = sport
        self.dstip  = dstip
        self.dport  = dport
        self.hostname = hostname
        self.country = country
        self.lat  = lat
        self.lng  = lng
        self.org = org
        self.attack = attack
