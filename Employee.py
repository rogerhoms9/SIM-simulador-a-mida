from Event  import *
from Util import *

class Employee:

    def __init__(self, scheduler):
        self.clientsAttended=0
        self.scheduler = scheduler
  
        self.timeOfProcess = 150
        self.available = True
    

    def initializeEntity(self,queue, sink):
        self.queue = queue
        self.sink=sink
    

    def tractarEsdeveniment(self,event:Event):
        self.available = False
        print("Processing client: "+str(event.entitat))
        self.scheduler.afegirEsdeveniment(Event(self.queue, event.tid+self.timeOfProcess, EventType.FinishService, event.entitat))
        self.scheduler.afegirEsdeveniment(Event(self.sink, event.tid+self.timeOfProcess, EventType.FinshClient, event.entitat))
