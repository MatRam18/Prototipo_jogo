# Importações
from Script.Cores import *
from Script.Dados import *
import pygame

# Inicia o pygame
pygame.font.init()

# Define as fontes
font1 = pygame.font.Font('Assents/font/COMICSANS.TTF', 50)
font2 = pygame.font.Font('Assents/font/COMICSANS.TTF', 30)
font3 = pygame.font.Font('Assents/font/COMICSANS.TTF', 60)
font4 = pygame.font.Font('Assents/font/COMICSANS.TTF', 40)
font5 = pygame.font.Font('Assents/font/COMICSANS.TTF', 25)

def centerLarg(texto, altura):
    return texto.get_rect(center=(larguraT // 2, altura))


# Função para mostrar o título da home (Por ser um texto que fica mudando de cor, é nescessario ser uma função)
def texto_inicio(color):
    return font3.render('CAÇA AO MOUSE', True, color)

# Variáveis com os textos da home
texto_m = font2.render('(Precione T para ir ao tutorial)', True, PRETO)
texto_esc = font2.render('(Precione Esc para sair)', True, PRETO)
texto_c = font2.render('(Precione C para começar)', True, PRETO)

# textos de explicação

texto_titulo1 = font2.render('OBJETIVO:', True, ROXO)
texto_titulo2 = font2.render('PERSONAGENS:', True, ROXO)

texto_menu1 = font5.render('Desvie dos Bill Gates o maximo que der', True, PRETO)
texto_menu2 = font5.render('Use o W.A.S.D ou as SETINHAS para se movimentar', True, PRETO)
texto_menu3 = font5.render('Até o Round 5 os Bill Gates almentam de tamanho', True, PRETO)
texto_menu4 = font5.render('E até o Round 10 os Bill Gates almentam de tamanho', True, PRETO)






# Variáveis para mostrar os textos durante o jogo
texto_round = font5.render('Round:', True, PRETO)

texto_tempo = font5.render('Tempo:', True, PRETO)

texto_pause = font3.render('Pause', True, PRETO)
texto_pause2 = font2.render('|Aperte ESC novamente para sair|', True, PRETO)
texto_pause3 = font2.render('|Aperte C para voltar ao jogo|', True, PRETO)

texto_vida = font5.render('Vidas:', True, PRETO)

def num(numero):
    return font5.render(str(numero), True, PRETO)



# Função para mostrar o título de GameOver (Por ser um texto que fica mudando de cor, é nescessario ser uma função)
def game_over(color):
    return font3.render('GAME OVER', True, color)

# Variável com o texto de continuar
game_over2 = font2.render('(Precione Esc para sair ou R para recomeçar)', True, BRANCO)
