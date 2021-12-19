
import math
from Event import *


class Sink:


    def __init__(self):
        # inicialitzar element de simulacio
        self.entitatsSortides=0
        # self.state=State.SERVICE
        self.livAvg=0
        # self.veuretraza=veuretraza

    def tractarEsdeveniment(self, event):
        self.processFinihService(event)        

    def processFinihService(self,event:Event):
        # Fer quelcom d'estadistics
        self.entitatsSortides+=1
        print("Client "+ str(event.entitat)+" has been served.")
        #self.livAvg=(self.livAvg+event.entitat.livstid)/self.entitatsSortides
        # Memoritzar temps de vida
        self.summary()

        pass
    
    def summary(self):
        print('Entitats sortides del sistema: ',self.entitatsSortides)
        #print('Temps mig de vida: ',self.livAvg)

    
   