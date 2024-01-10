import pygame as pg
from random import randrange



## Definir o Taamanho da Janela do Jogo
WINDOW = 750
TILE_SIZE = 50
RANGE = (TILE_SIZE//2, WINDOW-TILE_SIZE//2, TILE_SIZE)


## Funções de Auxilio
get_random_position = lambda: [randrange(*RANGE), randrange(*RANGE)] ## Gerar Posições aleatórias com o tamanho de TILE


time, time_step = 0, 110 ## Controlar a Velocidade dos objetos
lenght = 1 ## Tamanho da Cobra 
screen = pg.display.set_mode([WINDOW]*2) ## Resolução da Janela a ser gerada
clock = pg.time.Clock() ## Ticks do Jogo. a.k.a controle de atualização de frames da tela
dirs = {pg.K_w: 1, pg.K_s: 1, pg.K_a: 1, pg.K_d: 1} ## Controle de Direção da Cobra 


##Cobra 
snake = pg.rect.Rect([0,0, TILE_SIZE -2, TILE_SIZE-2]) ## Gerar a Cobra
snake.center = get_random_position() ## Colocar a cobra em uma posição aleatória na tela
snake_dir = (0,0) ## Direção da Cobra

# Comida 
food = snake.copy() ## Copiar as Caracteristicas da Cobra
food.center = get_random_position() ## Gerar a comida em uma posição aleatória

segments = [snake.copy()] ## Copiar e Controlar as caracterisiticas da cobra ao comer a comida


## Loop principal do Jogo, fazer as atualizações dos frames a cada segundo
while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()

        ## Controles de Movimento da Cobras
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_w and dirs[pg.K_w]:
                snake_dir = (0, -TILE_SIZE)
                dirs = {pg.K_w: 1, pg.K_s: 0, pg.K_a: 1, pg.K_d: 1}

            if event.key == pg.K_s and dirs[pg.K_s]:
                snake_dir = (0,TILE_SIZE)
                dirs = {pg.K_w: 0, pg.K_s: 1, pg.K_a: 1, pg.K_d: 1}

            if event.key == pg.K_a and dirs[pg.K_a]:
                snake_dir = (-TILE_SIZE,0)
                dirs = {pg.K_w: 1, pg.K_s: 1, pg.K_a: 1, pg.K_d: 0}

            if event.key == pg.K_d and dirs[pg.K_d]:
                snake_dir = (TILE_SIZE,0)
                dirs = {pg.K_w: 1, pg.K_s: 1, pg.K_a: 0, pg.K_d: 1}

        if snake.center == food.center:
            food.center = get_random_position()
            lenght+=1
                
        ## Pintar o Fundo de Preto
        screen.fill('black')
   

        ## Regras do Jogo

        ## Não poder se encostar dentro do proprio corpo 
        self_eating = pg.Rect.collidelist(snake, segments[:-1]) != -1

        # Verificar se ela encostou em alguma borda ou em si mesma
        if snake.left < 0 or snake.right > WINDOW or snake.top < 0 or snake.bottom > WINDOW or self_eating:
            snake.center, food.center = get_random_position(), get_random_position()
            lenght, snake_dir = 1, (0,0)
            segments = [snake.copy()]    

        ## Desenhar a cobra na Tela, na cor verde e todos os seus segmentos 
        [pg.draw.rect(screen, 'green', segment) for segment in segments ]
        pg.draw.rect(screen, 'red', food)


        time_now = pg.time.get_ticks()

        
        """
         Atualizar a cada determinado número de Ticks
         a tela do Jogo
        """
        
        
        if time_now - time > time_step:
            time = time_now
            snake.move_ip(snake_dir)
            segments.append(snake.copy())
            segments = segments[-lenght:]

        pg.display.flip()
        clock.tick(60)
    