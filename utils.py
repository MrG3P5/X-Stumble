import requests

def topCrownLocal(username):
    try:
        pattern = 1
        found = False
        req = requests.get("http://kitkabackend.eastus.cloudapp.azure.com:5010/highscore/crowns/list?start=0&count=100&country=ID").json()
        for x in req['scores']:
            if username in x['User']['Username']:
                pattern = pattern
                found = True
                break
            else:
                pattern += 1
        if found == True:
            return pattern
        else:
            return "0"
    except:
        return "0"

def topCrownGlobal(username):
    try:
        pattern = 1
        found = False
        req = requests.get("http://kitkabackend.eastus.cloudapp.azure.com:5010/highscore/crowns/list?start=0&count=100&country=").json()
        for x in req['scores']:
            if username in x['User']['Username']:
                pattern = pattern
                found = True
                break
            else:
                pattern += 1
        if found == True:
            return pattern
        else:
            return "0"
    except:
        return "0"

def topRankLocal(username):
    try:
        pattern = 1
        found = False
        req = requests.get("http://kitkabackend.eastus.cloudapp.azure.com:5010/highscore/rank/list?start=0&count=100&country=ID").json()
        for x in req['scores']:
            if username in x['User']['Username']:
                pattern = pattern
                found = True
                break
            else:
                pattern += 1
        if found == True:
            return pattern
        else:
            return "0"
    except:
        return "0"

def topRankGlobal(username):
    try:
        pattern = 1
        found = False
        req = requests.get("http://kitkabackend.eastus.cloudapp.azure.com:5010/highscore/rank/list?start=0&count=100&country=").json()
        for x in req['scores']:
            if username in x['User']['Username']:
                pattern = pattern
                found = True
                break
            else:
                pattern += 1
        if found == True:
            return pattern
        else:
            return "0"
    except:
        return "0"

print(topRankLocal("IG: @xmrg3p5"))
