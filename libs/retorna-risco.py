from check_hora import checahora
from check_ip import checkip, ip
from check_loc import checkloc, loc

class Risco:
    def __init__(self, valor):
        self.valor = valor

    def peso(self, w):
        self.valor *= w
        return self

def retorna_risco():
    global RH
    RH = Risco(checahora())
    RH.peso(1)

    global RI
    RI = Risco(checkip(ip()))
    RI.peso(5)

    global RL
    RL = Risco(checkloc())
    RL.peso(2)

# chamar a função
retorna_risco()

# agora você pode acessar RH e RI diretamente
print(RH.valor)
print(RI.valor)
print(RL.valor)