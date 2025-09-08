import pygame

pygame.init()

largura = 800
altura = 600
tela = pygame.display.set_mode((largura, altura))

pygame.display.set_caption("meu primeiro jogo.")

jogando = True

while jogando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            jogando = False

    tela.fill((255,255,255))

    pygame.display.update()

pygame.quit()