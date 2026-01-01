from libs.check_hora import checahora
from libs.check_ip import checkip, ip
from libs.check_loc import checkloc, loc
from libs.check_dev import check_dev
import numpy as np

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

    global RD
    RD = Risco(check_dev())
    RD.peso(3)

def Retorno():
    retorna_risco()
    resultado = 1/(1+np.exp(-0.6*(RH.valor + RI.valor + RL.valor + RD.valor-0.7)))
    return resultado

print(Retorno())