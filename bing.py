import sys
from microsofttranslator import Translator
import requests
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
    def getToken(self):
        receiveMsg = requests.post(self.tokenUrl)
        self.token = receiveMsg.text
        print (receiveMsg.text)
        print (receiveMsg.status_code)
        print (receiveMsg.reason)
        print (receiveMsg)
    def translate(self, translateText, fromLanguage, toLanguage):
        translateUrl = "https://api.microsofttranslator.com/v2/http.svc/Translate"
        params = {'appid': 'Bearer '+ self.token, 'text': translateText, 'from': fromLanguage, 'to': toLanguage}
        headers = {'Accept': 'application/xml'}
        receivedTranslate = requests.get(translateUrl, params=params, headers=headers)
        print(receivedTranslate.text)
