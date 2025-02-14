from Script.Musica import *
from Script.Textos import *
from Script import *
import Jogo

#Começa a tela de menu
def Tela_Inicial(Parar=False):
#Inicia o pygame e resto
    global cont, texto_inicio
    pygame.init()
    tela = pygame.display.set_mode(reso)
    pygame.display.set_caption('Tela inicial Group 6')
    pygame.mixer.init()
#Começa a musicas de menu
    musica_menu()
#Define os frames
    frames = pygame.time.Clock()
#define a variavel de saida
    sair = Parar
#Começa o loop da tela
    while not sair:
    #Define os frames
        frames.tick(60)
    #Verifica os eventos
        for evento in pygame.event.get():
        #fiquei com preguiça de explicar, vai na def jogo que a explicação é quase a mesma
            if evento.type == pygame.QUIT:
                sair = True
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    sair = True
                if evento.key == pygame.K_c:
                    Jogo.Jogar()
                    sair = True
        if not ii("Saia.jpg"):
            sair = True
        tela.fill(BRANCO)

        if cont == 8:
            RGB = (randint(0, 255), randint(0, 255), randint(0, 255))
            texto_inicio = font1.render('Jogo Bolado Pra Dedéu', True, RGB)
            cont = 0

        tela.blit(texto_inicio, [220, 40])
        tela.blit(texto_inicio2, [70, 200])
        tela.blit(texto_inicio3, [50, 300])
        tela.blit(texto_esc, [30, 500])
        tela.blit(texto_c, [580, 500])

        cont += 1

        pygame.display.flip()

