
import string
import random

# Generar los ID_CELULA de forma aleatoria

letrasValidas = string.ascii_lowercase

def generar_id_celula():
    identificador = 'c'
    for i in range(3):
        identificador += random.choice(letrasValidas)
    return identificador

def generar_lista_ids_celulas():
    celulas = set()
    for i in range(100):
        while True:
            ident = generar_id_celula()
            if ident not in celulas:
                celulas.add(ident)
                break
    return celulas


# Generar los COD_ANALISTA de forma aleatoria


letrasValidasAnalistas = string.ascii_uppercase

def generar_id_analista():
    identifica = 'A'
    for i in range(4):
        identifica += random.choice(letrasValidasAnalistas)
    return identifica

def generar_lista_ids_analista():
    analistas = set()
    for i in range(4):
        while True:
            ident = generar_id_analista()
            if ident not in analistas:
                analistas.add(ident)
                break
    return analistas

# Generar numeros aleatorios en un rango

def generar_numero_aleatorio(minimo, maximo):
    return random.randint(minimo, maximo)


# Generar los COD_PACIENTES de forma aleatoria

letrasValidasPacientes = string.ascii_uppercase

def generar_id_pacientes():
    identificador = 'P'
    for i in range(4):
        identificador += random.choice(letrasValidasPacientes)
    return identificador

def generar_lista_ids_pacientes():
    pacientes = set()
    for i in range(30):
        while True:
            ident = generar_id_pacientes()
            if ident not in pacientes:
                pacientes.add(ident)
                break
    return pacientes

# Generar numeros aleatorios entre 0 y 1 que definen el estado de salud

import random

def generar_estado_salud():
    return round(random.uniform(0, 1), 2)