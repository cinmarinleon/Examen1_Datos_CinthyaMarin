import utilitarios
from utilitarios import *

#
# unPaciente = {
#     "idPaciente": utilitarios.generar_id_pacientes(),
#     "edad": utilitarios.generar_numero_aleatorio(0,1200),
#     "condicion": utilitarios.generar_estado_salud(),
#
# }
#
# unaCelula = {
#     "idCelula": utilitarios.generar_id_celula(),
#     "analista": utilitarios.generar_id_analista(),
#     "radioX": utilitarios.generar_numero_aleatorio(5,99),
#     "radioY": utilitarios.generar_numero_aleatorio(5,99),
#     "radioZ": utilitarios.generar_numero_aleatorio(5,99),
#
# }

# Generar las celulas

idCelulasString = utilitarios.generar_lista_ids_celulas()

pilaCelulas = []
for celula in idCelulasString:
    unaCelula = {
        "idCelula": celula,
        "analista": utilitarios.generar_id_analista(),
        "radioX": utilitarios.generar_numero_aleatorio(5,99),
        "radioY": utilitarios.generar_numero_aleatorio(5,99),
        "radioZ": utilitarios.generar_numero_aleatorio(5,99),
    }
    pilaCelulas.append(unaCelula)

#Generar los pacientes

idPacientesString = utilitarios.generar_lista_ids_pacientes()

listaPacientes = []
for paciente in idPacientesString:
    unPaciente = {
        "idPaciente": paciente,
        "edad": utilitarios.generar_numero_aleatorio(0,1200),
        "condicion": utilitarios.generar_estado_salud(),
        "celulas": []
    }
    listaPacientes.append(unPaciente)

# Asignar una celula por paciente

for paciente in listaPacientes:
    paciente["celulas"].append(pilaCelulas.pop())

for celula in pilaCelulas:
    paciente = random.choice(listaPacientes)
    paciente["celulas"].append(celula)

 


