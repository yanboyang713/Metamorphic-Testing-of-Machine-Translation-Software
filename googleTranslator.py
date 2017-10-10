from google.cloud import translate
from google.oauth2 import service_account

# This class sets up the google cloud translation object with credentials and
# validates the target language.
class Google(object):
    def __init__(self):
        # When the sample credit has expired a new service key will need to be genreated.
        translateCredentials = service_account.Credentials.from_service_account_file(
        'CSCI318 Translate Testing-901005799451.json')
        self.translateClient = translate.Client(credentials=translateCredentials)
        # This is a list of all posible languages that can be specified for the
        # Google translate API
        self.validLanguages = ['af', 'sq', 'am',
            'ar', 'hy', 'az', 'eu', 'be', 'bn', 'bs', 'bg', 'ca', 'ceb',
            'zh-CN', 'zh-TW', 'co', 'hr', 'cs', 'da', 'nl', 'en', 'eo',
            'etm', 'fi', 'fr', 'fy', 'gl', 'ka', 'de', 'el', 'gu', 'ht',
            'ha', 'haw', 'iw', 'hi', 'hmn', 'hu', 'is', 'ig', 'id', 'ga',
            'it', 'ja', 'jw', 'kn', 'kk', 'km', 'ko', 'ku', 'ky', 'lo',
            'la', 'lv', 'lt', 'lb', 'mk', 'mg', 'ms', 'ml', 'mi', 'mr',
            'mn', 'my', 'ne', 'no', 'ny', 'ps', 'fa', 'pl', 'pt', 'pa',
            'ro', 'ru', 'sm', 'gd', 'sr', 'st', 'sn', 'sd', 'si', 'sk',
            'sl', 'so', 'es', 'su', 'sw', 'sv', 'tl', 'tg', 'ta', 'te',
            'th', 'tr', 'uk', 'ur', 'uz', 'vi', 'cy', 'xh', 'yi', 'yo', 'zu']

    # Input a phrase to be translated (input language is autmatically detected)
    # target language must be in the ISO-639-1 Code
    # Python3 supports all strings as unicode so no conversion is required.
    def translate(self, phrase, target):
        # Check that the taget language is valid than return the translation
        if target in self.validLanguages:
            result  = self.translateClient.translate(phrase, target_language=target)
            return result
        else:
            raise ValueError('The output language ' + target + ' is not available.')
            return None
