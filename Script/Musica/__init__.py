#Importações
import pygame

#Função para tocar a música de início
def musica_home(s=True):
    pygame.mixer.init()
    pygame.mixer.music.load('Assents/sounds/home.mp3')
    pygame.mixer.music.play(loops=100000000)
    if not s:
        pygame.mixer.music.stop()

#Função para tocar a música do jogo
def musica_game(s=True):
    pygame.mixer.init()
    pygame.mixer.music.load('Assents/sounds/play.mp3')
    pygame.mixer.music.play(loops=100000000)
    if not s:
        pygame.mixer.music.stop()

#função para tocar a música de GameOver
def musica_go(s=True):
    pygame.mixer.init()
    pygame.mixer.music.load('Assents/sounds/gameover.mp3')
    pygame.mixer.music.play(loops=100000000)
    if not s:
        pygame.mixer.music.stop()
