
class Saver:
    def __init__(self):
        #creer les listes pour enregistrer les blocks
        self.list_all_block = []
        self.list_of_all_command_block = []
        self.number_of_blocks = 0
        self.avancement = 0


    ###les definitions suivante servent de support pour faciliter lecriture des blocks
    def text_creater_line(self, list_block_description):#creer le texte a ecrire dans le fichier
        cmd_txt = 'game.spawn_blockFor(' + str(list_block_description[0]-self.avancement) + \
                  ', ' + str(list_block_description[1]) + ', ' + str(list_block_description[2])+\
                  ', ' + str(list_block_description[3]) + ', ' + '"' + str(list_block_description[4])+\
                  '"' +', ' + str(list_block_description[5]) + ','+str(list_block_description[6])+')'
        return cmd_txt

    def text_creater_object_line(self, list_object_description):#creer le texte a ecrire dans le fichier v1
         cmd2_txt = 'game.spawn_pomme(' + str(list_object_description[0]-self.avancement) + ', ' +\
                    str(list_object_description[1]) + ')'
         return cmd2_txt

        
    def text_creater_deco_line(self, list_deco_description):#creer le texte a ecrire dans le fichier v2
        cmd_txt = 'game.spawn_deco_Block(' + str(list_deco_description[0]-self.avancement) + \
                  ', ' + str(list_deco_description[1]) + ', ' + str(list_deco_description[2]) + \
                  ', ' + str(list_deco_description[3]) + ', ' + '"' + str(list_deco_description[4]) + \
                  '"' + ', ' + str(list_deco_description[5]) + ',' + str(list_deco_description[6]) + ')'
        return cmd_txt

    def list_of_all_block_maker(self):#transforme la liste de blocks en liste de texte pour lecrire sur le fichier
        for blocks in self.list_all_block:
            cmd_txt_in = self.text_creater_line(blocks)
            self.list_of_all_command_block.append(cmd_txt_in)
        return self.list_of_all_command_block

    def number_of_block_num(self):#retourne la taille de la liste de blocks
        self.number_of_blocks = len(self.list_of_all_command_block)
        return self.number_of_blocks


    ###definition qui permettent d'inscire les blocks dans le fichier
    def list_of_block_changer(self, list_all_block):#importeles liste de block (1ERE CMD A EFFECTUER POUR ENRGISTRER)
        self.list_all_block = list_all_block
        self.list_of_all_command_block = list_all_block

    def writer_in_textfile(self, namefile, list___B, list___O,decotab,avencement,game,monde):#ecrit dans le fichier (2EME CMD A EFFECTUER POUR ENRGISTRER)
        self.avancement = avencement
        fih = open(namefile, 'w')
        num = len(list___B) + len(list___O) + len(decotab)
        fih.write(str(monde))
        fih.write('\n')
        fih.write(str(game.ajouter))
        print(game.ajouter)
        fih.write('\n')
        fih.write(str(num))
        fih.write('\n')
        for cmd in list___B:
        #for cmd in self.list_of_all_command_block:
            #print(self.list_of_all_command_block)
            ccm = self.text_creater_line(cmd)
            print(ccm)
            fih.write(ccm)
            fih.write('\n')
        for cmd2 in list___O:
            ccm2 = self.text_creater_object_line(cmd2)
            print(ccm2)
            fih.write(ccm2)
            fih.write('\n')
        for cmd3 in decotab:
            ccm3 = self.text_creater_deco_line(cmd3)
            print(ccm3)
            fih.write(ccm3)
            fih.write('\n')
        fih.close()

    


