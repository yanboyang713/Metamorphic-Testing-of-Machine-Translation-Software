import sys
import xml.etree.ElementTree as ET
from xml.etree import ElementTree
import requests
import time
from threading import Timer

class MaxDepth:                     # The target object of the parser
    def __init__(self):
        maxDepth = 0
        depth = 0
    def start(self, tag, attrib):   # Called for each opening tag.
        self.depth += 1
        if self.depth > self.maxDepth:
            self.maxDepth = self.depth
    def end(self, tag):             # Called for each closing tag.
        self.depth -= 1
    def data(self, data):
        pass            # We do not need to do anything with data.
    def close(self):    # Called when all data has been parsed.
        return self.maxDepth


class Bing(object):
    def __init__(self):
        # subscription ID
        self.subscriptionID= "c3136e53-8485-4dc0-b2fb-99ba109b8508"
        # key one
        self.keyOne = "aad8cda03b66483da611e75226208cd8"
        #key two
        self.keyTwo = "c3ea56f82dd5420cb0a08ea112726034"
        # tokenURL
        self.tokenUrl = "https://api.cognitive.microsoft.com/sts/v1.0/issueToken?Subscription-Key=" + self.keyOne
        # token
        self.token = ""
        # refresh token
        Timer(5, self.__refreshToken, ()).start()

    def getToken(self):
        receiveMsg = requests.post(self.tokenUrl)
        self.token = receiveMsg.text

    def translate(self, translateText, fromLanguage, toLanguage):
        translateUrl = "https://api.microsofttranslator.com/v2/http.svc/Translate"
        params = {'appid': 'Bearer '+ self.token, 'text': translateText, 'from': fromLanguage, 'to': toLanguage}
        headers = {'Accept': 'application/xml'}
        receivedTranslate = requests.get(translateUrl, params=params, headers=headers)
        tree = ElementTree.fromstring(receivedTranslate.content)
        return tree.text

    def __refreshToken(self):
        self.getToken()
        Timer(5, self.__refreshToken, ()).start()
