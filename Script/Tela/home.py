# Importações
from pygame.sprite import collide_rect

from Script import *
from Script.Musica import *
from Script.Tela import game
from Script.Tela import menu
from Script.Textos import *
import Script.Dados as dd


# Função que dá início a todo código
def play(Parar=False):

    # Inicia o pygame e outros detalhes
    global texto_inicio
    p_mili_seg = mili_seg
    pygame.init()
    tela = pygame.display.set_mode(res_tela)
    pygame.display.set_caption('Tela inicial Group 6')
    pygame.mixer.init()
    cor = RGB()

    # Começa a musíca
    if dd.primeira_vez:
        musica_home()

    # Define os frames
    frames = pygame.time.Clock()

    # define a variável de saida
    sair = Parar

    # Começa o looping da tela
    while not sair:

        # Define os frames em 60 FPS
        frames.tick(60)

        if not dd.home_call:

            # Verifica os eventos das teclas
            for evento in pygame.event.get():

                # Verificando as ações das teclas do teclado e botão de fechar
                if evento.type == pygame.QUIT:
                    sair = True

                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_ESCAPE:
                        sair = True
                    if evento.key == pygame.K_c:
                        dd.set_prime(True)
                        game.play()
                        sair = True
                    if evento.key == pygame.K_t:
                        dd.set_call(1, True)
                        menu.play()

            # Palhaçadinha :)
            if not ii("Assents/image/Saia.jpg"):
                sair = True

            # Preenche a tela de branco
            tela.fill(BRANCO)

            # Toda a vez que o cont chegar a 7 ele chama a função RGB de novo para gerar uma nova cor para o título
            if p_mili_seg == 7:
                cor = RGB()
                p_mili_seg = 0

            # Mostra os textos na tela e define o local de cada um
            tela.blit(texto_inicio(cor), centerLarg(texto_inicio(cor), 80))

            tela.blit(texto_c, centerLarg(texto_c, 450))
            tela.blit(texto_m, centerLarg(texto_m, 500))
            tela.blit(texto_esc, centerLarg(texto_esc, 550))

            # Adiciona mais 1 no contador (usado para mudar a cor do título)
            p_mili_seg += 1

        #Atualiza tudo
        pygame.display.flip()
