#importation des modules necessaires
import pygame
from editor import Editor
from game import Game
from math import atan,pi
#initialisation de la clock et de pygame
clock = pygame.time.Clock()
pygame.init()
#defini le monde a jouer
monde = 1
#lance la classe game
tomber = False
game = Game(tomber,monde,1)
#creer l'ecran
screen = pygame.display.set_mode((1080 + 8, 704))
#initialse la direction du personnage dans les menus
direction = 'droite'
#variable pour l'ecran de chargement
validee = False
chargement = [0,0]
#creation du fond d'ecran de base
bg = pygame.image.load('assets/background/brown.png')
bg = pygame.transform.scale(bg,(1080 + 8, 704))
previ = True
#bouton des setings
button1 = pygame.image.load('assets/menu/menu/Icons_39.png')
buttonO = pygame.image.load('assets/menu/menu/Icons_40.png')
button = pygame.image.load('assets/menu/menu/Icons_40.png')
button1 = pygame.transform.scale2x(button1)
buttonO = pygame.transform.scale2x(buttonO)
button = pygame.transform.scale2x(button)
button_rect = button1.get_rect()
button_rect.x = screen.get_width() - button_rect.width
#variabe pour les levels du monde
level_file_open = 0
#variable pour le jeu
runing = True
boucle = 1
X = 40
x = 0
playing = False
choosing = True
fichier = open('fichier/verify.txt', mode='r+')
fichier.write(str(1))
pose = 0
alerte = False
charge_playing = False
edittoring = False
edit_close_windows = True
#variabe pour le saut du jeu
double_saut = [1,0]
sauter = False
graviter = 0
debut_de_saut = 0
#variable pou le fonctionnement des blocks
nb_porte = 0
nb_terre = 1
portail = 0
nb_portail = 0
roto = 0
#variabe pour les menus
click = [0,0,0]
#variable pour lediteur
editi = 0
monde = 1
taille = 0
#variables pour le menu du monde
level = game.level
levelin = 0
mondein = 1
mov_menu = False
goooo = 'x'
x_or_y = 0
direction_presse = None
xcarte_test = 0
ycarte_test = 0
directt = 'droite'
directionn = 0
x_player = 489
y_player = 267
#variable pour lecran de chargement
boucle_s = [100]
#variable declarer avant detre utilise pour eviter les bug
mouse_x, mouse_y = 10000, 10000
#variable pour la music et volume
placein, placeto, placeto2 = 'menu', 'roux', 'roux'
game.audio.chan1.set_volume(1)
#liste/dico des niveau debloque
unlock_level = [[], {0:True, 1:True,2:False,3:False,4:False,5:False,6:False,7:False,8:False,9:False,10:False,11:False,12:False,'A':True, 'B':True, 'ch':True, 'n15':True, 'n25':True, 'n35':True}]
#variable pour la boutique
skin = game.skin
skin_acheter = game.skin_acheter
#variable des boutons du premier menu
resume_bouton = game.menu.resume_bouton1
restart_bouton = game.menu.restart_bouton1
quit_bouton = game.menu.quit_bouton1
seting_bouton = game.menu.seting_bouton1
#variable des bouton du deuxieme menu
playimage = game.menu.playimage2
levelimage = game.menu.levelimage2
editimage = game.menu.editimage2
boutiqueimage = game.menu.boutiqueimage2
backhome = game.menu.backhome
valide = game.menu.valide1

def fermer_retour_level():#retourn à linterface de base
    global charge_playing,editi,edittoring,nb_portail,playing,nb_porte,portail,x
    game.audio.chan0.play(game.audio.fin_niveau)
    if editi == 1:
        try:
            edit.fermer()
        except:
            pass
        editi = 0
        print(edittoring)
        edittoring = False
        game.editor = True
        game.open = False
    click[0] = 2
    click[1] = 2
    x = 0
    unlock_level[mondein][levelin+1] = True
    if charge_playing == True:
        charge_playing = True
    nb_portail = 0
    portail = 0
    nb_porte = 0
    playing = False


def open_level():#ouvre un niveau
    global validee,charge_playing,Chargement,edit,x,level_file_open,levelin
    Chargement = [1, 100, 0]
    click[0] = 0
    charge_playing = True
    opp = Open()
    level_file_open = 'levelsaved/level '+str(levelin) +'.txt'
    fichh = open(level_file_open, 'r')
    fichh.close()
    game.open = True
    validee = True
    Chargement = [1, 100, 0]

def mouv_background():#deplace l'arriere plan
    if game.background_rect_1.x+game.background_rect_1.width < -game.background_rect_1.width:
        game.background_rect_1.x = game.background_rect_1.width
    if game.background_rect_2.x+game.background_rect_2.width < -game.background_rect_2.width:
        game.background_rect_2.x =game.background_rect_2.width
    if game.background_rect_3.x+game.background_rect_3.width < -game.background_rect_3.width:
        game.background_rect_3.x = game.background_rect_3.width
    screen.blit(background,game.background_rect_1)
    screen.blit(background, game.background_rect_2)
    screen.blit(background, game.background_rect_3)

def selection_monde():#selectionne le monde dans lediteur
    if monde == 1:
        background = pygame.image.load('assets/background/Background.png')
    elif monde == 2:
        background = pygame.image.load('assets/background/feu.png')
    elif monde ==3:
        background = pygame.image.load('assets/background/ice.png')
    elif monde == 4:
        background = pygame.image.load('assets/background/cave.png')
    elif monde == 5:
        background = pygame.image.load('assets/background/RLGMLA.png')
    background = pygame.transform.scale(background, (1080 + 8, 920))
    return background


def playlevel():
    pass


def levelopen(folder):#ouvre un niveau à paritr d'un fichier
    global monde,background
    fichh = open(folder, 'r')
    monde = int(fichh.readline())
    game.__init__(tomber,monde,skin)

    game.open = True
    background = selection_monde()
    game.cree_mat(int(fichh.readline()))
    lines = fichh.readline()
    for i in range(int(lines)):
        cmd = fichh.readline()
        try:
            eval(cmd[0:-1])
        except:
            pass
        #print(str(cmd[0:-1]))
    lines = ''
    fichh.close()
    game.mouv = True
    game.alert = False
    game.start()
    game.playing = True

    for i in range(len(game.blocktab)):
        if game.blocktab[i][4][5] == 3:
            game.player.rect.x = game.blocktab[i][0]
            game.player.rect.y = game.blocktab[i][1] - 58
    game.open = False

