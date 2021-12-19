import math
from Client import * 
from Event import *
from Util import *
import numpy as np


class Source:

    def __init__(self,scheduler,parameter):
        # inicialitzar element de simulacio
        self.scheduler=scheduler
        self.tempsEntreArribades=parameter
        self.idClient=0


    def __repr__(self):
        return "Source"

    def tractarEsdeveniment(self, event):
        if (event.type==EventType.ScheduleArrival):
            self.processNextArrival(event)        

    def simulationStart(self):
        self.properaArribada(0)
        
    def processNextArrival(self,event):
        #programacio propera arribada
        if event.tid + self.tempsEntreArribades <= self.scheduler.tempsSimulacio:
            self.properaArribada(event.tid)
        # incrementem estadistics si s'escau
        
        #creacio entitat arribada
        
        if len(self.scheduler.queue.queue) < self.scheduler.queue.maxSize:
            self.idClient+=1
            entitat=Client(self.idClient, self.scheduler.currentTime, np.random.randint(2,size=1)[0] )
            print("Client "+ str(entitat.id)+" de tipus "+str( "carn" if entitat.tipus==0 else "peix")+" created.")

            self.scheduler.afegirEsdeveniment(Event(self.scheduler.queue,event.tid,EventType.NewClient, entitat))
        else:
            print("Queue is full!")

    def properaArribada(self, temps):
        # programacio pròxima arribada
        self.scheduler.afegirEsdeveniment(Event(self, temps+ self.tempsEntreArribades,EventType.ScheduleArrival, None))
      
    def summary(self):
        print('Entitats arribades al sistema: ',self.entitatsCreades)
        