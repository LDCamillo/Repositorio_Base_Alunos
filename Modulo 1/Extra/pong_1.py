import pygame
LARGURA, ALTURA = 800, 600
FPS = 60
BRANCO = (255,255,255)
PRETO = (0,0,0)

velocidade_esquerda = 0
velocidade_direita = 0


LARGURA_BARRA, ALTURA_BARRA = 10, 100
VELOCIDADE_BARRA = 7 

TAMANHO_BOLA = 15
VELOCIDADE_BOLA_X = 5
VELOCIDADE_BOLA_Y = 5



pygame.init()
tela = pygame.display.set_mode((LARGURA,ALTURA))
pygame.display.set_caption("Pong Turma 1")
clock = pygame.time.Clock()

barra_esquerda = pygame.Rect(10, (ALTURA - ALTURA_BARRA) // 2, LARGURA_BARRA, ALTURA_BARRA)
barra_direita = pygame.Rect(LARGURA - 10, (ALTURA - ALTURA_BARRA) // 2, LARGURA_BARRA, ALTURA_BARRA)

bola = pygame.Rect((LARGURA - TAMANHO_BOLA) // 2, (ALTURA - TAMANHO_BOLA) // 2, TAMANHO_BOLA, TAMANHO_BOLA)

rodando = True

while rodando:
     for evento in pygame.event.get():
          
          if evento.type == pygame.QUIT:
               rodando = False
          
          if evento.type == pygame.KEYDOWN:
               if evento.key == pygame.K_w:
                    velocidade_esquerda = -VELOCIDADE_BARRA
               if evento.key == pygame.K_s:
                    velocidade_esquerda = VELOCIDADE_BARRA
               if evento.key == pygame.K_UP:
                    velocidade_direita = -VELOCIDADE_BARRA
               if evento.key == pygame.K_DOWN:
                    velocidade_direita = VELOCIDADE_BARRA

          if evento.type == pygame.KEYUP:
               if evento.key == pygame.K_w or evento.key == pygame.K_s:
                   velocidade_esquerda = 0
               if evento.key == pygame.K_UP or evento.key == pygame.K_DOWN:
                    velocidade_direita = 0


     barra_esquerda.y += velocidade_esquerda
     barra_direita.y += velocidade_direita

barra_esquerda.y = max(0, min(ALTURA_TELA))

     tela.fill(PRETO)
     pygame.draw.rect(tela, BRANCO, barra_esquerda)
     pygame.draw.rect(tela, BRANCO, barra_direita)
     pygame.draw.rect(tela, BRANCO, bola)


     #Atualiza clock e display
     pygame.display.flip()
     clock.tick(FPS)


pygame.quit()