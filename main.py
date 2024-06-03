#!/usr/bin/python
#
import sys,time,socket,json
import tkinter as tk
import tkinter.messagebox

class appVote:

    lafin = False
    photo = None
    almRouge = None
    almVert = None
    adresseIP = None
    port = None

    def __init__(self, geo="1000x700+225+150", confFile="config.json"):

        with open(confFile, 'r') as file:
            self.parametres = json.load(file)

        self.adresseIP = self.parametres['adresse_serveur']
        self.port = self.parametres['port_tcp_serveur']

        self.email_sender = self.parametres['email_sender']

        self.root = tk.Tk()
        self.root.geometry(geo)
        #self.root.resizable(False, False)
        #self.root.attributes('-fullscreen',True)
        self.root.minsize(1000, 700)
        self.root.title("Cégep Joliette Télécom@" + str(socket.gethostname()))
        self.root.wm_attributes('-alpha', 0.75)

        try :

            self.almRouge = tk.PhotoImage(file="almRouge.png")
            self.almVerte = tk.PhotoImage(file="almVerte.png")
            self.photo = tk.PhotoImage(file="logodemo_t.png")

            # Load the custom icon image
            icon_image = tk.PhotoImage(file="iconeDemo.png")

            # Set the custom icon for the window titlebar
            self.root.iconphoto(False, icon_image)

        except Exception as excpt:
            
            print("Fichiers des images manquants!")
            print("Erreur : ", excpt)
            sys.exit()
            
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        try:
            s.connect(('10.255.255.255', 1))
            self.adresseIP = s.getsockname()[0]
        except:
            self.adresseIP='127.0.0.1'
        finally:
            s.close()
        self.lblAdresseIP = tk.Label(self.root, anchor="w")                     # Bas de page
        self.lblAdresseIP.place(relx=0.05, rely=0.95, height=23, width=225)
        self.lblAdresseIP.configure(text="Serveur " + self.adresseIP)
        self.lblAdresseIP.configure(justify='left')
        self.lblAdresseIP.configure(font=("Courrier New", 10, "bold"))
        #self.lblAdresseIP.bind("<Button-1>", self.buttonAdresse)

        self.lblPortTCP = tk.Label(self.root, anchor="w")                       # Bas de page
        self.lblPortTCP.place(relx=0.25, rely=0.95, height=23, width=100)
        self.lblPortTCP.configure(text="Port " + ":" + str(self.port))
        self.lblPortTCP.configure(justify='left')
        self.lblPortTCP.configure(font=("Courrier New", 10, "bold"))
        #self.lblPortTCP.bind("<Button-1>", self.buttonPort)

    def run(self):

        while not self.lafin:
    
            self.root.update_idletasks()
            self.root.update()
            time.sleep(0.01)
            
        self.root.quit()

    def on_closing(self):

        if tk.messagebox.askokcancel("Terminé ?", "Est-ce que vous voulez fermer le programme ?"):

            self.lafin = True
            time.sleep(1)
            
application = appVote("1190x750+225+150")
application.run()
    
