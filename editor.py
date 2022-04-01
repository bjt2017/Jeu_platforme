from tkinter import *
from time import sleep

from levelsaver import Saver



class Editor:
    def __init__(self,game):

        #mise en place de la fenetre et des variables
        self.fen = Tk()
        self.bouton = []
        self.saver = Saver()
        self.button_size = 64+4
        
        self.size_can_width = self.button_size*8
        self.size_can_height = self.size_can_width
        
        self.can = Canvas(self.fen, width=self.size_can_width, height=self.size_can_height, bg='red')
        self.bg_editor = PhotoImage(file="assetsEditor/editor_background.png")
        self.can.pack()
        
        self.game = game
        
        #importation des images
        self.img_dor = PhotoImage(file="assetsEditor/dor1.png")
        self.img_grass = PhotoImage(file="assetsEditor/terre.png")
        self.img_eau = PhotoImage(file="assetsEditor/eau.png")
        self.img_echelle = PhotoImage(file="assetsEditor/echeclle.png")
        self.img_solid_block = PhotoImage(file="assetsEditor/Idle.png")
        self.img_poutre = PhotoImage(file="assetsEditor/poutre.png")
        self.img_porte = PhotoImage(file="assetsEditor/portail.png")
        self.img_porte2 = PhotoImage(file="assetsEditor/portail2.png")
        self.porte2 = False
        self.img_pomme = PhotoImage(file="assetsEditor/Coin1.png")
        self.img_start = PhotoImage(file="assetsEditor/Start (Idle).png")
        self.img_delete = PhotoImage(file="assetsEditor/delete.png")
        self.img_rock = PhotoImage(file="assetsEditor/Rock_Big3.png")
        self.img_tree = PhotoImage(file="assetsEditor/Tree3.png")
        self.img_goblin = PhotoImage(file="assetsEditor/Goblin1.png")

        #creation des boutons
        self.create(1, 0, self.img_delete, -1)
        self.create(0, 0, self.img_grass, 0)
        self.create(0,1,self.img_eau,1)
        self.create(0, 2, self.img_echelle, 2)
        self.create(0, 3, self.img_solid_block, 3)
        self.create(0, 4, self.img_pomme, 4)
        self.create(0, 5, self.img_start, 5)
        self.create(0, 6, self.img_porte, 6)
        self.create(0, 7, self.img_rock, 7)
        self.create(1, 1, self.img_tree, 8)
        self.create(1, 2, self.img_goblin, -2)
        self.create(1, 3, self.img_dor, -3)

        #autoriser lutilisation des boutons
        self.enable_grass = True
        self.enable_eau = True
        self.enable_echelle = True
        self.enable_solid_block = True
        self.enable_poutre = True
        self.enable_porte = True
        self.enable_pomme = True
        self.enable_start = True
        self.enable_delete = True
        self.list_enable = [self.enable_grass, self.enable_eau, self.enable_echelle,
                            self.enable_solid_block, self.enable_poutre, self.enable_porte,
                            self.enable_pomme, self.enable_start, self.enable_delete]
        
        #desinne le reste de linterface des boutons
        self.Saver_draw(340, 10)
        self.bg = self.can.create_image(-10, -10, anchor=NW, image=self.bg_editor)
        self.select = self.can.create_image(self.size_can_width, self.size_can_height, anchor=SE, image=self.img_solid_block)
        self.select_num = 0


        #liste pour l'enregistrement des niveaux créee
        self.list_block_saver_out = []
        self.list_objects_saver_out = []
        

       # self.fen.mainloop()
    def fermer(self):
        self.fen.destroy()

        
    def create(self,c,l,image,chiffre):#creer un bouton
        self.button = Button(self.fen, image=image, bg='#8B4513', bd='0',activeforeground='white', command = lambda:self.cliquer(chiffre,image))
        self.button.pack()
        self.button.place_configure(x=self.button_size * c, y=self.button_size * l)



    def cliquer(self,x,img):#trouve levenement du clique
        self.select_num = x
        self.can.itemconfig(self.select, image=img)




    def value_select(self):#retourne la valeur du bouton selectionner
        return self.select_num


    def Update(self, list_block__, list_objects__, total,decotab,game,monde):#update lediteur dans main
        self.monde = monde
        self.list_block_saver_out = list_block__
        self.list_objects_saver_out = list_objects__
        self.decotab = decotab
        self.avencement = total
        self.saver.avancement = total
        #print(self.list_block_saver_out)
        self.fen.update()
        self.game = game




    def save(self):#sauvegarde la liste des objets placés
        print('save : ', self.list_block_saver_out)
        self.saver.list_of_block_changer(self.list_block_saver_out)

    def save_in_file(self):#sauvegarde la liste des objets placés dans le fichier
        print('saved in file', bool(self._entry_file_name.get()))
        if True:
            if bool(self._entry_file_name.get()) != False:
                namefile = 'levelsaved/' + self._entry_file_name.get() + '.txt'
                print(self._entry_file_name.get())
            else:
                namefile = 'levelsaved/' + self.input_name() + '.txt'
                print(self.input_name)
            print(namefile)
            self.saver.writer_in_textfile(namefile, self.list_block_saver_out, self.list_objects_saver_out,self.decotab,self.avencement,self.game,self.monde)

    def input_name(self):#pour faire rentrer le nom du fichier voulu pour edupython
        return str(input("Enter le nom du niveau : "))
        

    def Saver_draw(self, ppx, ppy): #dessine les boutons et lentree de texte pour lenregistemrement des fichiers
  
        #size x=__, y=__
        self._label_file1 = Label(self.fen, text='levelsaved/', bg='#7fbddc')
        self._label_file1.pack()
        self._label_file1.place_configure(anchor=NW, x=ppx, y=ppy)
        #self._label_file1.grid(row=0, column=0)

        #size x=__, y=__
        self._entry_file_name = Entry(self.fen)
        self._entry_file_name.pack()
        self._entry_file_name.place_configure(anchor=NW, x=ppx+66, y=ppy)
        #self._entry_file_name.grid(row=0, column=1)

        #size x=__, y=__
        self.save_button = Button(self.fen, text='Save in file', bg='#59add6', activebackground='#7fbddc', command=self.save_in_file)
        self.save_button.pack()
        self.save_button.place_configure(anchor=NW, x=ppx+90, y=ppy+24)
        #self.save_button.grid(row=1, column=0)

        #size x=__, y=__
        self.save_button = Button(self.fen, text='Update Save', bg='#59add6', activebackground='#7fbddc', command=self.save)
        self.save_button.pack()
        self.save_button.place_configure(anchor=NW, x=ppx, y=ppy+24)
        #self.save_button.grid(row=1, column=0)

        #size x=__, y=__
        #self.input_button = Button(self.fen, text='Input Name', bg='#59add6', activebackground='#7fbddc', command=self.input_name)
        #self.input_button.pack()
        #self.input_button.place_configure(anchor=NW, x=ppx, y=ppy+58)
        #self.save_button.grid(row=1, column=0)




#pour tester et debuger
#edit = Editor(3)
