import utilitarios
from utilitarios import *

unPaciente = {
    "idPaciente": utilitarios.generar_id_pacientes(),
    "edad": utilitarios.generar_numero_aleatorio(0,1200),
    "condicion": utilitarios.generar_estado_salud(),

}

unaCelula = {
    "idCelula": utilitarios.generar_id_celula(),
    "analista": utilitarios.generar_id_analista(),
    "radioX": utilitarios.generar_numero_aleatorio(5,99),
    "radioY": utilitarios.generar_numero_aleatorio(5,99),
    "radioZ": utilitarios.generar_numero_aleatorio(5,99),

}

