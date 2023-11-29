import pygame
import pytmx
import pyscroll

from player import Player

#creation de la class Game pour creer la fenetre
class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((800, 800))
        pygame.display.set_caption("Pythemon by mbm")

        tmx_data = pytmx.util_pygame.load_pygame('carte.tmx')
        map_data = pyscroll.data.TiledMapData(tmx_data)
        map_layer = pyscroll.orthographic.BufferedRenderer(map_data, self.screen.get_size())
        map_layer.zoom = 2

#position du joueur a modif
        #self.player = Player(coordonées x et y ) ou bien avec tiled :
        player_position = tmx_data.get_object_by_name("player")
        self.player = Player(player_position.x, player_position.y)


        self.group = pyscroll.PyscrollGroup(map_layer, default_layer=3)
        self.group.add(self.player)

#les touches du perso pr bouger

    def handle_input(self):
        pressed = pygame.key.get_pressed()

        if pressed[pygame.K_UP]:
            print("haut")
        elif pressed[pygame.K_DOWN]:
            print("bas")
        elif pressed[pygame.K_LEFT]:
            print("gauche")
        elif pressed[pygame.K_RIGHT]:
            print("droite")
#des le lancement faut faire des actualistaions pr que le jeu soit bien et que si le jeu est fermé on actualise plus
    def run(self):

        running = True

        while running:


            self.handle_input()
            self.group.update()
            self.group.center(self.player.rect)
            self.group.draw(self.screen)
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

        pygame.quit()