# NetworkLog class to store results from analysis
class NetworkLog:
    def __init__(self, key, ip, country, lat, lng, attack):
        self.key = key
        self.ip  = ip
        self.country = country
        self.lat  = lat
        self.lng  = lng
        self.attack = attack
