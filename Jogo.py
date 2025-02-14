from Script.Musica import *
from Script.Textos import *
from Script import *


#Começa o jogo
def Jogar(Parar=False):
#Deixa as variaveis globais (Frescurite da porra)
    global personagem, num_vida, vel_x, vel_y, quant_vida, recomecar, tempo, tempoO
    global velO, velO2, velO3, velO4, alt, lar, velP3, velP2, velP, alt2, lar2
    global oponenteX, oponenteX2 , oponenteX3, Round, num_round, num_tempo, tempoU
    global velO5, velP4
#Mesma coisa do menu
    pygame.init()
    pygame.font.init()
    tela = pygame.display.set_mode(reso)
    pygame.display.set_caption('Jogo Group 6')
#Põe a barreira em uma lista
    pads = [left_pad, right_pad, up_pad, down_pad]

#Mesma coisa do menu, com a diferença que aqui para a musica do menu para começar a do jogo
    musica_menu(s=False)
    musica_jogo()
    frames = pygame.time.Clock()
    sair = Parar

#Começa o loop
    while not sair:

    #Define os frames
        frames.tick(60)

    #Randoriza o local de surgimento de novo
        loq_opo_y = randint(30, 300)
        loq_opo_y2 = randint(480, 680)
        loq_opo_y3 = randint(240, 450)
        loq_opo_y4 = choice([randint(40, 80), randint(550, 680)])
        loq_opo_y5 = randint(50, 680)

        loq_opo_x = randint(420, 650)
        loq_opo_x2 = randint(540, 950)
        loq_opo_x3 = randint(80, 450)
        loq_opo_x4 = choice([randint(50, 150), randint(800, 950)])

    #Preenche a tela com fundo branco
        tela.fill(BRANCO)

    #Verifica os botões e eventos
        for evento in pygame.event.get():

        #Faz o evento de fechar a janela acontecer
            if evento.type == pygame.QUIT:
                sair = True

        #verifica os botões precionados
            if evento.type == pygame.KEYDOWN:

            #Faz o botão Esc sair do jogo
                if evento.key == pygame.K_ESCAPE:
                    sair = True

            #Faz o botão R recomeçar o jogo caso a quantidade de vida seja 0
                if evento.key == pygame.K_r:
                    if quant_vida == 0:
                        recomecar = True

            #Dá função aos botões de movimentos
                if evento.key == pygame.K_d or evento.key == pygame.K_RIGHT:
                    vel_x = vel
                if evento.key == pygame.K_w or evento.key == pygame.K_UP:
                    vel_y = -vel
                elif evento.key == pygame.K_a or evento.key == pygame.K_LEFT:
                    vel_x = -vel
                elif evento.key == pygame.K_s or evento.key == pygame.K_DOWN:
                    vel_y = vel
        #Verifica as teclas que não estão precionadas
            if evento.type == pygame.KEYUP:

            #Verifica o botão de recomeçar
                if evento.key == pygame.K_r:
                    recomecar = False

            #Verifica os botçoes de movimento
                if evento.key == pygame.K_w or evento.key == pygame.K_s:
                    vel_y = 0
                if evento.key == pygame.K_a or evento.key == pygame.K_d:
                    vel_x = 0
                if evento.key == pygame.K_UP or evento.key == pygame.K_DOWN:
                    vel_y = 0
                if evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT:
                    vel_x = 0

    #Faz os parametros voltarem ao inicio caso recomese
        if recomecar:
            quant_vida = 3

            velO = 3
            velO2 = 4
            velO3 = 5
            velO4 = 2
            velO5 = 9

            velP = 4
            velP2 = 2
            velP3 = 3
            velP4 = 6

            alt = 25
            lar = 35

            alt2 = 35
            lar2 = 25

            tempoO = 1
            Round = 1
            tempoU = 0

            num_vida = font1.render(str(quant_vida), True, PRETO)
            num_round = font1.render(str(Round), True, PRETO)
            num_tempo = font1.render(str(tempoU), True, PRETO)

            oponenteY.x = loq_opoe_x
            oponenteY2.x = loq_opoe_x
            oponenteY3.x = loq_opoe_x
            oponenteY4.x = loq_opoe_x
            oponenteY5.x = loq_opoe_x

            oponenteX.y = loq_opox_y
            oponenteX2.y = loq_opox_y
            oponenteX3.y = loq_opox_y
            oponenteX4.y = loq_opox_y

    #Faz o protagonista andar
        personagem.x += vel_x
        personagem.y += vel_y
    #Almenta a altura/largura e velocidade dos nossos oponentes
        if tempoO == 11:
            if Round <= 10:
                velO += 1
                velO2 += 1
                velO3 += 1
                velO4 += 1
                velO5 += 1

                velP += 1
                velP2 += 1
                velP3 += 1
                velP4 += 1

                alt += 2
                lar += 4
                alt2 += 4
                lar2 += 2

            tempoO = 1
            Round += 1

            num_round = font1.render(str(Round), True, PRETO)


    #Cria o protagonista e os oponentes enquanto a vida não for 0
        if quant_vida != 0:

        #Cria o nosso protagonista
            pygame.draw.rect(tela, PRETO, personagem)

        #Cria os oponentes
            oponenteY.x += velO
            oponenteY.width = lar
            oponenteY.height = alt

            oponenteY2.x += velO2
            oponenteY2.width = lar
            oponenteY2.height = alt

            oponenteY3.x += velO3
            oponenteY3.width = lar
            oponenteY3.height = alt

            oponenteY4.x += velO4
            oponenteY4.width = lar
            oponenteY4.height = alt

            oponenteY5.x += velO5
            oponenteY5.width = lar
            oponenteY5.height = alt

            oponenteX.y -= velP
            oponenteX.width = lar2
            oponenteX.height = alt2

            oponenteX2.y -= velP2
            oponenteX2.width = lar2
            oponenteX2.height = alt2

            oponenteX3.y -= velP3
            oponenteX3.width = lar2
            oponenteX3.height = alt2

            oponenteX4.y -= velP4
            oponenteX4.width = lar2
            oponenteX4.height = alt2

            if loq_opo_y != loq_opo_y2 and loq_opo_y != loq_opo_y3:
                if loq_opo_y != loq_opo_y4 and loq_opo_y != loq_opo_y5:
                    pygame.draw.rect(tela, PRETO, oponenteY)

            if loq_opo_y2 != loq_opo_y3 and loq_opo_y2 != loq_opo_y:
                if loq_opo_y2 != loq_opo_y4 and loq_opo_y2 != loq_opo_y5:
                    pygame.draw.rect(tela, ROXO, oponenteY2)

            if loq_opo_y3 != loq_opo_y2 and loq_opo_y3 != loq_opo_y:
                if loq_opo_y3 != loq_opo_y4 and loq_opo_y3 != loq_opo_y5:
                    pygame.draw.rect(tela, AZUL, oponenteY3)

            if loq_opo_y4 != loq_opo_y2 and loq_opo_y4 != loq_opo_y3:
                if loq_opo_y4 != loq_opo_y and loq_opo_y4 != loq_opo_y5:
                    pygame.draw.rect(tela, VERDE, oponenteY4)

            if loq_opo_y5 != loq_opo_y2 and loq_opo_y5 != loq_opo_y3:
                if loq_opo_y5 != loq_opo_y and loq_opo_y5 != loq_opo_y4:
                    pygame.draw.rect(tela, LARANJA, oponenteY5)

        #Oponentes baixo pra cima
            if loq_opo_x != loq_opo_x2 and loq_opo_x != loq_opo_x3 and loq_opo_x != loq_opo_x4:
                pygame.draw.rect(tela, PRETO, oponenteX)

            if loq_opo_x2 != loq_opo_x3 and loq_opo_x2 != loq_opo_x and loq_opo_x2 != loq_opo_x4:
                pygame.draw.rect(tela, ROXO, oponenteX2)

            if loq_opo_x3 != loq_opo_x2 and loq_opo_x3 != loq_opo_x and loq_opo_x3 != loq_opo_x4:
                pygame.draw.rect(tela, AZUL, oponenteX3)

            if loq_opo_x4 != loq_opo_x2 and loq_opo_x4 != loq_opo_x3 and loq_opo_x4 != loq_opo_x:
                pygame.draw.rect(tela, VERDE, oponenteX4)

    #Cria a tela de GAME OVER
        if str(0) in str(quant_vida):
            tela.blit(GAME_OVER, [300, 200])
            tela.blit(GAME_OVER2, [170, 400])

    #Cria as barreiras
        for pad in pads:
            pygame.draw.rect(tela, VERMELHO, pad)

    #Colisão personagem/barreira
        if personagem.collidelist(pads) >= 0:
            personagem = pygame.Rect(loq_prota_x, loq_prota_y, 20, 20)
            quant_vida -= 1
            num_vida = font1.render(str(quant_vida), True, PRETO)

    #Colisões personagem/oponentes
        if personagem.colliderect(oponenteY):
            personagem = pygame.Rect(loq_prota_x, loq_prota_y, 20, 20)
            if quant_vida > 0:
                quant_vida -= 1
            num_vida = font1.render(str(quant_vida), True, PRETO)

        if personagem.colliderect(oponenteY2):
            personagem = pygame.Rect(loq_prota_x, loq_prota_y, 20, 20)
            if quant_vida > 0:
                quant_vida -= 1
            num_vida = font1.render(str(quant_vida), True, PRETO)

        if personagem.colliderect(oponenteY3):
            personagem = pygame.Rect(loq_prota_x, loq_prota_y, 20, 20)
            if quant_vida > 0:
                quant_vida -= 1
            num_vida = font1.render(str(quant_vida), True, PRETO)

        if personagem.colliderect(oponenteY4):
            personagem = pygame.Rect(loq_prota_x, loq_prota_y, 20, 20)
            if quant_vida > 0:
                quant_vida -= 1
            num_vida = font1.render(str(quant_vida), True, PRETO)

        if personagem.colliderect(oponenteY5):
            personagem = pygame.Rect(loq_prota_x, loq_prota_y, 20, 20)
            if quant_vida > 0:
                quant_vida -= 1
            num_vida = font1.render(str(quant_vida), True, PRETO)

        if personagem.colliderect(oponenteX):
            personagem = pygame.Rect(loq_prota_x, loq_prota_y, 20, 20)
            if quant_vida > 0:
                quant_vida -= 1
            num_vida = font1.render(str(quant_vida), True, PRETO)

        if personagem.colliderect(oponenteX2):
            personagem = pygame.Rect(loq_prota_x, loq_prota_y, 20, 20)
            if quant_vida > 0:
                quant_vida -= 1
            num_vida = font1.render(str(quant_vida), True, PRETO)

        if personagem.colliderect(oponenteX3):
            personagem = pygame.Rect(loq_prota_x, loq_prota_y, 20, 20)
            if quant_vida > 0:
                quant_vida -= 1
            num_vida = font1.render(str(quant_vida), True, PRETO)

        if personagem.colliderect(oponenteX4):
            personagem = pygame.Rect(loq_prota_x, loq_prota_y, 20, 20)
            if quant_vida > 0:
                quant_vida -= 1
            num_vida = font1.render(str(quant_vida), True, PRETO)

    #COlisões oponentes/barreiras
        if oponenteY.collidelist(pads) >= 0:
            oponenteY.x = 50
            oponenteY.y = loq_opo_y

        if oponenteY2.collidelist(pads) >= 0:
            oponenteY2.x = 50
            oponenteY2.y = loq_opo_y2

        if oponenteY3.collidelist(pads) >= 0:
            oponenteY3.x = 50
            oponenteY3.y = loq_opo_y3

        if oponenteY4.collidelist(pads) >= 0:
            oponenteY4.x = 50
            oponenteY4.y = loq_opo_y4

        if oponenteY5.collidelist(pads) >= 0:
            oponenteY5.x = 50
            oponenteY5.y = loq_opo_y5

        if oponenteX.collidelist(pads) >= 0:
            oponenteX.y = 630
            oponenteX.x = loq_opo_x

        if oponenteX2.collidelist(pads) >= 0:
            oponenteX2.y = 630
            oponenteX2.x = loq_opo_x2

        if oponenteX3.collidelist(pads) >= 0:
            oponenteX3.y = 630
            oponenteX3.x = loq_opo_x3

        if oponenteX4.collidelist(pads) >= 0:
            oponenteX4.y = 630
            oponenteX4.x = loq_opo_x4

    #Cria o texto na tela de vida e etc
        tela.blit(texto_vida, [22, 10])
        tela.blit(num_vida, [220, 10])
        tela.blit(texto_round, [350, 10])
        tela.blit(num_round, [520, 10])
        tela.blit(texto_tempo, [650, 10])
        tela.blit(num_tempo, [820, 10])

    #Faz com que o tempo resete e adicione mais 1 ao tempo dos oponentes
        if quant_vida > 0:
            if tempo == 60:
                tempo = 0
                tempoO += 1
                tempoU += 1
                num_tempo = font1.render(str(tempoU), True, PRETO)
        #Atualiza o tempo
            tempo += 1
        if not ii("Saia.jpg"):
            sair = True
    #Atualiza a téla
        pygame.display.flip()
