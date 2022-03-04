

def getAttack(networklogs):
    dictAttack={}

    for i in networklogs:
        if dictAttack.__contains__(i.attack):
            
            dictAttack[i.attack]= dictAttack[i.attack] + 1

        else:
            dictAttack[i.attack] = 1

    return dictAttack

