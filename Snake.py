import pygame
import time
import random
 
pygame.init()
 
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)
 

disWidth = 400
disHeight = 300
dis = pygame.display.set_mode((disWidth, disHeight))
pygame.display.set_caption('Snake Game by Edureka')
 
clock = pygame.time.Clock()
snakeBlock = 10
snakeSpeed = 15
 
def yourScore( score ):
    font = pygame.font.SysFont( None, 20 )
    s = font.render("Your Score: "+str(score), True, blue)
    dis.blit(s, [0, 0])
def OurSnake( snakeBlock, snakeList ):
    for x in snakeList:
        pygame.draw.rect(dis, black, [x[0], x[1], snakeBlock, snakeBlock])
        
def message( msg, color ):
    font = pygame.font.SysFont( None, 20 )
    mesg = font.render( msg, True, color )
    dis.blit( mesg, [ disWidth/4, disHeight/2 ] )

def gameLoop():
    game_over = False
    game_close = False
    x1 = disWidth / 2
    y1 = disHeight / 2
    x1_change = 0       
    y1_change = 0
    snakeList = []
    LengthOfSnake = 1

    foodx = round( random.randrange( 0, disWidth - snakeBlock) / snakeBlock) * snakeBlock
    foody = round( random.randrange(0, disHeight - snakeBlock) / snakeBlock) * snakeBlock
    
    # 主要遊戲程式
    while not game_over:

        # 當蛇死掉的時候
        while game_close == True:
            dis.fill( black )
            message("YOU lost! Press Q-Quit or C-Play Again", red)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()
        # 遊戲控制  
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snakeBlock
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snakeBlock
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snakeBlock
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snakeBlock
                    x1_change = 0
        # 碰到邊界
        if x1 >= disWidth or x1 < 0 or y1 >= disHeight or y1 < 0:
            game_close = True

        # 遊戲控制後的變數
        x1 += x1_change
        y1 += y1_change
        dis.fill(white)
        pygame.draw.rect(dis, red, [foodx, foody, snakeBlock, snakeBlock]) # 畫食物

        # 畫蛇
        snakeHead = []
        snakeHead.append(x1)
        snakeHead.append(y1)
        snakeList.append(snakeHead)
        if len(snakeList) > LengthOfSnake:
            snakeList.pop(0)
        for x in snakeList[:-2]:
            if x == snakeHead:
                game_close = True
        OurSnake( snakeBlock, snakeList)
        # 畫分數
        yourScore(LengthOfSnake-1)

        pygame.display.update()

        # 蛇碰到食物
        if x1 == foodx and y1 == foody:
            print("Yummy!!")
            foodx = round( random.randrange( 0, disWidth - snakeBlock) / snakeBlock ) * snakeBlock
            foody = round( random.randrange( 0, disHeight - snakeBlock) / snakeBlock ) * snakeBlock
            LengthOfSnake += 1
           

        clock.tick(snakeSpeed)
    
    # 遊戲完全結束後，關起來pygame
    pygame.quit()
    quit() 

    
if __name__ == "__main__":
    gameLoop()


