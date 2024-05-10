import requests
import openai
def get_data__from_keyboard():
    """ Aquesta funció recull les dades des del teclat
       Retorna: una única cadena de caràcters"""
    return input()
def get_data_from_server(URL):
  """ Aquesta funció recull les dades des d’una API Rest a partir d’una URL """
  return requests.get(URL).text
def get_data_from_chatGPT(questio):
    """Aquesta funció recull la resposta a una pregunta"""
    openai.api_key = "sk - grm5sT2LEcKEMQP5uaeVT3BlbkFJtmkEm9uYvBpPtnS94pM0"
    ENGINE = "gpt-3.5-turbo"
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