import pygame

pygame.init()
tela = pygame.display.set_mode([500, 400])
pygame.display.set_caption('Jogo Very Fuck')
frames = pygame.time.Clock()

cor_branca = (255,255,255)
cor_preta = (0, 0, 0)

sair = False
cor = False

while sair != True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            sair = True
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_a:
                cor = True
            if evento.key == pygame.K_d:
                cor = False

    frames.tick(30)
    if cor != True:
        tela.fill(cor_branca)
    else:
        tela.fill(cor_preta)
    pygame.display.update()

pygame.quit()
