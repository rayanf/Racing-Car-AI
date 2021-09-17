import pygame
import os

pygame.init()


class Game:
    def __init__(self):
        self.w = 1000
        self.h = 1000
        self.fps = 25

        self.screen = pygame.display.set_mode([self.w,self.h])  
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
        self.carsObjects.draw(self.screen)        
        pygame.display.update()  
        pygame.display.flip()


class Car(pygame.sprite.Sprite):
    def __init__(self,pos,img):
        pygame.sprite.Sprite.__init__(self)  
        self.image = pygame.image.load(img)  
        self.rect = self.image.get_rect()  
        self.rect.center = pos


if __name__ == '__main__':
    game = Game()
    game.add_car((200,200),'car_1.png')
    
    while True:
        game.update_screen()