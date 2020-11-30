import time, pygame
from joueur import *
from constantes import *
from labyrinthe import *
# https://fr.wikibooks.org/wiki/Pygame/Version_imprimable
# https://www.pygame.org/docs/ref/key.html#pygame.key.name
# https://github.com/TheAwesomePossum/StartPy/blob/3d6c824259fdf4e9e78e3138d2c9c0fecedf645f/Events.py
# https://www.pygame.org/docs/ref/key.html#pygame.key.get_pressed

pygame.init()

screen = pygame.display.set_mode(size)

''' on divise la taille du personnage par 4 et on le tourne de 0 degre'''
pygame.key.set_repeat(60, 60)
# grid=createLaby(0,tailleLabyCube,tailleLabyCube,3,3)
grids=createCubicLaby(tailleLabyCube)

perso = Joueur(grids[0][1][0])
#persovar = perso.get_rect()
#persovar = persovar.move([posInitPlayerX,posInitPlayerY])
#perso = pygame.transform.rotozoom(perso, 0, sizePlayer)

layerToPrint=0



while 1:
    
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        layerToPrint=perso.movejoueur(grids,layerToPrint)

    screen.fill(BLACK)
    
    printNeighbLabysCubicLaby(grids,screen,layerToPrint)
    perso.printPerso(screen)
    # printLabyGrayScale(grid[0],screen,"start",9,9,500)
    # printLabyGrayScale(grid[0],screen,"end",9,9,500,400)
    # printLaby(grid[0],screen,9,9)
    # screen.blit(perso, persovar)

    pygame.display.flip()
    pygame.event.get()
    time.sleep(0.05)
