""" Converter horário do formato 12 horas AM/PM para o de 24 hrs"""


# testes
# variavel = '12:00:00AM'
# print(variavel.split(':'))

# print(variavel.find("AM"))


def converter_hora(hora):
    horario, sufixo = hora[:-2], hora[-2:]
    horario_separado = horario.split(":")
    horario_separado[0] = int(horario_separado[0])
    if horario_separado[0] == 12:
        horario_separado[0] = 0
    if sufixo == "PM":
        if horario_separado[0] != 12:
            horario_separado[0] += 12
    horario_separado[0] = str(horario_separado[0]).zfill(2)
    horario = ":".join(horario_separado)
    print(horario)

hora = '11:00:00PM'
converter_hora(hora)