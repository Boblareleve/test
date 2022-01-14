import pygame
import claa

# x:600 y:640
if True :
    pygame.init()
    screen = pygame.display.set_mode((600,640))
    pygame.display.set_caption("space invader")
    icon = pygame.image.load("logo.png")
    pygame.display.set_icon(icon)
running=True
ennemies = []


basique = claa.ennemie_type(4,"logo.png")

P=claa.player()



def addEnnemie(type):
    x = 300-(basique.claa.ennmie_type.w/2)
    for i in ennemies:
        if x<=i.posx<=x+(i.w/2):
            x=(x+40)%600
            if 0<=i.posy<=i.h:
                y=0
            else:
                break
        else:
            break
    e = claa.ennemie(type, x,y)
    ennemies.append(e)

addEnnemie(basique)
addEnnemie(basique)

while running :
    hchan=0
    bchan=0
    gchan=0
    dchan=0
    moment=0
    while moment==0:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                moment=2
            if event.type == pygame.MOUSEBUTTONDOWN:
                mx,my=pygame.mouse.get_pos()
                if 0<=mx<=600 and 0<=my<=640:
                    if event.button == 1:
                        moment=1
    while moment==1 :
        screen.fill((0,0,0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                moment=2
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    gchan=1
                if event.key == pygame.K_d:
                    dchan=1
                if event.key == pygame.K_z:
                    hchan=1
                if event.key == pygame.K_s:
                    bchan=1
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_d:
                    dchan=0
                if event.key == pygame.K_q:
                    gchan=0
                if event.key == pygame.K_z:
                    hchan=0
                if event.key == pygame.K_s:
                    bchan=0
                if event.key == pygame.K_p :
                    addEnnemie(basique)
    
        P.dépgauche(gchan)
        P.dépdroite(dchan)
        P.dépbas(bchan)
        P.déphaut(hchan)

        screen.blit(P.image,(P.posx,P.posy))
        for i in ennemies:
            i.IA_tick()
            screen.blit(i.getImage(),(i.getPosx(),i.getPosy()))

        pygame.display.update()
