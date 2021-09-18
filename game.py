import pygame
import os
import math

pygame.init()


class Game:
    def __init__(self):
        self.w = 1500
        self.h = 800
        self.fps = 20
        self.changeDegree = 10
        self.changeSpeed = 1
                
        ww = pygame.display.Info().current_w
        wh = pygame.display.Info().current_h
        self.screen = pygame.display.set_mode((1200,750))
        self.screen.fill((255,0,0))
        self.screen.blit(pygame.image.load('track.png'),(0,0))
        self.clock = pygame.time.Clock()  

        self.cars = []
        self.carsObjects = pygame.sprite.Group()
        self.track = pygame.image.load('track.png')
        

    def add_car(self,pos,img):
        car = Car(pos,img)
        self.cars.append(car)
        self.carsObjects.add(car)

    def one_step(self,moves):
        for i in range(len(self.cars)):
            car = self.cars[i]
            move = moves[i]
            # if not self.check_road(car.rect.center):
            #     car.speed = 0
                # break

            car.move(move)   

        game.update_screen()


    def update_screen(self):
        self.screen.fill((255, 255, 102))
        self.screen.blit(pygame.image.load('track.png'),(0,0))
        self.screen.blit(self.cars[0].rotatedimage,self.cars[0].rect.center)

        # self.carsObjects.draw(self.screen)        
        pygame.display.update()  
        pygame.display.flip()

    def check_road(self,point):
        clr = self.track.get_at(point)
        # print(clr)
        # print(point)

        if clr == (100,100,100,255): 
            return True
        else: return False

class Car(pygame.sprite.Sprite):
    def __init__(self,pos,color):
        pygame.sprite.Sprite.__init__(self)  
        self.image = pygame.Surface([35,20],pygame.SRCALPHA)
        self.image.fill(color)
        self.rotatedimage = self.image
        self.rect = self.image.get_rect()  
        self.rect.center = pos
        self.speed = 0
        self.degree = 0
        self.moves = ['forward', 'left', 'right', 'backward']

    def move(self,move):
        change_degree = 0
        for i in range(1,3):
            if move == self.moves[i]:
                self.degree += game.changeDegree * [-1, 1][i-1]

        if move == self.moves[0]:
            self.speed += game.changeSpeed * 1
        elif move == self.moves[-1]:
            if self.speed > 0:
                self.speed += game.changeSpeed * -1

        self.rect.x += round(self.speed * math.cos(math.radians(self.degree)))
        self.rect.y += round(self.speed * math.sin(math.radians(self.degree)))

        self.rotatedimage = pygame.transform.rotate(self.image,self.degree*-1)


if __name__ == '__main__':
    color = (100,149,237)
    
    game = Game()
    game.add_car((100,200),color)
    
    # while True:
    for i in range(10):
        game.one_step(['right'])
        game.one_step(['forward'])
        game.clock.tick(game.fps)  

    for i in range(10):
        game.one_step(['backward'])
        game.clock.tick(game.fps)  

    for i in range(10):
        game.one_step(['left'])
        game.one_step(['forward'])
        game.clock.tick(game.fps)  
    for i in range(20):
        game.one_step(['forward'])
        game.clock.tick(game.fps)  