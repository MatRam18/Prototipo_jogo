# Importações
from Script.Musica import *
from Script.Tela import gameover
from Script.Textos import *
from Script import *
import Script.Dados as dd
from Script.Tela import menu
from Script.Tela import home

# Começa o jogo
def play(Parar=False):
    # Váriaveis globais
    global velRatx, velRaty, rato

    # Variaveis de pausar
    pause = False
    esc_pause = False

    # Resolução
    p_res_tela = res_tela

    # Imagem do rato
    p_rato_img = rato_img
    velRatx = 0
    velRaty = 0

    # Barreiras
    p_pads = [left_pad, right_pad, up_pad, down_pad]

    # Redefinição das váriaveis restantes

    p_mili_seg = mili_seg
    p_rounds = rounds
    p_segundos = segundos
    p_tempo_round = tempo_round

    # Invencibilidade
    p_vida = vida
    p_tempo_inven = tempo_inven
    p_inven = inven

    # Oponentes verticais

    # Velocidade do oponente
    p_velVerRx = velVerRx
    p_velVerAz = velVerAz
    p_velVerVm = velVerVm
    p_velVerVr = velVerVr
    p_velVerLr = velVerLr

    # Autura e largura do oponente
    p_alturaV = alturaV
    p_larguraV = larguraV

    # Localização do oponente
    p_loq_bilV_yRx = loq_bilV_yRx
    p_loq_bilV_yAz = loq_bilV_yAz
    p_loq_bilV_yVm = loq_bilV_yVm
    p_loq_bilV_yVr = loq_bilV_yVr
    p_loq_bilV_yLr = loq_bilV_yLr
    p_loq_bilV_x = loq_bilV_x

    # Laranja
    p_bill_esq_laranja = bill_esq_laranja
    p_bil_img_esq_laranja = bil_img_esq_laranja

    # Azul
    p_bill_esq_azul = bill_esq_azul
    p_bil_img_esq_azul = bil_img_esq_azul

    # Roxo
    p_bill_esq_roxo = bill_esq_roxo
    p_bil_img_esq_roxo = bil_img_esq_roxo

    # Verde
    p_bill_esq_verde = bill_esq_verde
    p_bil_img_esq_verde = bil_img_esq_verde

    # Vermelho
    p_bill_esq_vermelho = bill_esq_vermelho
    p_bil_img_esq_vermelho = bil_img_esq_vermelho


    # Oponente Horizontal

    # Velocidade do oponente
    p_velHorAm = velHorAm
    p_velHorSa = velHorSa
    p_velHorRo = velHorRo
    p_velHorCi = velHorCi

    # Autura e largura do oponente
    p_alturaH = alturaH
    p_larguraH = larguraH

    # Localização do oponente
    p_loq_bilH_y = loq_bilH_y
    p_loq_billH_xAm = loq_billH_xAm
    p_loq_bilH_xSa = loq_bilH_xSa
    p_loq_bilH_xRo = loq_bilH_xRo
    p_loq_bilH_xCi = loq_bilH_xCi

    # Imagem e geração dos oponentes

    # Salmão
    p_bill_ret_salmao = bill_ret_salmao
    p_bil_img_ret_salmao = bil_img_ret_salmao

    # Rosa
    p_bill_ret_rosa = bill_ret_rosa
    p_bil_img_ret_rosa = bil_img_ret_rosa

    # Ciano
    p_bill_ret_ciano = bill_ret_ciano
    p_bil_img_ret_ciano = bil_img_ret_ciano

    # Amarelo
    p_bill_ret_amarelo = bill_ret_amarelo
    p_bil_img_ret_amarelo = bil_img_ret_amarelo

    # Inicia o pygame e outros detalhes
    pygame.init()
    tela = pygame.display.set_mode(p_res_tela)
    pygame.display.set_caption('Game Principal')
    pygame.mixer.init()

    # Encerra a música do jogo principal e inicia a música de GameOver
    if dd.primeira_vez:
        musica_home(s=False)
        musica_go(s=False)
        musica_game()
        dd.set_prime(False)

    # Define os frames
    frames = pygame.time.Clock()

    # define a variavel de saida
    sair = Parar

    # Começa o looping da tela
    while not sair:
        # Define os frames em 60 FPS
        frames.tick(60)

        if not dd.game_call:
            # Verifica se a vida é igual a 0, se for, ira para tela de Game Over
            if p_vida == 0:
                dd.set_prime(True)
                gameover.play()
                sair = True

            # Verifica os eventos das teclas
            for evento in pygame.event.get():

                # Verificando as ações das teclas do teclado e botão de fechar e pausar
                if evento.type == pygame.QUIT:
                    sair = True
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_ESCAPE:
                        esc_pause = True
                    if pause and evento.key == pygame.K_ESCAPE:
                        sair = True
                    if pause and evento.key == pygame.K_c:
                        esc_pause = False
                        pause = False
                    if pause and evento.key == pygame.K_t:
                        dd.set_call(2, True)
                        menu.play()
                    if pause and evento.key == pygame.K_q:
                        dd.set_prime(True)
                        home.play()
                        sair = True

                # Faz com que se as teclas estiverem precionadas, ele adicione ou retire a velocidade do rato (movimentação)
                    if evento.key == pygame.K_w or evento.key == pygame.K_UP:
                        velRaty = -velRat
                    if evento.key == pygame.K_s or evento.key == pygame.K_DOWN:
                        velRaty = velRat
                    if evento.key == pygame.K_a or evento.key == pygame.K_LEFT:
                        velRatx = -velRat
                    if evento.key == pygame.K_d or evento.key == pygame.K_RIGHT:
                        velRatx = velRat

                # Faz com que se as teclas não estiverem precionadas, ele adicione 0 a velocidade do rato (movimentação)
                if evento.type == pygame.KEYUP:
                    if evento.key == pygame.K_w or evento.key == pygame.K_UP:
                        velRaty = 0
                    if evento.key == pygame.K_s or evento.key == pygame.K_DOWN:
                        velRaty = 0
                    if evento.key == pygame.K_a or evento.key == pygame.K_LEFT:
                        velRatx = 0
                    if evento.key == pygame.K_d or evento.key == pygame.K_RIGHT:
                        velRatx = 0

            # Verifica se o botão de pause foi clicado
            if esc_pause:
                pause = True

            # Velociade do rato se não estiver pausado
            if not pause:
                rato.x += velRatx
                rato.y += velRaty

            # Deixa a tela em branco
            tela.fill(BRANCO)

            # Muda as imagens do rato enquanto ele estiver invencivel durante 3 segundos
            if p_inven:
                if p_mili_seg == 30:
                    p_rato_img = pygame.image.load("Assents/image/Xerox.png")
                    p_rato_img = pygame.transform.scale(p_rato_img, [larguraR, alturaR])

                if p_mili_seg == 60:
                    p_rato_img = pygame.image.load("Assents/image/Xerox2.png")
                    p_rato_img = pygame.transform.scale(p_rato_img, [larguraR, alturaR])
                    p_tempo_inven -= 1

                if p_tempo_inven < 0:
                    p_inven = inven
                    p_rato_img = rato_img


            # Cria o nosso rato
            tela.blit(p_rato_img, rato)

            # Cria as Barreiras
            for pad in p_pads:
                pygame.draw.rect(tela, VERMELHO, pad)

            # Colisões

            # Colisões Rato, Barreira
            if rato.collidelist(p_pads) >= 0:
                rato = pygame.Rect(loq_rato_x, loq_rato_y, alturaR, larguraR)
                p_tempo_inven = tempo_inven
                p_inven = True
                p_vida -= 1

            # Palhaçadinha :)
            if not ii("Assents/image/Saia.jpg"):
                sair = True

            # Se a tela estiver pausada, ele exibe os textos de pause
            if pause:
                tela.blit(texto_pause, [400, 200])
                tela.blit(texto_pause2, [40, 600])
                tela.blit(texto_pause3, [520, 600])

            # Exibe os textos de vida, round e tempo
            tela.blit(texto_vida, [30, -6])
            tela.blit(num(p_vida), [110, -6])
            tela.blit(texto_round, [420, -6])
            tela.blit(num(p_rounds), [510, -6])

            # Muda a distância do tempo e do número de tempo dependendo da casa decimal
            if p_segundos <= 9:
                tela.blit(texto_tempo, [830, -6])
                tela.blit(num(p_segundos), [930, -6])
            elif p_segundos <= 99:
                tela.blit(texto_tempo, [820, -6])
                tela.blit(num(p_segundos), [920, -6])
            elif p_segundos <= 999:
                tela.blit(texto_tempo, [810, -6])
                tela.blit(num(p_segundos), [910, -6])


            #Contador de segundos
            if p_mili_seg == 60:
                p_segundos += 1
                p_mili_seg = 0
                p_tempo_round += 1
                if p_tempo_round == 10:
                    p_rounds += 1
                    p_tempo_round = tempo_round

            # Se não estiver pausado, adiciona mais 1 para o milisegundo
            if not pause:
                p_mili_seg += 1

        # Atualiza todas as informações da tela
        pygame.display.flip()