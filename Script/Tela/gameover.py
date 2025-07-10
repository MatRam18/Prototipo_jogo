#Importações
from Script.Musica import *
from Script.Textos import *
from Script.Cores import RGB
from Script import *
from Script.Tela import game
from Script.Dados import *
import Script.Dados as dd
from Script.Tela import menu


#Começa a tela de game over
def play(Parar=False):

    p_mili_seg = mili_seg

    # Inicia o pygame e outros detalhes
    pygame.init()
    tela = pygame.display.set_mode(res_tela)
    pygame.display.set_caption('GAME OVER')
    pygame.mixer.init()
    cor = RGB()

    #Encerra a música do jogo principal e inicia a música de GameOver
    if dd.primeira_vez:
        musica_game(s=False)
        musica_go()

    #Define os frames
    frames = pygame.time.Clock()

    #define a variavel de saida
    sair = Parar

    #Começa o looping da tela
    while not sair:

    #Define os frames em 60 FPS
        frames.tick(60)

        if not dd.gameover_call:

            #Verifica os eventos das teclas
            for evento in pygame.event.get():

                # Verificando as ações das teclas do teclado e botão de fechar
                if evento.type == pygame.QUIT:
                    sair = True
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_ESCAPE:
                        sair = True
                    if evento.key == pygame.K_r:
                        dd.set_prime(True)
                        game.play()
                        sair = True
                    if evento.key == pygame.K_t:
                        dd.set_call(3, True)
                        menu.play()


            # Palhaçadinha :)
            if not ii("Assents/image/Saia.jpg"):
                sair = True

            # Preenche a tela de branco
            tela.fill(PRETO)

            # Toda a vez que o cont chegar a 7 ele chama a função RGB de novo para gerar uma nova cor para o título
            if p_mili_seg == 8:
                cor = RGB()
                p_mili_seg = 0

            # Mostra os textos na tela e define o local de cada um
            tela.blit(game_over(cor), [300, 200])
            tela.blit(game_over2, [170, 400])

            # Adiciona mais 1 no contador (usado para mudar a cor do título)
            p_mili_seg += 1

        # Atualiza tudo
        pygame.display.flip()