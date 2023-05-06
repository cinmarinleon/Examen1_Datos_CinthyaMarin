import utilitarios
from utilitarios import *

# Generar las celulas

idCelulasString = utilitarios.generar_lista_ids_celulas()

pilaCelulas = []
for celula in idCelulasString:
    unaCelula = {
        "ID_CELULA": celula,
        "COD_ANALISTA": utilitarios.generar_id_analista(),
        "DIM_RAD_NM_X": utilitarios.generar_numero_aleatorio(5,99),
        "DIM_RAD_NM_Y": utilitarios.generar_numero_aleatorio(5,99),
        "DIM_RAD_NM_Z": utilitarios.generar_numero_aleatorio(5,99),
    }
    pilaCelulas.append(unaCelula)

#Generar los pacientes

idPacientesString = utilitarios.generar_lista_ids_pacientes()

listaPacientes = []
for paciente in idPacientesString:
    unPaciente = {
        "COD_PACIENTE": paciente,
        "EDAD_PACIENTE": utilitarios.generar_numero_aleatorio(0,1200),
        "COND_GENERAL_PACIENTE": utilitarios.generar_estado_salud(),
        "celulas": []
    }
    listaPacientes.append(unPaciente)

# Asignar una celula por paciente

for paciente in listaPacientes:
    paciente["celulas"].append(pilaCelulas.pop())

for celula in pilaCelulas:
    paciente = random.choice(listaPacientes)
    paciente["celulas"].append(celula)


datosAplanados = []
for paciente in listaPacientes:
    for celula in paciente["celulas"]:
        unPaciente = {
            "ID_CELULA": celula["ID_CELULA"],
            "COD_ANALISTA": celula["COD_ANALISTA"],
            "DIM_RAD_NM_X": celula["DIM_RAD_NM_X"],
            "DIM_RAD_NM_Y": celula["DIM_RAD_NM_Y"],
            "DIM_RAD_NM_Z": celula["DIM_RAD_NM_Z"],
            "COD_PACIENTE": paciente["COD_PACIENTE"],
            "COND_GENERAL_PACIENTE": paciente["COND_GENERAL_PACIENTE"],
            "EDAD_PACIENTE": paciente["EDAD_PACIENTE"],
        }
        datosAplanados.append(unPaciente)





