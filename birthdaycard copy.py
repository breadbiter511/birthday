import pygame
import time
pygame.mixer.init()
pygame.init()

WIDTH = 600
HEIGHT = 600

background = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("birthday greeting")

img = pygame.image.load("birthday animation\card.jpg")
image = pygame.transform.scale(img,(WIDTH,HEIGHT))
birthday_sound = pygame.mixer.Sound("birthday animation\happy-birthday-155461 (2).mp3")
while True :
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            pygame.quit()
    font = pygame.font.SysFont("Arial",30)
    text = font.render("happy birthday",True,"black")
    text2 = font.render("good luck",True,"black")
    text3 = font.render("here is some cake",True,"black")
    
    background.fill("white")
    background.blit(image,(0,0))
    background.blit(text,(200,200))
    birthday_sound.play()
    pygame.display.update()
    time.sleep(2)
    
    img2 = pygame.image.load("birthday animation\preasent.jpg")
    background.blit(img2,(0,0))
    background.blit(text2,(200,300))
    pygame.display.update()
    time.sleep(2)

    img3 = pygame.image.load("birthday animation\cake.jpg")
    background.blit(img3,(0,0))
    background.blit(text3,(200,500))
    pygame.display.update()
    time.sleep(2)
    
            


               