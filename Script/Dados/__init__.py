import pygame
from random import randint
from random import choice

#Resolução
reso = (980, 720)

#recomecar
recomecar = False
tempo = 0
Round = 1
tempoU = 0
cont = 0

#Protagonista
quant_vida = 3
vel = 3
vel_x = 0
vel_y = 0
loq_prota_x = 420
loq_prota_y = 340
personagem = pygame.Rect(loq_prota_x, loq_prota_y, 20, 20)

#Barreiras
left_pad = pygame.Rect(-1, -1, 30, 730)
right_pad = pygame.Rect(950, 1, 30, 730)
up_pad = pygame.Rect(-1, -1, 990, 30)
down_pad = pygame.Rect(-1, 690, 990, 30)

#Oponente
velO = 3
velO2 = 4
velO3 = 5
velO4 = 2
velO5 = 9

alt = 25
lar = 35

loq_opo_y = randint(30, 300)
loq_opo_y2 = randint(480, 680)
loq_opo_y3 = randint(240, 450)
loq_opo_y4 = choice([randint(40, 80), randint(550, 680)])
loq_opo_y5 = randint(50, 680)
loq_opoe_x = 50



tempoO = 1

oponenteY = pygame.Rect(loq_opoe_x, loq_opo_y, lar, alt)
oponenteY2 = pygame.Rect(loq_opoe_x, loq_opo_y2, lar, alt)
oponenteY3 = pygame.Rect(loq_opoe_x, loq_opo_y3 + 40, lar, alt)
oponenteY4 = pygame.Rect(loq_opoe_x, loq_opo_y4, lar, alt)
oponenteY5 = pygame.Rect(loq_opoe_x, loq_opo_y4 - 40, lar, alt)


velP = 4
velP2 = 2
velP3 = 3
velP4 = 6


alt2 = 35
lar2 = 25

loq_opox_y = 630
loq_opo_x = randint(420, 650)
loq_opo_x2 = randint(540, 950)
loq_opo_x3 = randint(80, 450)
loq_opo_x4 = choice([randint(50, 150), randint(800, 950)])

oponenteX = pygame.Rect(loq_opo_x, loq_opox_y, lar2, alt2)
oponenteX2 = pygame.Rect(loq_opo_x2, loq_opox_y, lar2, alt2)
oponenteX3 = pygame.Rect(loq_opo_x3, loq_opox_y, lar2, alt2)
oponenteX4 = pygame.Rect(loq_opo_x3, loq_opox_y, lar2, alt2)

