import pygame

class Audio:
    def __init__(self):
        pygame.mixer.init()#init du son

        self.chan0 = pygame.mixer.Channel(0)#creation du channel pour les effets
        self.chan1 = pygame.mixer.Channel(1)#creation du channel pour les musiques

        #importation des effets
        self.bond = pygame.mixer.Sound('assetsAudio/bond.wav')
        self.cash = pygame.mixer.Sound('assetsAudio/cash.wav')
        self.death = pygame.mixer.Sound('assetsAudio/death.wav')
        self.feu = pygame.mixer.Sound('assetsAudio/feu.wav')
        self.fin_niveau = pygame.mixer.Sound('assetsAudio/fin_niveau.wav')
        self.ring = pygame.mixer.Sound('assetsAudio/ring.wav')
        self.son_in = pygame.mixer.Sound('assetsAudio/son_in.wav')
        self.son_portail = pygame.mixer.Sound('assetsAudio/son_portail.wav')
        self.waa = pygame.mixer.Sound('assetsAudio/waa.wav')
        
        #importation des musiques
        self.chateau = pygame.mixer.Sound('assetsAudio/chateau.wav')
        self.moskau = pygame.mixer.Sound('assetsAudio/moskau.wav')
        self.ievan_polska = pygame.mixer.Sound('assetsAudio/ievan polska.wav')
        self.brawl_star = pygame.mixer.Sound('assetsAudio/brawl star.wav')
        self.guile_theme = pygame.mixer.Sound('assetsAudio/guile theme.wav')

    
        #permet de choisir les musiques d'ambience en fonction du menu
        self.music_list = [self.brawl_star, self.guile_theme, self.ievan_polska]
            
        self.music_dico = {'menu':self.moskau, \
                           'play':self.guile_theme, \
                           'edit':self.brawl_star, \
                           'level':self.chateau, \
                           'boutique':self.ievan_polska}

        self.playing = False #son en cours


    def set_volume(self, volume=0.02): #definition du volume
        pygame.mixer.music.set_volume(volume)


    def update_music(self, key_music, key_music_to): #changement de musique d'ambiance
        if key_music == key_music_to:
            return key_music
        else:
            if not self.playing:
                self.chan1.stop()
                self.chan1.play(self.music_dico[key_music])
                self.playing = True
            return key_music
            
