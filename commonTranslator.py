from youdao import Youdao
from bing import Bing
from googleTranslator import Google

# This class can be used as a common interface between
# all the different translation engines.
#
# Instructions:
#   1. Create a CommonTranslator object
#   2. Call the translate() function
#   3. Input parmeters as
#   translate(desired_translator, text_to_translate, desired_language, starting_language)
#
#   Valid translators are Google, Bing and Youdao
#   Can also requset All to recieve a dictionary containing the translation from each.

class CommonTranslator(object):

    # Create objects for each possible type of translation
    def __init__(self):
        self.__googleTranslator = Google()
        self.__bingTranslator = Bing()
        self.__youdaoTranslator = Youdao()

    # Call this function to begin a translation
    # irregardless of the transaltion engine desired
    def translate(self, translator, text, output_lang, input_lang):
        # Pass the request to the appropriate translate engine's function
        if translator.lower() == 'all':
            return {
                'Google':   self.__translateGoogle(text, output_lang),
                'Bing':     self.__translateBing(text, output_lang, input_lang),
                'Youdao':   self.__translateYoudao(text, output_lang, input_lang)
            }
        if translator.lower() == 'google':
            return self.__translateGoogle(text, output_lang)
        elif translator.lower() == 'bing':
            return self.__translateBing(text, output_lang, input_lang)
        elif translator.lower() == 'youdao':
            return self.__translateYoudao(text, output_lang, input_lang)
        # If an invalid tranlation engine is specified
        # return false to indicate failure
        else:
            return False

    # This function is responsible for performing all Google Translations
    def __translateGoogle(self, text, output_lang):
        translated_text = self.__googleTranslator.translate(text, output_lang)
        return translated_text['translatedText']

    # This function is responsible for performing all Bing Translations
    def __translateBing(self, text, output_lang, input_lang):
        self.__bingTranslator.getToken()
        translated_text = self.__bingTranslator.translate(text, input_lang, output_lang)
        return translated_text

    # This function is responsible for performing all Youdao Translations
    def __translateYoudao(self, text, output_lang, input_lang):
        translated_text = self.__youdaoTranslator.translate(input_lang, output_lang, text)
        return translated_text
