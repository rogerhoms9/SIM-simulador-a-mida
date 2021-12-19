from Event  import *
from Util import *
import numpy as np

class Employee:

    def __init__(self, scheduler, id, mediana, variancia):
        self.clientsAttended=0
        self.scheduler = scheduler
        self.id=id
        #self.timeOfProcess = simulationTime
        self.mediana= mediana
        self.variancia= variancia
        self.available = True
        self.working =0.0

    

    def initializeEntity(self,queue, sink):
        self.queue = queue
        self.sink=sink
    
    def tractarEsdeveniment(self,event:Event):
        self.timeOfProcess=np.random.normal(self.mediana, self.variancia,1)[0]
        self.available = False
        self.working+=self.timeOfProcess
        print("Processing client: "+str(event.entitat.id))
        if self.id==1:
            self.scheduler.afegirEsdeveniment(Event(self.queue, event.tid+self.timeOfProcess, EventType.FinishService1, event.entitat))
        elif self.id==2:
            self.scheduler.afegirEsdeveniment(Event(self.queue, event.tid+self.timeOfProcess, EventType.FinishService2, event.entitat))
        elif self.id==3:
            self.scheduler.afegirEsdeveniment(Event(self.queue, event.tid+self.timeOfProcess, EventType.FinishService3, event.entitat))

        self.scheduler.afegirEsdeveniment(Event(self.sink, event.tid+self.timeOfProcess, EventType.FinshClient, event.entitat))

    def getWorkingTime(self):
        return self.working
