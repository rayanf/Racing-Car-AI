import pygame
import os
import math

pygame.init()


class Game:
    def __init__(self):
        self.w = 1500
        self.h = 800
        self.fps = 10
        self.changeDegree = 10
        self.changeSpeed = 2
        self.screen = pygame.display.set_mode([self.w,self.h])  
        self.screen.fill((50, 153, 213))
        self.clock = pygame.time.Clock()  

        self.cars = []
        self.carsObjects = pygame.sprite.Group()

        

    def add_car(self,pos,img):
        car = Car(pos,img)
        self.cars.append(car)
        self.carsObjects.add(car)

    def one_step(self,moves):
        for i in range(len(self.cars)):
            car = self.cars[i]
            move = moves[i]



    def update_screen(self):
        self.screen.fill((50, 153, 213))

        self.carsObjects.draw(self.screen)        
        pygame.display.update()  
        pygame.display.flip()


class Car(pygame.sprite.Sprite):
    def __init__(self,pos,img):
        pygame.sprite.Sprite.__init__(self)  
        self.image = pygame.image.load(img)
        self.rect = self.image.get_rect()  
        self.rect.center = pos
        self.speed = 0
        self.degree = 0
        self.moves = ['forward', 'left', 'right', 'backward']

    def move(self,move):
        for i in range(1,3):
            if move == self.moves[i]:
                self.degree += game.changeDegree * [-1, 1][i-1]

        if move == self.moves[0]:
            self.speed += game.changeSpeed * 1
        elif move == self.moves[-1]:
            if self.speed > 0:
                self.speed += game.changeSpeed * -1

        self.rect.x += self.speed * math.cos(math.radians(self.degree))
        self.rect.y += self.speed * math.sin(math.radians(self.degree))
        print(self.rect.center)

if __name__ == '__main__':
    game = Game()
    game.add_car((200,200),'car_1.png')
    
    # while True:
    for i in range(10):
        game.cars[0].move('right')
        game.cars[0].move('forward')
        game.update_screen()
        game.clock.tick(game.fps)  

    for i in range(10):
        game.cars[0].move('backward')
        game.update_screen()
        game.clock.tick(game.fps)  

    for i in range(10):
        game.cars[0].move('right')
        game.cars[0].move('forward')
        game.update_screen()
        game.clock.tick(game.fps)  
