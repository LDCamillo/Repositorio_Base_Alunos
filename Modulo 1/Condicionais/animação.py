import pygame

pygame.init()

largura, altura = 800,600
tela = pygame.digital.set_mode((largura, altura))
relogio = pygame.time.Clock()

x = 50
y = 50
velocidade_x = 5
velocidade_y = 5
largura_ret, altura_ = 50,50

rodando = True

while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

x += velocidade_x
y += velocidade_y


if x + largura_ret > largura