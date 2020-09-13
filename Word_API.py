import json
import os
import requests

class Word_Api:

    def is_proper_noun(word):
        random_word = word
        url = "https://wordsapivl.p.rapidapi.com/words/{}/typeOf".format(random_word)

        host = os.environ['WORDS_API_HOST']
        key = os.environ['WORDS_API_KEY']

        headers = {
            'x-rapidapi-host': host,
            'x-rapidapi-key': key
        }

        response = requests.request("GET", url, headers=headers)
        result = response.text
        result = json.loads(result)

        try:
            if result['typeOf'] is None or len(result['typeOf'])==0:
                return False
            else:
                return True

        except KeyError:
            #When the eord is not recognised by the API
            return False
