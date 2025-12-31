from datetime import datetime, time

def hora():
    now = datetime.now().time()
    return now

def checahora():
    horario = hora()
    if horario >= time(0, 0) and horario < time(6, 0):
        risco = 0
    elif horario >= time(6, 0) and horario < time(20, 0):
        risco = 0
    elif horario >= time(20, 0) and horario <= time(21, 0):
        risco = 0.25
    elif horario > time(21, 0) and horario <= time(22, 0):
        risco = 0.5
    elif horario > time(22, 0) and horario <= time(23, 0):
        risco = 0.75
    else:
        risco = 1
    return risco
