import math
from Client import * 
from Event import *
from Util import *

class Source:

    def __init__(self,scheduler,parameter):
        # inicialitzar element de simulacio
        self.entitatsCreades=0
        self.state=State.SERVICE
        self.scheduler=scheduler
        self.tempsEntreArribades=parameter
        self.idClient=0


    def __repr__(self):
        return "Source"
    
#    def koble(self,gataE,gataO,gataN,gataS):
#        self.gataE=gataE
#        self.gataO=gataO
#        self.gataN=gataN
#        self.gataS=gataS   
#         self.gater=[self.gataE,self.gataO,self.gataN,self.gataS]

    def tractarEsdeveniment(self, event):
        if (event.type==EventType.ScheduleArrival):
            self.processNextArrival(event)        

    def simulationStart(self):
        self.entitatsCreades=0
        self.properaArribada(0)
        
    def processNextArrival(self,event):
        #programacio propera arribada
        self.properaArribada(event.tid)
        # incrementem estadistics si s'escau
        self.entitatsCreades=self.entitatsCreades+1
        #creacio entitat arribada
        self.idClient+=1
        entitat=Client(self.idClient, self.scheduler.currentTime )
        print("Client "+ str(entitat.id)+" created.")
        self.scheduler.afegirEsdeveniment(Event(self.scheduler.queue,event.tid,EventType.NewClient, entitat))

    def properaArribada(self, temps):
        # cada quan generem una arribada (hauriem de tenir com a minim alguna component estocastica)
        tempsEntreArribades = self.tempsEntreArribades
        # programacio arribada
        self.scheduler.afegirEsdeveniment(Event(self,temps+tempsEntreArribades,EventType.ScheduleArrival, None))
      
    def summary(self):
        print('Entitats arribades al sistema: ',self.entitatsCreades)
        