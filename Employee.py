from Event  import *
from Util import *
import numpy as np

class Employee:

    def __init__(self, scheduler, id, mediana, variancia):
        self.clientsAttended=0
        self.scheduler = scheduler
        self.id=id
        self.mediana= mediana
        self.variancia= variancia
        self.available = True
        self.workingCarn =0.0
        self.workingPeix =0.0

    

    def initializeEntity(self,queue, sink):
        self.queue = queue
        self.sink=sink
    
    def tractarEsdeveniment(self,event:Event):
        #IF tipus 1, per tant client que compra peix -> el temps de process es duplica
        if event.entitat.tipus==1:
            self.timeOfProcess=round(np.random.normal(self.mediana, self.variancia,1)[0],1) * 2
            print("Processing client peix: "+str(event.entitat.id)+ ". Temps de procés:" + str(self.timeOfProcess)+ " segons.")
            if event.tid+self.timeOfProcess <= self.scheduler.tempsSimulacio:   
                self.workingPeix +=self.timeOfProcess
        else:
            self.timeOfProcess=round(np.random.normal(self.mediana, self.variancia,1)[0], 1)
            print("Processing client carn: "+str(event.entitat.id)+ ". Temps de procés:" + str(self.timeOfProcess)+ " segons.")
            if event.tid+self.timeOfProcess <= self.scheduler.tempsSimulacio:   
                self.workingCarn +=self.timeOfProcess
        self.available = False

        #Per evitar possible error en l'últim element si es passa del temps de simulació
        

        if self.id==1:
            self.scheduler.afegirEsdeveniment(Event(self.queue, event.tid+self.timeOfProcess, EventType.FinishService1, event.entitat))
        elif self.id==2:
            self.scheduler.afegirEsdeveniment(Event(self.queue, event.tid+self.timeOfProcess, EventType.FinishService2, event.entitat))
        elif self.id==3:
            self.scheduler.afegirEsdeveniment(Event(self.queue, event.tid+self.timeOfProcess, EventType.FinishService3, event.entitat))

        self.scheduler.afegirEsdeveniment(Event(self.sink, event.tid+self.timeOfProcess, EventType.FinshClient, event.entitat))

    def getWorkingTimes(self):
        return [self.workingCarn, self.workingPeix]
