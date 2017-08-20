import random
import json
import sys
import requests
import hashlib
class Youdao(object):
    def __init__(self):
        # app key
        self.appKey = "0b2326799bc74b6e"
        #pass ward
        self.pwd = "h8YekUjoOWwK15BhlpsXJ0bxkgXv4XQE"

    def translate(self, fromLanguage, toLanguage, translateText):
        salt = random.randrange(10)
        signString = self.appKey + translateText + str(salt) + self.pwd
        sign = hashlib.md5(signString.encode())
        url = "http://openapi.youdao.com/api?q=" + translateText + "&from=" + fromLanguage + "&to=" + toLanguage + "&appKey=" + self.appKey +  "&salt=" + str(salt) + "&sign=" + sign.hexdigest()
        receiveMsg = requests.post(url)
        jsonObj = json.loads(receiveMsg.text)
        #print (receiveMsg.text)
        result = jsonObj["translation"]
        leng = len(result)
        return result[0]
