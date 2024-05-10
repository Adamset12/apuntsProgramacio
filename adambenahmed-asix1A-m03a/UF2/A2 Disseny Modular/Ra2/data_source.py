import requests
import openai
def get_data__from_keyboard():
    """ Aquesta funció recull les dades des del teclat
       Retorna: una única cadena de caràcters"""
    return input()
def get_data_from_server(URL):
  """ Aquesta funció recull les dades des d’una API Rest a partir d’una URL """
  return requests.get(URL).text.split("\"")[1]
def get_data_from_chatGPT(questio):
    openai.api_key = 'sk-proj-9L82KGYJlhgvkj3cjTHCT3BlbkFJWd4OY3ibdABBz0e0s617'
    ENGINE = "gpt-3.5-turbo-instruct"
    ANSWER_QUANTITY = 1
    MAX_TOKENS = 2048
    completion = openai.Completion.create(engine=ENGINE, prompt=questio, n=ANSWER_QUANTITY, max_tokens=MAX_TOKENS)
    return completion.choices[0].text
#TODO al 3r lliurament
'''def get_data_from_file(file_name):
    """ Aquesta funció recull les dades des d'un arxiu
    Entrada: Una cadena de caràcters amb el nom del fitxer origen
    Retorna: una única cadena de caràcters"""
    dades=""
    #TODO: Per al 3r lliurament "r3" ...
    return text'''