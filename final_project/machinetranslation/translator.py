''' Translator module used to translate English text to French and vice versa'''

import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

api_key = os.environ['apikey']
url = os.environ['url']
authenticator = IAMAuthenticator(api_key)
language_translator = LanguageTranslatorV3(
    version = '2018-05-01', authenticator=authenticator
)
language_translator.set_service_url(url)

def english_to_french(english_text):
    ''' translates English text to French '''
    translation = language_translator.translate(
        text=english_text,
        model_id='en-fr').get_result()

    french_text = translation['translations'][0]['translation']

    return french_text

def french_to_english(french_text):
    ''' translates French text to English '''
    translation = language_translator.translate(
        text=french_text,
        model_id='fr-en').get_result()

    english_text = translation['translations'][0]['translation']

    return english_text
