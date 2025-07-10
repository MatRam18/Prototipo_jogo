#Importações
from random import randint

#Define as cores
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
ROXO = (102, 0, 255)
VERMELHO = (255, 0, 0)
AZUL = (0, 0, 255)
VERDE = (0, 255, 0)
LARANJA = (255, 85, 0)

#Função para gerar um RGB (Funciona somente se durante o jogo ela for chamada várias vezes)
def RGB():
    return (randint(0, 255), randint(0, 255), randint(0, 255))

