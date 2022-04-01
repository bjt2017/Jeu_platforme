import sys
class Open:
    def __init__(self):
        pass

    def get_file(self): #ouvre la fenetre pour rechercher un fichier
        import tkinter
        import tkinter as tk
        from tkinter.filedialog import askopenfilename
        root = tk.Tk()
        root.withdraw()
        filename = askopenfilename()
        root.destroy()


        return filename








