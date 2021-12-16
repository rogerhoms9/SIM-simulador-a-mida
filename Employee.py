from Event  import *
from Util import *

class Employee:

    def __init__(self, scheduler, id, simulationTime):
        self.clientsAttended=0
        self.scheduler = scheduler
        self.id=id
        self.timeOfProcess = simulationTime
        self.available = True
        self.working =0

    

    def initializeEntity(self,queue, sink):
        self.queue = queue
        self.sink=sink
    
    def tractarEsdeveniment(self,event:Event):
        self.available = False
        self.working+=self.timeOfProcess
        print("Processing client: "+str(event.entitat))
        if self.id==1:
            self.scheduler.afegirEsdeveniment(Event(self.queue, event.tid+self.timeOfProcess, EventType.FinishService1, event.entitat))
        elif self.id==2:
            self.scheduler.afegirEsdeveniment(Event(self.queue, event.tid+self.timeOfProcess, EventType.FinishService2, event.entitat))
        elif self.id==3:
            self.scheduler.afegirEsdeveniment(Event(self.queue, event.tid+self.timeOfProcess, EventType.FinishService3, event.entitat))

        self.scheduler.afegirEsdeveniment(Event(self.sink, event.tid+self.timeOfProcess, EventType.FinshClient, event.entitat))

    def getWWorkingTime(self):
        return self.working