#importe les modules necessaires pour l'editeur
from editor import Editor
from levelopen import Open
#variable utlise pour enregistrer le bloc de lediteur selectionner
fk = 0

def chargement(x):#definition de l'ecran de chargement
        screen.blit(pygame.image.load('assets/background/black.png'), (0, 0))
        screen.blit(pygame.transform.scale2x(game.object.coinframe[game.object.coinindex]), (1000, 620))
        screen.blit(pygame.transform.scale2x(game.player.frame[game.player.index]), (500, 300))
        if len(game.object.coinframe) - 1 > game.object.coinindex:
            game.object.coinindex += 1
        else:
            game.object.coinindex = 0
        if len(game.player.frame) - 1 > game.player.index:
            game.player.index += 1
        else:
            game.player.index = 0

        for i in range(round(x/ 10)):
            screen.blit(pygame.transform.scale2x(pygame.image.load('assets/menu/button.png')), (200 + (66 * i), 670))

while runing:#BOUCLE DU JEU
    if edittoring == True:#si l'editeur est activé
        # print('y')
        fk = edit.value_select()#enregistrer ici le bloc selectionner

    fichier = open('fichier/verify.txt', mode='r+')

    nb = int(fichier.readline())
    if nb == 2:
        verify = True
    else:
        verify = False
    fichier.close()




    if playing == False:#quand le jeu n'est pas lancé
        screen.blit(bg, (0, 0))#dessine le fond d'ecran de base
        placein = 'menu'#pour le music, du menu

        if not click[1]==3:
            screen.blit(game.menu.menu_image, game.menu.rect)
            screen.blit(game.menu.name_image, game.menu.namerect)

        elif click[0]==2:
            screen.blit(game.menu.boutiqueimage1,game.menu.boutiqueimage_rect)

        if click[0] == 0:#si il ny a pas de click su rle menu
            #dessine le menu classique
            screen.blit(playimage, game.menu.playrect)
            screen.blit(levelimage, game.menu.levelrect)
            screen.blit(editimage, game.menu.editrect)
            screen.blit(editimage, game.menu.editrect)
            screen.blit(boutiqueimage, game.menu.boutiquerect)

        if click[0] == 2:#verifie si il y a un clique sur le menu
            if click[1]==1:#verifie si le clique sur lediteur
                #dessine l'editeur
                screen.blit(game.menu.open,game.menu.open_rect)
                screen.blit(game.menu.flecheg,game.menu.flecheg_rect)
                screen.blit(game.menu.fleched, game.menu.fleched_rect)
                screen.blit(game.menu.flecheg, game.menu.flecheg_rect2)
                screen.blit(game.menu.fleched, game.menu.fleched_rect2)
                #dessine lediteur en foncion de la teile et du monde
                screen.blit(pygame.transform.scale2x(pygame.image.load("assets/monde/"+str(monde)+".png")),(365,345))
                screen.blit(pygame.image.load("assets/monde/taille.png"), (555, 270))
                screen.blit(pygame.image.load("assets/monde/monde.png"), (260, 270))
                game.menu.nombre(taille, 2, screen, 665, 355,1,24+8,32+8,40)
                #dessine le bouton retour
                screen.blit(valide, game.menu.validerect)
                game.menu.backhomerect.x = 250
                game.menu.backhomerect.y = 150
                screen.blit(backhome, game.menu.backhomerect)


            if click[1]==3:#verifie si le clique est sur la boutique
                placein = 'boutique'#donne la place pour le musique
                game.audio.playing = False #reset la music pour rejouer la bonne
                #init les variables de nouveau pour les skins
                skin = game.skin
                skin_acheter = game.skin_acheter
                #dessine le bouton retour
                game.menu.backhomerect.x = 80
                game.menu.backhomerect.y = 80
                screen.blit(backhome, game.menu.backhomerect)
                #dessine les autres boutons
                screen.blit(game.menu.boutiqueimage56, game.menu.boutiqueimage56_rect)
                screen.blit(game.menu.idem, game.menu.idem_rect)
                screen.blit(game.menu.skin, game.menu.skin_rect)
                screen.blit(game.menu.boule_feu, game.menu.boule_feu_rect)
                screen.blit(game.menu.skin1, game.menu.skin1_rect)
                screen.blit(game.menu.skin2, game.menu.skin2_rect)
                screen.blit(game.menu.skin3, game.menu.skin3_rect)
                #dessine les nombres
                game.menu.nombre(game.coin, 3, screen, 870, 80, 3, 24, 32, 30)

                for i in range(len(game.menu.button_vierge_rect)):#dessine les boutons
                    screen.blit(game.menu.button_vierge,game.menu.button_vierge_rect[i])

                if game.skin == 1:#dessine le bouton du skin 1 en fonction de son utillisation
                    screen.blit(game.menu.valide_true,(game.menu.skin1_rect.x+13, game.menu.skin1_rect.y+73))
                else:
                    screen.blit(game.menu.valide_false, (game.menu.skin1_rect.x + 13, game.menu.skin1_rect.y + 78))


                if game.skin_acheter[2][0] == False:#si le skin 2 n'est pas acheter
                    game.menu.nombre(game.skin_acheter[2][1], 3, screen, game.menu.skin2_rect.x - 25,
                                     game.menu.skin2_rect.y + 80, 3, 24, 32, 30)
                else:
                    if game.skin == 2:#dessine le bouton du skin 2 en fonction de son utillisation
                        screen.blit(game.menu.valide_true, (game.menu.skin2_rect.x + 13, game.menu.skin2_rect.y + 73))
                    else:
                        screen.blit(game.menu.valide_false, (game.menu.skin2_rect.x + 13, game.menu.skin2_rect.y + 78))


                if game.skin_acheter[3][0]==False:#si le skin 3 n'est pas acheter
                    game.menu.nombre(game.skin_acheter[3][1], 3, screen, game.menu.skin3_rect.x-25,
                     game.menu.skin3_rect.y + 80, 3, 24, 32, 30)

                else:
                    if game.skin == 3:#dessine le bouton du skin 3 en fonction de son utillisation
                        screen.blit(game.menu.valide_true, (game.menu.skin3_rect.x + 13, game.menu.skin3_rect.y + 73))
                    else:
                        screen.blit(game.menu.valide_false, (game.menu.skin3_rect.x + 13, game.menu.skin3_rect.y + 78))

                #dessine l'achat des boules de feu
                game.menu.nombre(10, 2, screen, game.menu.boule_feu_rect.x - 15,game.menu.boule_feu_rect.y + 80, 3, 24, 32, 30)



                for event in pygame.event.get(): #boucle pour les events
                    if event.type == pygame.QUIT:#si le joueur quitte
                        running = False
                        quit()
                    if event.type == pygame.MOUSEBUTTONDOWN:#si il clique sur...
                        if game.menu.backhomerect.collidepoint(event.pos): #si il revient en arriere
                            click[0] = 0
                            click[1] = 0
                            boucle_s[0] = 100
                        if click[2] == 0:#si il clique sur...
                            if game.menu.button_vierge_rect[0].collidepoint(event.pos):#le premier skin
                                if not game.skin == 1:
                                    game.skin = 1           #le seleciton si pas deja selectinner
                            if game.menu.button_vierge_rect[1].collidepoint(event.pos): #le deuxieme skin
                                if game.skin_acheter[2][0]==True: #si deja acheter
                                    if not game.skin == 2:
                                        game.skin = 2       #le seleciton si pas deja selectinner
                                else: #sinon pas acheter
                                    if game.coin > game.skin_acheter[2][1]: #achat du skin
                                        game.coin -= game.skin_acheter[2][1]
                                        game.skin_acheter[2][0] = True #achat confirmé
                                        game.skin = 2 #selectinne le skin
                                        game.audio.chan0.play(game.audio.cash) #joue l audio de lachat

                            if game.menu.button_vierge_rect[2].collidepoint(event.pos):#le troisieme skin
                                if game.skin_acheter[3][0]==True: #si deja acheter
                                    if not game.skin == 3:
                                        game.skin = 3       #le seleciton si pas deja selectinner
                                else:  #sinon pas acheter
                                    if game.coin > game.skin_acheter[3][1]: #achat du skin
                                        game.coin -= game.skin_acheter[3][1]
                                        game.skin_acheter[3][0] = True  #achat confirmé
                                        game.skin = 3  #selectinne le skin
                                        game.audio.chan0.play(game.audio.cash) #joue l audio de lachat



            if click[1]==2:#si il lance le 'jeu', le menu monde
                boucle_s[0] += 2 #boucle de chargement
                if boucle_s[0] > 100: #boucle de chargement finie
                    #dessine le bouton retour home
                    screen.blit(game.menu.image_mondes[mondein], game.menu.image_mondes_rect)
                    game.menu.backhomerect.x = 0
                    game.menu.backhomerect.y = 0
                    screen.blit(backhome, game.menu.backhomerect)

                    for event in pygame.event.get(): #prend les evenements pour le clavier
                        if event.type == pygame.QUIT: #si quitte
                            running = False
                            quit()   #alors quitte
                        if event.type == pygame.MOUSEBUTTONDOWN:#si le clique de la souris
                            if game.menu.editrect.collidepoint(event.pos): #d'edit
                                click[0] = 2
                                click[1] = 1
                            if game.menu.backhomerect.collidepoint(event.pos): #de retour
                                click[0] = 0
                                click[1] = 0
                                boucle_s[0] = 100
                        if event.type == pygame.KEYUP: #si une touche est presse puis releve
                            if event.key == pygame.K_RIGHT: #si c'est celle de droite
                                if mov_menu == False: #si bouge
                                    mov_menu = True #ne peut pas bouger pendant le delacement
                                    directionn = 1 #direction droite correspond à 1
                                    # si ce niveau est debloquer
                                    if game.menu.place_monde[mondein][levelin][2][directionn] != None: #si il y a un niveau dans cette direction
                                        if unlock_level[mondein][game.menu.place_monde[mondein][levelin][2][directionn]] or \
                                           str(game.menu.place_monde[mondein][levelin][2][directionn])[0] == 'n' or \
                                           str(game.menu.place_monde[mondein][levelin][2][directionn])[0] == '0':
                                            directt = game.menu.find_direction(mondein, levelin, 'Right') #definit la direction du perso
                                            levelin = game.menu.place_monde[mondein][levelin][2][1] #defini le nouveau niveau

                            if event.key == pygame.K_LEFT:
                                if mov_menu == False: #si bouge
                                    mov_menu = True #ne peut pas bouger pendant le delacement
                                    directionn = 3 #direction gauche correspond à 3
                                    if game.menu.place_monde[mondein][levelin][2][directionn] != None: #si il y a un niveau dans cette direction
                                        # si ce niveau est debloquer
                                        if unlock_level[mondein][game.menu.place_monde[mondein][levelin][2][directionn]] or \
                                           str(game.menu.place_monde[mondein][levelin][2][directionn])[0] == 'n' or \
                                           str(game.menu.place_monde[mondein][levelin][2][directionn])[0] == '0':
                                            # ou si ce n'est pas un niveau jouable
                                            directt = game.menu.find_direction(mondein, levelin, 'Left') #definit la direction du perso
                                            levelin = game.menu.place_monde[mondein][levelin][2][3] #defini le nouveau niveau

                            if event.key == pygame.K_UP:
                                if mov_menu == False: #si bouge
                                    mov_menu = True #ne peut pas bouger pendant le delacement
                                    directionn = 0 #direction dessus correspond à 0
                                    if game.menu.place_monde[mondein][levelin][2][directionn] != None: #si il y a un niveau dans cette direction
                                        if unlock_level[mondein][game.menu.place_monde[mondein][levelin][2][directionn]] or \
                                           str(game.menu.place_monde[mondein][levelin][2][directionn])[0] == 'n' or \
                                           str(game.menu.place_monde[mondein][levelin][2][directionn])[0] == '0':
                                            # si ce niveau est debloquer
                                            # ou si ce n'est pas un niveau jouable
                                            directt = game.menu.find_direction(mondein, levelin, 'Up') #definit la direction du perso
                                            levelin = game.menu.place_monde[mondein][levelin][2][0] #defini le nouveau niveau

                            if event.key == pygame.K_DOWN:
                                if mov_menu == False: #si bouge
                                    mov_menu = True #ne peut pas bouger pendant le delacement
                                    directionn = 2 #direction dessous correspond à 2
                                    # ou si ce n'est pas un niveau jouable
                                    # si ce niveau est debloquer
                                    if game.menu.place_monde[mondein][levelin][2][directionn] != None: #si il y a un niveau dans cette direction
                                        if unlock_level[mondein][game.menu.place_monde[mondein][levelin][2][directionn]] or \
                                           str(game.menu.place_monde[mondein][levelin][2][directionn])[0] == 'n' or \
                                           str(game.menu.place_monde[mondein][levelin][2][directionn])[0] == '0':
                                            directt = game.menu.find_direction(mondein, levelin, 'Down') #definit la direction du perso
                                            levelin = game.menu.place_monde[mondein][levelin][2][2] #defini le nouveau niveau


                            if event.key == pygame.K_SPACE: #si persse a barre espace
                                print(levelin)
                                try:
                                    if levelin != 0: #si le niveau n'ets pas 0
                                        open_level() #ouvrir le niveau
                                except:
                                    pass #sinn passé


                    var_de_deple = 36 #vitesse du perso


                    levelin = game.menu.deplacer_niveau(mondein, levelin, mov_menu, directionn) #defini le prochain niveau si il y a un deplacement automatique (entre le niveau 4 et 5)
                    # change les coordonnee de la carte en fonction du niveau
                    game.menu.image_mondes_rect.x, game.menu.image_mondes_rect.y, mov_menu = \
                                                   game.menu.deplacer_libre(game.menu.image_mondes_rect.x, game.menu.image_mondes_rect.y,\
                                                                            game.menu.place_monde[mondein][levelin][0], game.menu.place_monde[mondein][levelin][1],\
                                                                            var_de_deple, var_de_deple, mov_menu, screen, False)




                    game.menu.position_perso(x_player, y_player, mov_menu, screen, directt) #fait bouger le joueur

                    #print(x_player, y_player, levelin, mov_menu)


                else:
                    chargement(boucle_s[0])

                placein = 'level' #la place etait le menu monde
                game.audio.playing = False #reinit la musique pour faire jouer la nouvelle

        #sortie des menus, monde, edit et boutique

        for event in pygame.event.get():#resevoir tout les action
            if event.type == pygame.QUIT:#si envent et quiter
                running = False#la boucle while se ferme
                quit()
            if event.type == pygame.MOUSEMOTION:#resevoir toute les action de la souris
                if game.menu.backhomerect.collidepoint(event.pos):#si le rectange backhomerect est toucher
                    blackhome = game.menu.backhome2#changer l'image
                else:
                    blackhome = game.menu.backhome#changer limage

                if game.menu.validerect.collidepoint(event.pos):#si le rectange est toucher
                #changer l'image
                    valide = game.menu.valide2
                else:
                    valide = game.menu.valide1


                if game.menu.playrect.collidepoint(event.pos):#si le rectange est toucher
                    #changer l'image
                    playimage = game.menu.playimage
                else:
                    playimage = game.menu.playimage2

                if game.menu.editrect.collidepoint(event.pos):#si le rectange est toucher
                #changer l'image
                    editimage = game.menu.editimage
                else:
                    editimage = game.menu.editimage2
                if game.menu.levelrect.collidepoint(event.pos):#si le rectange est toucher
                #changer l'image
                    levelimage = game.menu.levelimage
                else:
                    levelimage = game.menu.levelimage2

                if game.menu.boutiquerect.collidepoint(event.pos):#si le rectange est toucher
                #changer l'image
                    boutiqueimage = game.menu.boutiqueimage
                else:
                    boutiqueimage = game.menu.boutiqueimage2

            if click[0] == 0:
                if event.type == pygame.MOUSEBUTTONDOWN:#resevoir toute les action de click
                    if game.menu.playrect.collidepoint(event.pos):#si le rectange est clicker
                        click[0] = 2#changer la variable click
                        click[1] = 2#changer la variable click
                        game.player.__init__(game)#reinisaliser la class game


                if event.type == pygame.MOUSEBUTTONDOWN:#resevoir toute les action de click
                    if game.menu.editrect.collidepoint(event.pos):#si le rectange est clicker
                        click[0] = 2#changer la variable click
                        click[1] = 1#changer la variable click
                    if game.menu.boutiquerect.collidepoint(event.pos):#si le rectange est clicker
                        click[0] = 2#changer la variable click
                        click[1] = 3#changer la variable click
                    if game.menu.backhomerect.collidepoint(event.pos):#si le rectange est clicker
                        click[0] = 0#changer la variable click
                        click[1] = 0#changer la variable click
                        boucle_s[0] = 0#changer la variable click



                if event.type == pygame.MOUSEBUTTONDOWN:#resevoir toute les action de click
                    if game.menu.levelrect.collidepoint(event.pos):#si le rectange est clicker

                        try:#essayer

                            charge_playing = True#changer variable
                            opp = Open()#ouvrir une fenetre pour choisir les niveau
                            level_file_open = opp.get_file()#ouvrir le niveau
                            fichh = open(level_file_open, 'r')#ouvrir le fichier
                            x = fichh.readline()#lire la premier ligne
                            fichh.close()#fermer le fichier
                            game.open = True#changer variable
                            Chargement = [1, 100, 0]#changer variable
                            validee = True#changer variable

                        except:
                            pass#passer






            elif click[0]==2:#si click ==2

                if event.type == pygame.MOUSEBUTTONDOWN: #si un bouton de souris est presser

                    if game.menu.backhomerect.collidepoint(event.pos):#si le rectange est clicker
                        click[0] = 0
                        boucle_s[0] = 0
                        monde = 1
                    if game.menu.flecheg_rect.collidepoint(event.pos):#si le rectange est clicker
                        if monde<5:
                            monde += 1
                    if game.menu.fleched_rect.collidepoint(event.pos):#si le rectange est clicker
                        if monde>1:
                            monde -= 1
                    if game.menu.flecheg_rect2.collidepoint(event.pos):#si le rectange est clicker
                        if taille<50:
                            taille += 1
                    if game.menu.fleched_rect2.collidepoint(event.pos):#si le rectange est clicker
                        if taille>0:
                            taille -= 1
                    if game.menu.open_rect.collidepoint(event.pos):#si le rectange est clicker

                        charge_playing = True
                        opp = Open()#ouvrir une fenetre pour choisir le fichier
                        level_file_open = opp.get_file() #ouvrir le fichier
                        fichh = open(level_file_open, 'r')#ovrir le fichier
                        x = fichh.readline()#lire la premier ligne
                        fichh.close()#fermer le fichier
                        game.open = True#changer la variable
                        Chargement = [1, 100, 0]#changer la variable
                        validee = True#changer la variable
                        edittoring = True#changer la variable
                        print("editor")
                        edittoring = True#changer la variable
                        edit = Editor(game)#ouvrir l'editeur
                        print("yaaaaaaaaa")
                        click[0] = 0#changer la variable
                        game.__init__(tomber, monde,skin)#initialiser la class game
                        game.editor = True
                        game.start()
                        game.playing = True





                    if game.menu.validerect.collidepoint(event.pos):#si le rectange est clicker
                        background = selection_monde()
                        Chargement = [1,100,0]
                        validee = True
                        print("editor")
                        edittoring = True

                        edit = Editor(game)#ouvrir l'editeur
                        print("yaaaaaaaaa")

                        click[0] = 0
                        game.skin = skin
                        game.__init__(tomber, monde,skin)
                        game.editor = True
                        game.cree_mat(taille)
                        game.start()
                        game.playing = True











    if charge_playing == True : #charge le level
        if level == 8:
            levelopen('levelsaved/Level 2.txt')#level test
        else:
            try:
                levelopen(level_file_open)
            except FileNotFoundError: #si il ny a pas d efichier trouver
                playing = False #ne joue pas
                #raise FileNotFoundError
        charge_playing = False #ne charge pas
        print(level_file_open)
    if validee == True: #si le fichier est charger
        #lance le chargement
        if Chargement[0] == 1:
            Chargement[2] += 2
            chargement(Chargement[2])
            if Chargement[2] == Chargement[1]:
                Chargement[0] = 0
                playing = True
                validee = False




    if playing == True: #si le jeu est lancée
        placein = 'play' #reinit la place pour la musique

        if game.playing == False:#met en place le jeu
            fermer_retour_level()
        game.variable(skin_acheter,skin)
        for i in range(len(game.matrice)):
            for y in range(len(game.matrice[0])):
                if game.matrice[i][y]>nb_terre:
                    nb_terre = game.matrice[i][y]+1


        if game.player.vie == False:
            sauter = False
            tomber = False
        mouv_background()

        for i in game.all_blockx:
            if i.rect.x + i.rect.width>=0 and i.rect.x<=1088:
                screen.blit(i.image,i.rect)


        if level == 81:
            game.update_level1(screen)
        if level == 812:
            game.update_level2(screen)
        game.update(screen, tomber)
        if click[0] == 0:
            #deplace la rectange
            game.menu.menu_rect.x = 10000
            game.menu.menu_rect.y = 10000
            game.menu.resume_rect.x = 10000
            game.menu.resume_rect.y = 10000
            game.menu.restart_rect.x = 10000
            game.menu.restart_rect.y = 10000
            game.menu.seting_rect.x = 10000
            game.menu.seting_rect.y = 10000
            game.menu.quit_rect.x = 10000
            game.menu.quit_rect.y = 10000
            button_rect.x = screen.get_width() - button_rect.width

        if click[0] == 1:
            #dessine et deplace les boutons de retour
            game.menu.menu_rect.x = 300
            game.menu.menu_rect.y = 100
            game.menu.resume_rect.x = 370
            game.menu.resume_rect.y = 190
            game.menu.restart_rect.x = 370
            game.menu.restart_rect.y = 280
            game.menu.seting_rect.x = 370
            game.menu.seting_rect.y = 370
            game.menu.quit_rect.x = 370
            game.menu.quit_rect.y = 460
            button_rect.x = 10000
            screen.fill(0)
            screen.blit(background,(0,0))
            screen.blit(game.menu.menu,game.menu.menu_rect)
            screen.blit(resume_bouton,game.menu.resume_rect)
            screen.blit(restart_bouton, game.menu.restart_rect)
            screen.blit(quit_bouton, game.menu.quit_rect)
            screen.blit(seting_bouton, game.menu.seting_rect)

        screen.blit(button, button_rect)
        #game.all_block.draw(screen)








        if edittoring==True and previ == True: #si lediteur est actif
            #print(fk)
            placein = 'edit' #init la place pour l music

            #si le bloc selctionner est :
            #    placer le bloc q=suivant les conditions de son pacement
            #   dessine le bloc une fois que son placement est fait

            if fk == 8 : #arbre
                ligne,collone = game.menu.ligne_collone(mouse_x, mouse_y,150,256,0)
                screen.blit(pygame.transform.scale(pygame.image.load("assets/deco_block/Tree2-copy.png"),(150,256)), (64*collone-128+game.avancementT,64*ligne-256))
            if fk == 0: #terre
                if monde == 1:
                    ligne, collone = game.menu.ligne_collone(mouse_x, mouse_y, 150, 256,0)
                    screen.blit(
                        pygame.transform.scale(pygame.image.load("assets/terre/TileSet_02-copy.png"), (64, 64)),(64*(collone-1)+game.avancementT,64*(ligne-1)))
            if fk == 2: #echelle
                if monde == 1:
                    print("yo")
                    ligne, collone = game.menu.ligne_collone(mouse_x, mouse_y, 150, 256,0)
                    screen.blit(pygame.transform.scale(pygame.image.load("assets/echelle-copy.png"), (64, 64)), (64 * (collone - 1)+game.avancementT, 64 * (ligne - 1)))
            if fk == 1: #eau
                if monde == 1:
                    ligne, collone = game.menu.ligne_collone(mouse_x, mouse_y, 150, 256,0)
                    screen.blit(pygame.transform.scale(pygame.image.load("assets/eau/Water1-copy.png"), (64, 64)),
                                (64 * (collone - 1)+game.avancementT, 64 * (ligne - 1)))
            if fk == 5: #platforme du debit de niveau
                ligne, collone = game.menu.ligne_collone(mouse_x, mouse_y, 64, 16,1)
                screen.blit(pygame.transform.scale(pygame.image.load("assets/Start (Idle)-copy.png"), (64, 16)),
                            (64 * (collone - 1)+game.avancementT, 16 * (ligne - 1)))
            if fk == 4: #piece
                ligne, collone = game.menu.ligne_collone(mouse_x, mouse_y, 40, 40, 1)
                screen.blit(pygame.transform.scale(pygame.image.load("assets/objet/coin/Coin1-copy.png"), (32, 32)),
                            (40 * (collone - 1)+game.avancementT, 40 * (ligne - 1)))
            if fk == -3: #porte de fin du niveau
                ligne,collone = game.menu.ligne_collone(mouse_x, mouse_y, 64 + 32, 128, 0)
                screen.blit(pygame.transform.scale(pygame.image.load("assets/porte/dor1-copy.png"), (64+32, 128)),
                            ((64 ) * (collone - 2) + game.avancementT, 64 * (ligne - 2)))
            if fk == 6: #portail
                ligne, collone = game.menu.ligne_collone(mouse_x, mouse_y, 64, 128, 0)
                if portail%2==0: #verifie quel portail est mis
                    screen.blit(pygame.transform.scale(pygame.image.load("assets/portail-copy.png"), (64, 128)),
                            ((64) * (collone - 1) + game.avancementT, 64 * (ligne - 2)+ligne+1))
                else:
                    screen.blit(pygame.transform.scale(pygame.image.load("assets/portail2-copy.png"), (64, 128)),
                                ((64) * (collone - 1) + game.avancementT, 64 * (ligne - 2) + ligne + 1))
            if fk == 3: #boite/tonneau
                ligne, collone = game.menu.ligne_collone(mouse_x, mouse_y, 64, 128, 0)
                screen.blit(pygame.transform.scale(pygame.image.load("assets/Box2-copy.png"), (64, 64)),
                            ((64) * (collone - 1) + game.avancementT, 64 * (ligne - 1)))
            if fk == 7: #pierre, caillou
                ligne,collone = game.menu.ligne_collone(mouse_x, mouse_y, 64, 64, 0)
                screen.blit(pygame.transform.scale(pygame.image.load("assets/deco_block/Rock_Big3-copy.png"), (128, 64)),
                            ((64 ) * (collone - 2) + game.avancementT, 64 * (ligne - 1)))


    boucle += 1#rajoute a la boucle
    for event in pygame.event.get():
        if event.type == pygame.MOUSEMOTION:#resevoir tout les touche presser
            mouse_x = event.pos[0]

            mouse_y = event.pos[1]
            pass


        if event.type == pygame.QUIT:#fermer la fenetre si la crois est presser
            running = False
            quit()
        if event.type == pygame.MOUSEMOTION:#si le jouer bouje sa souris
            if button_rect.collidepoint(event.pos):#si le retange est toucher changer l'image
                button = pygame.transform.scale2x(pygame.image.load('assets/menu/menu/Icons_40.png'))
                button_rect = button.get_rect()
            else:
                button = pygame.transform.scale2x(pygame.image.load('assets/menu/menu/Icons_39.png'))
            if game.menu.resume_rect.collidepoint(event.pos):#si le retange est toucher changer l'image
                resume_bouton = game.menu.resume_bouton2
            else:
                resume_bouton = game.menu.resume_bouton1
            if game.menu.restart_rect.collidepoint(event.pos):#si le retange est toucher changer l'image
                restart_bouton = game.menu.restart_bouton2
            else:
                restart_bouton = game.menu.restart_bouton1

            if game.menu.quit_rect.collidepoint(event.pos):#si le retange est toucher changer l'image
                quit_bouton = game.menu.quit_bouton2
            else:
                quit_bouton = game.menu.quit_bouton1
            if game.menu.seting_rect.collidepoint(event.pos):#si le retange est toucher changer l'image
                seting_bouton = game.menu.seting_bouton2
            else:
                seting_bouton = game.menu.seting_bouton1



        if event.type == pygame.MOUSEBUTTONUP:#si on click sur la souris
            try:#essayer
                if game.editor == False and game.boule == True:
                    if event.pos[0]>game.player.rect.x and event.pos[1]<game.player.rect.y+game.player.rect.height:
                        alpha = atan(((game.player.rect.y+game.player.rect.height)-event.pos[1])/((event.pos[0]-game.player.rect.x+game.player.rect.width)-34))
                        alpha = alpha/pi*180

                        game.spawn_boule_de_feu('droite',round(alpha,-1))
            except:
                pass



            if button_rect.collidepoint(event.pos):#si le rectanger est toucher changer les variable

                click[0] = 1
                if edittoring == True:
                    edittoring = False
                    editi = 1
                    game.alert = True
                    game.mouv = False

            if game.menu.resume_rect.collidepoint(event.pos):#si le rectanger est toucher changer les variable
                if editi == 1:
                    edittoring = True
                    editi = 0
                click[0] = 0
                game.alert = False
                game.mouv = True

            if game.menu.quit_rect.collidepoint(event.pos):#si le rectanger est toucher changer les variable et quiter le jeu
                if editi == 1:
                    try:
                        edit.fermer()

                    except :
                        pass
                    editi = 0
                    print(edittoring)
                    edittoring = False
                    game.editor = True
                    game.open = False
                click[0] = 0
                x = 0
                if charge_playing == True:
                    charge_playing = True
                nb_portail = 0
                portail = 0
                nb_porte = 0
                playing = False
            if game.menu.restart_rect.collidepoint(event.pos):#si le rectanger est toucher changer les variable et relancer le niveau
                game.__init__(tomber,monde,skin)
                charge_playing = True
                click[0] = 0














        if edittoring == True: #si lediteur est actif
            if event.type == pygame.MOUSEBUTTONDOWN: #si un clique est effectuer (un bloc placer)
                if not event.pos[0]>screen.get_width()-64 or not event.pos[1]<64: #si le clique est "valable"
                    # print('edt')
                    if event.type == pygame.MOUSEBUTTONDOWN and fk == -1: #suppression d'un bloc
                        y = 0
                        x = 0
                        for i in game.all_deco_block: #supprime le bloc dans deco block où leveneent a eu lieu
                            if event.pos[0] > i.rect.x and event.pos[0] < i.rect.x + i.rect.width and event.pos[1] > i.rect.y and event.pos[1] < i.rect.y + i.rect.height:
                                i.remove()
                                y = i.rect.y
                                x = i.rect.x

                        for i in game.all_object: #supprime le bloc dans all block où leveneent a eu lieu
                            if event.pos[0] > i.rect.x and event.pos[0] < i.rect.x + i.rect.width and event.pos[1] > i.rect.y and event.pos[1] < i.rect.y + i.rect.height:
                                i.remove()

                        for i in game.all_blockx: #supprime le bloc dans les autre blocks où leveneent a eu lieu
                            if event.pos[0] > i.rect.x and event.pos[0] < i.rect.x + i.rect.width and event.pos[1]>i.rect.y and event.pos[1]< i.rect.y+i.rect.height:
                                i.remove()
                                y = i.rect.y
                                x = i.rect.x

                                for i in range(len(game.blocktab)): #pour tous les blocks
                                    if game.blocktab[i][0] == x and game.blocktab[i][1] == y:
                                        if game.blocktab[i][4][7][0]==1:
                                            c,l = game.menu.ligne_collone(x,y,64,64,0)
                                            game.matrice[c-1][l-1] = 0
                                            game.update_block()
                                        game.blocktab[i][0], game.blocktab[i][1] = 10000, 10000


                    if event.type == pygame.MOUSEBUTTONDOWN and fk == 0: #terre
                        #dessine le bloc en fonction des conditions et du monde
                        if monde==2:
                            game.spawn_blockFor(event.pos[0], event.pos[1], 64, 64, "assets/lave/TileSet_02.png",[0, 50, 25, 2, True, 0, roto,[1,nb_terre,0],[0,0,0]], 0)
                        if monde==1:
                            game.spawn_blockFor(event.pos[0], event.pos[1], 64, 64, "assets/terre/TileSet_02.png",[0, 50, 25, 2, True, 0, roto, [1, nb_terre, 0], [0, 0, 0]], 0)
                        if monde==3:
                            game.spawn_blockFor(event.pos[0], event.pos[1], 64, 64, "assets/ice/TileSet_02.png",[0, 50, 25, 2, True, 0, roto, [1, nb_terre, 0], [0, 0, 0]], 0)
                        if monde==4:
                            game.spawn_blockFor(event.pos[0], event.pos[1], 64, 64, "assets/cave/TileSet_02.png",[0, 50, 25, 2, True, 0, roto, [1, nb_terre, 0], [0, 0, 0]], 0)

                        nb_terre += 1 #rajoute un bloc au nombre de bloc de terre

                    if event.type == pygame.MOUSEBUTTONDOWN and fk == 1: #eau
                        #dessine leau en fonction du monde et des conditions
                        if monde==1 :
                            game.spawn_blockFor(event.pos[0], event.pos[1], 64, 63, "assets/eau/Water1.png", [0, 50, 25, 2, True, 1, roto,[0,0,0],[0,0,0]],1)
                        if monde==2:
                            game.spawn_blockFor(event.pos[0], event.pos[1], 64, 63, "assets/lave/lava/lava1.png",[0, 50, 25, 2, True, 1, roto, [0, 0, 0], [0, 0, 0]], 1)
                        if monde==4 or monde==3 :
                            game.spawn_blockFor(event.pos[0], event.pos[1], 64, 63, "assets/eau/w/Water1.png",[0, 50, 25, 2, True, 1, roto, [0, 0, 0], [0, 0, 0]], 1)


                    if event.type == pygame.MOUSEBUTTONDOWN and fk == 2: #echelle
                        #dessine lechelle en fonction des conditions
                        if monde==1 or monde==3:
                            game.spawn_blockFor(event.pos[0], event.pos[1], 64, 64, "assets/echelle.png",[0, 50, 25, 2, False, 2, roto,[0,0,0],[0,0,0]], 0)
                        if monde == 2:
                            game.spawn_blockFor(event.pos[0], event.pos[1], 64, 64, "assets/object feu/3.png",[0, 50, 25, 2, False, 2, roto, [0, 0, 0], [0, 0, 0]], 0)
                        if monde == 4:
                            game.spawn_blockFor(event.pos[0], event.pos[1], 64, 64, "assets/object feu/2.png",[0, 50, 25, 2, False, 2, roto, [0, 0, 0], [0, 0, 0]], 0)
                        game.nbechelle += 1 #rajoute un nombre au nombre d'echelle

                    if event.type == pygame.MOUSEBUTTONDOWN and fk == 3: #dessine une boite
                        #dessine uniquement en fonction des conditions
                        game.spawn_blockFor(event.pos[0], event.pos[1], 64, 64, "assets/Box2.png", [0, 64, 0, 2, True, 0, roto,[0,0,0],[0,0,0]],0)

                    if event.type == pygame.MOUSEBUTTONDOWN and fk == 4: #dessine l'Idle
                        #dessine uniquement en fonction des conditions
                        game.spawn_blockFor(event.pos[0], event.pos[1], 40, 40, "assets/Idle.png", [0, 64, 0, 2, True, 0, roto,[0,0,0],[0,0,0]],9)


                    if event.type == pygame.MOUSEBUTTONDOWN and fk == 6: #dessine un portal
                        if nb_portail<2: #verifie si il a le droit de sinner un portail
                            if portail == 0: #si le prmier type de portail est selctionner
                                #dessine le portail en fonction des conditions
                                game.spawn_blockFor(event.pos[0], event.pos[1], 64, 128, "assets/portail.png", [0, 64+16, 0, 2, True, 4, roto,[0,0,0],[5,1,nb_portail]],8)
                                portail = 1 #change la selction du portail
                            else: #si le deuxieme type de portail est selctionner
                                #dessine le portail en fonction des conditions
                                game.spawn_blockFor(event.pos[0], event.pos[1], 64, 128, "assets/portail2.png",[0, 64+16, 0, 2, True, 4, roto, [0,0,0],[5,2,nb_portail]], 8)
                                portail = 0 #change la selction du portail
                                nb_portail += 1 #rajoute un au nombr de paire de portail possible

                    #dessine les bloks de deco (pierre, arbre)
                    if event.type == pygame.MOUSEBUTTONDOWN and fk == 7: #pierre
                        game.spawn_blockFor(event.pos[0], event.pos[1], 128,64, "assets/deco_block/Rock_Big3.png",[0, 64, 0, 2, True, 0, roto, [0, 0, 0], [0, 0, 0]], 10)
                    if event.type == pygame.MOUSEBUTTONDOWN and fk == 8: #arbre
                        game.spawn_blockFor(event.pos[0], event.pos[1], 150,256, "assets/deco_block/Tree2.png",[0, 64, 0, 2, True, 0, roto, [0, 0, 0], [0, 0, 0]], 10)






                    if event.type == pygame.MOUSEBUTTONDOWN and fk == 5:#start
                        if not len(game.startCo) == 0:
                            for i in range(len(game.blocktab)): #deplcace l'ancien spawn/start pour dessiner le nouveau
                                if game.blocktab[i][4][5] == 3:
                                    game.blocktab[i][4][5] = 0
                                    game.blocktab[i][4][6] = 1
                                    game.blocktab[i][0] = 1000
                                    game.blocktab[i][1] = 1000
                            for i in game.all_blockx:
                                if i.rect.x == game.startCo[0][0] and i.rect.y == game.startCo[0][1]:
                                    i.remove() #supprime les spawns deplacer
                            del game.startCo[0]
                        #dessine une nouveau spawn a lendroit voulu en respectnt les conditions
                        game.spawn_blockFor(event.pos[0], event.pos[1], 64, 16, "assets/Start (Idle).png",[0, 64, 0, 2, True, 3, roto,[0,0,0],[0,0,0]], 0)
                        #avec le joueur pour quil puisse bouger
                        game.mouv = True
                        game.alert = False

                    if event.type == pygame.MOUSEBUTTONDOWN and fk ==-3: #porte
                        if nb_porte == 0: #verifie si un porte est deja pas placée
                            nb_porte += 1 #place une nb_porte
                            #place une porte en fonciton des conditions
                            game.spawn_blockFor(event.pos[0], event.pos[1], 64+32, 128, "assets/porte/dor1.png",[0, 0, 0, 0, True, 10, roto, [0, 0, 0], [0, 0, 0]], 10)

                    if event.type == pygame.MOUSEBUTTONDOWN and fk == -2:#fait spawn un monster
                        game.spaw_monster(event.pos[0],event.pos[1])






        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                fichier2 = open('fichier/left.txt', mode='r+')
                fichier2.write(str(2))
                fichier2.close()
            if event.key == pygame.K_RIGHT:
                fichier3 = open('fichier/right.txt', mode='r+')
                fichier3.write(str(2))
                fichier3.close()
                right = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                fichier2 = open('fichier/left.txt', mode='r+')
                fichier2.write(str(1))
                fichier2.close()

            if event.key == pygame.K_RIGHT:
                fichier3 = open('fichier/right.txt', mode='r+')
                fichier3.write(str(1))
                fichier3.close()
                right = True



        if event.type == pygame.KEYDOWN:#resevoir tout les touche qui sont presser
            game.pressed[event.key] = True
            game.pressed2[event.key] = False

            #si la fleche du haut est presser alors sauter = True
            if (event.key == pygame.K_UP and sauter == False and tomber == False and game.alert == False and game.alert1 == False and game.alert2 == False) or (double_saut[0]==0 and double_saut[1]==1 and event.key == pygame.K_UP):
                if (event.key == pygame.K_UP and sauter == False and tomber == False and game.alert == False and game.alert1 == False and game.alert2 == False):
                    pass
                else:
                    if double_saut[1]==1:
                        double_saut[0] = 1

                game.player.index = 0
                sauter = True
                game.audio.chan0.play(game.audio.bond)
                tomber = False
                X = 30

                fichier = open('fichier/verify.txt', mode='r+')
                fichier.write(str(2))
        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False
            game.pressed2[event.key] = True



    if sauter == False and tomber == False:
        x = 0
        for i in range(len(game.blocktab)):
            if game.blocktab[i][4][8][0]==0:#si le personnage ne touche aucun block alors il tombe
                if game.player.rect.colliderect(game.blocktab[i][0], game.blocktab[i][1], game.blocktab[i][2],game.blocktab[i][3]):
                    x += 1
        if x == 0:
            tomber = True
            X = 0

    if sauter == True and tomber == False:#sauter
        if X - 2 >= 0:
            X -= 3
        else:
            X = 0

        sauter = game.player.sauter(X)#fonction qui fait sauter le personnage


        if sauter == False:
            tomber = True
            X = 0

    elif tomber == True and sauter == False:#tomber

        X -= 3
        tomber = game.player.tomber(X)#fonction tomber

        if double_saut[0] == 1:
            if tomber==False:
             double_saut[0]=0

    if edittoring == True:# si lediteur est actif
        if playing==True: # si joue
            try:
                edit.Update(game.block_list,game.objecttab, game.avancementT,game.decotab,game,monde)# sauvegarde automatiquemtn la listes des blocks
            except: #sinn terminer lediteur
                #playing = True
                #edit.fermer()
                edittoring == False
                editi = 0
                game.editor = True
                game.open = False
    #        edit.list_block_saver_out(game.block_list)
    #        print(edit.list_block_saver_out)

    clock.tick(30)#blockage des frame
    pygame.display.update()#acctualisation de la fenetre

    placeto = placeto2 #change le changement de music chaque prochaine boucle
    placeto2 = game.audio.update_music(placein, placeto)#change la music si besoin
