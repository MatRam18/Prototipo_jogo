from Script.Tela import game
from Script.Tela import home
from Script.Tela import gameover
from Script.Cores import *
from Script.Textos import *
import pygame
import Script.Dados as dd

def play(Parar=False):
    pygame.init()
    tela = pygame.display.set_mode(res_tela)
    pygame.display.set_caption('Menu de explicações')
    pygame.mixer.init()

    if dd.primeira_vez:
        dd.set_prime(False)

    frames = pygame.time.Clock()

    sair = Parar

    while not sair:

        frames.tick(60)

        for evento in pygame.event.get():

            if evento.type == pygame.QUIT:
                sair = True
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    if dd.home_call:
                        dd.set_call(1, False)
                        sair = True
                    if dd.game_call:
                        dd.set_call(2, False)
                        sair = True
                    if dd.gameover_call:
                        dd.set_call(3, False)
                        sair = True
        tela.fill(BRANCO)

        tela.blit(texto_titulo1, [10, 0])

        tela.blit(texto_menu1, [50, 40])
        tela.blit(texto_menu2, [50, 70])
        tela.blit(texto_menu3, [50, 100])
        tela.blit(texto_menu4, [50, 130])

        tela.blit(texto_titulo2, [10, 165])

        tela.blit(rato_img, [50, 205])

        tela.blit(bil_img_esq_azul, [50, 240])
        tela.blit(bil_img_esq_roxo, [50, 275])
        tela.blit(bil_img_esq_verde, [50, 310])
        tela.blit(bil_img_esq_laranja, [50, 345])
        tela.blit(bil_img_esq_vermelho, [50, 380])

        tela.blit(bil_img_ret_rosa, [50, 420])
        tela.blit(bil_img_ret_ciano, [50, 495])
        tela.blit(bil_img_ret_salmao, [50, 570])
        tela.blit(bil_img_ret_amarelo, [50, 645])

        pygame.display.flip()
