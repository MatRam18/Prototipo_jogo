from Script.Cores import *
from Script.Dados import *
import pygame

pygame.font.init()
font1 = pygame.font.Font('COMICSANS.TTF', 50)
font2 = pygame.font.Font('COMICSANS.TTF', 30)
font4 = pygame.font.Font('COMICSANS.TTF', 40)
font3 = pygame.font.Font('COMICSANS.TTF', 60)

texto_inicio = font1.render('Jogo Bolado Pra Dedéu', True, RGB)
texto_inicio2 = font4.render('Desvie dos inimigos até o Maximo que puder', True, VERDE)
texto_inicio3 = font1.render('E NÂO encoste na barreira vermelha', True, VERMELHO)
texto_esc = font2.render('(Precione Esc para sair)', True, PRETO)
texto_c = font2.render('(Precione C para começar)', True, PRETO)

texto_round = font1.render('Round:', True, PRETO)
num_round = font1.render(str(Round), True, PRETO)

texto_tempo = font1.render('Tempo:', True, PRETO)
num_tempo = font1.render(str(tempoU), True, PRETO)

texto_vida = font1.render('VIDAS:', True, PRETO)
num_vida = font1.render(str(quant_vida), True, PRETO)
GAME_OVER = font3.render('GAME OVER', True, VERMELHO)
GAME_OVER2 = font2.render('(Precione Esc para sair ou R para reestarta)', True, ROXO)

