#Ander Varuskin IS22
import pygame #impordib pygame




pygame.init() #pygame käivitamine




screen=pygame.display.set_mode([300,300]) #määrab akna suuruse
pygame.display.set_caption("Lumememm - Varuskin") #paneb aknale/tööle nime

screen.fill((153, 204, 255)) # helesinine taust



pygame.draw.circle(screen, [255, 255, 255], [150,115], 35, 0) #joonistab lumememme ülemise palli ehk pea
pygame.draw.circle(screen, [255, 255, 255], [150,180], 40, 0) #joonistab lumememme keskmise palli ehk kõhu
pygame.draw.circle(screen, [255, 255, 255], [150,250], 45, 0) #joonistab lumememme alumise palli ehk jala(d)
pygame.draw.circle(screen, [0, 0, 0], [134,105], 4, 0) #joonistab vasakpoolse silma
pygame.draw.circle(screen, [0, 0, 0], [165,105], 4, 0) #joonistab parempoolse silma

pygame.draw.polygon(screen, [228, 114, 0], [[145,110],[155,110],[150,135]]) #joonistab porgandi ehk nina


pygame.draw.circle(screen, [0, 0, 0], [150, 200], 5, 0) #loob esimese nööbi
pygame.draw.circle(screen, [0, 0, 0], [150, 180], 5, 0) #loob teise nööbi
pygame.draw.circle(screen, [0, 0, 0], [150, 160], 5, 0) #loob kolmanda nööbi

pygame.draw.rect(screen, [0, 0, 0], [120.5, 50, 61.5, 25], 0) #Kübara esimene osa
pygame.draw.rect(screen, [0, 0, 0], [118, 70, 65, 25], 0) #Kübara teine osa
pygame.draw.rect(screen, [255, 25, 25], [120.5, 60, 61.5, 10], 0) #Kübara punane osa

pygame.draw.line(screen, [0, 0, 0], [118, 160], [90, 130]) #Esimene käsi
pygame.draw.line(screen, [0, 0, 0], [210, 172], [176, 150]) #Teine käsi

pygame.draw.line(screen, [0, 0, 0], [90, 122], [55, 250]) #Harja kepp
pygame.draw.rect(screen, [0, 0, 0], [47, 245, 20, 10], 0) #Harja esimene osa
pygame.draw.rect(screen, [140, 96, 70], [33, 250, 50, 15], 0) #Harja teine osa

pygame.draw.circle(screen, [250, 228, 27], [300, 10], 30, 0) #Päikese loomine
pygame.draw.line(screen, [250, 228, 27], [300, 10], [200, 15]) #Esimese päikesekiire loomine
pygame.draw.line(screen, [250, 228, 27], [300, 20], [200, 40]) #Teise päikesekiire loomine
pygame.draw.line(screen, [250, 228, 27], [300, 30], [200, 70]) #Kolmanda päikesekiire loomine


pygame.display.flip()

run = True
while run:
  for event in pygame.event.get():
      if event.type == pygame.QUIT:
          run = False



  pygame.display.update()




pygame.quit()