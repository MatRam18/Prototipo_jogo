import pygame


def musica_menu(s=True):
    pygame.mixer.init()
    pygame.mixer.music.load('Menu.mp3')
    pygame.mixer.music.play(loops=100000000)
    if not s:
        pygame.mixer.music.stop()


def musica_jogo(s=True):
    pygame.mixer.init()
    pygame.mixer.music.load('Jogo.mp3')
    pygame.mixer.music.play(loops=100000000)
    if not s:
        pygame.mixer.music.stop()
