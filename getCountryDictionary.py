

def getCountry(networklogs):
    dictCountry={}

    for i in networklogs:
        if dictCountry.__contains__(i.country):
            
            dictCountry[i.country]= dictCountry[i.country] + 1

        else:
            dictCountry[i.country] = 1

    return dictCountry

