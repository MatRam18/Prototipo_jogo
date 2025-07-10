#Importações
import pygame
from random import randint
from random import choice

#Resolução
larguraT = 980
alturaT = 720
res_tela = (larguraT, alturaT)


primeira_vez = True

def set_prime(valor: bool):
    global primeira_vez
    primeira_vez = valor

home_call = False
game_call = False
gameover_call = False

def set_call(call: int, valor: bool):
    global gameover_call, game_call, home_call
    if call == 1:
        home_call = valor
    elif call == 2:
        game_call = valor
    elif call == 3:
        gameover_call = valor

#recomecar
recomecar = False
mili_seg = 0
rounds = 1
segundos = 0
tempo_round = 0

#Protagonista (Rato)

#invencibilidade
tempo_inven = 3
inven = False

#Vida
vida = 6

#Velocidade
velRat = 3
velRatx = 0
velRaty = 0

#Localização do rato
loq_rato_x = 480
loq_rato_y = 340

#Tamanho do rato
alturaR = 35
larguraR = 40

#Criação da imagem do rato
rato_img = pygame.image.load("Assents/image/Rato1.png")
rato = rato_img.get_rect(center= [loq_rato_x, loq_rato_y])
rato_img = pygame.transform.scale(rato_img, [larguraR, alturaR])


#Barreiras
left_pad = pygame.Rect(-1, -1, 30, 730)
right_pad = pygame.Rect(950, 1, 30, 730)
up_pad = pygame.Rect(-1, -1, 990, 30)
down_pad = pygame.Rect(-1, 690, 990, 30)


#Oponente vertical

#Velocidade do oponente
velVerRx = 3
velVerAz = 4
velVerVm = 5
velVerVr = 2
velVerLr = 9

#Autura e largura do oponente
alturaV = 30
larguraV = 70

#Localização do oponente
loq_bilV_yRx = randint(30, 300)
loq_bilV_yAz = randint(480, 680)
loq_bilV_yVm = randint(240, 450)
loq_bilV_yVr = choice([randint(40, 80), randint(550, 680)])
loq_bilV_yLr = rato.y
loq_bilV_x = 50

#Tempo?
tempo_opo = 1
tem_apa = True

#Imagem e geração dos oponentes

#Laranja
bil_img_esq_laranja = pygame.image.load("Assents/image/BilEsqLarP.png")
bill_esq_laranja = bil_img_esq_laranja.get_rect(left= loq_bilV_x, top= loq_bilV_yLr)
bil_img_esq_laranja = pygame.transform.scale(bil_img_esq_laranja, [larguraV, alturaV])

#Azul
bil_img_esq_azul = pygame.image.load("Assents/image/BilEsqAzuP.png")
bill_esq_azul = bil_img_esq_azul.get_rect(left= loq_bilV_x, top= loq_bilV_yAz)
bil_img_esq_azul = pygame.transform.scale(bil_img_esq_azul, [larguraV, alturaV])

#Roxo
bil_img_esq_roxo = pygame.image.load("Assents/image/BilEsqRoxP.png")
bill_esq_roxo = bil_img_esq_roxo.get_rect(left= loq_bilV_x, top= loq_bilV_yRx)
bil_img_esq_roxo = pygame.transform.scale(bil_img_esq_roxo, [larguraV, alturaV])

#Verde
bil_img_esq_verde = pygame.image.load("Assents/image/BilEsqVerdP.png")
bill_esq_verde = bil_img_esq_verde.get_rect(left= loq_bilV_x, top= loq_bilV_yVr)
bil_img_esq_verde = pygame.transform.scale(bil_img_esq_verde, [larguraV, alturaV])

#Vermelho
bil_img_esq_vermelho = pygame.image.load("Assents/image/BilEsqVermP.png")
bill_esq_vermelho = bil_img_esq_vermelho.get_rect(left= loq_bilV_x, top= loq_bilV_yVm)
bil_img_esq_vermelho = pygame.transform.scale(bil_img_esq_vermelho, [larguraV, alturaV])


#Oponente Horizontal

#Velocidade do oponente
velHorAm = 4
velHorSa = 2
velHorRo = 3
velHorCi = 6

#Autura e largura do oponente
alturaH = 70
larguraH = 30

#Localização do oponente
loq_bilH_y = 630
loq_billH_xAm = randint(420, 650)
loq_bilH_xSa = randint(540, 950)
loq_bilH_xRo = randint(80, 450)
loq_bilH_xCi = choice([randint(50, 150), randint(800, 950)])

#Imagem e geração dos oponentes

#Salmão
bil_img_ret_salmao = pygame.image.load("Assents/image/BilRetSalP.png")
bill_ret_salmao = bil_img_ret_salmao.get_rect(left= loq_bilH_xSa, top= loq_bilH_y)
bil_img_ret_salmao = pygame.transform.scale(bil_img_ret_salmao, [larguraH, alturaH])

#Rosa
bil_img_ret_rosa = pygame.image.load("Assents/image/BilRetRosP.png")
bill_ret_rosa = bil_img_ret_rosa.get_rect(left= loq_bilH_xRo, top= loq_bilH_y)
bil_img_ret_rosa = pygame.transform.scale(bil_img_ret_rosa, [larguraH, alturaH])

#Ciano
bil_img_ret_ciano = pygame.image.load("Assents/image/BilRetCiaP.png")
bill_ret_ciano = bil_img_ret_ciano.get_rect(left= loq_bilH_xCi, top= loq_bilH_y)
bil_img_ret_ciano = pygame.transform.scale(bil_img_ret_ciano, [larguraH, alturaH])

#Amarelo
bil_img_ret_amarelo = pygame.image.load("Assents/image/BilRetAmaP.png")
bill_ret_amarelo = bil_img_ret_amarelo.get_rect(left= loq_billH_xAm, top= loq_bilH_y)
bil_img_ret_amarelo = pygame.transform.scale(bil_img_ret_amarelo, [larguraH, alturaH])


#Parte que define as váriaveis do jogo
p_recomecar = p_mili_seg = p_rounds = p_segundos = p_cont = p_tempo_round = p_tempo_inven = p_inven = p_vida = ""
p_velVerRx = p_velVerAz = p_velVerVm = p_velVerVr = p_velVerLr = ""
p_alturaV = p_larguraV = ""
p_loq_bilV_yRx = p_loq_bilV_yAz = p_loq_bilV_yVm = p_loq_bilV_yVr = p_loq_bilV_yLr = p_loq_bilV_x = ""
p_bill_esq_laranja = p_bil_img_esq_laranja = ""
p_bill_esq_azul = p_bil_img_esq_azul = p_bill_esq_roxo = p_bil_img_esq_roxo = ""
p_bill_esq_verde = p_bil_img_esq_verde = p_bill_esq_vermelho = p_bil_img_esq_vermelho = ""
p_velHorAm = p_velHorSa = p_velHorRo = p_velHorCi = ""
p_alturaH = p_larguraH = ""
p_loq_bilH_y = p_loq_billH_xAm = p_loq_bilH_xSa = p_loq_bilH_xRo = p_loq_bilH_xCi = ""
p_bill_ret_salmao = p_bil_img_ret_salmao = p_bill_ret_rosa = p_bil_img_ret_rosa = p_bill_ret_ciano = ""
p_bil_img_ret_ciano = p_bill_ret_amarelo = p_bil_img_ret_amarelo = ""

