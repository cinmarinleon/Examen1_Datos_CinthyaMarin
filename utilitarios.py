# Generar los ID_CELULA de forma aleatoria

import string
import random

letrasValidas = string.ascii_lowercase

def generate_id():
    identificador = 'c'
    for i in range(3):
        identificador += random.choice(letrasValidas)
    return identificador

def generar_lista_ids_celulas():
    celulas = set()
    for i in range(100):
        while True:
            ident = generate_id()
            if ident not in celulas:
                celulas.add(ident)
                break
    return celulas


# Generar los COD_ANALISTA de forma aleatoria


letrasValidasAnalistas = string.ascii_uppercase

def generate_id_analista():
    identifica = 'A'
    for i in range(4):
        identifica += random.choice(letrasValidasAnalistas)
    return identifica

def generar_lista_ids_analista():
    analistas = set()
    for i in range(4):
        while True:
            ident = generate_id()
            if ident not in analistas:
                analistas.add(ident)
                break
    return analistas
