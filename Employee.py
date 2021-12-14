from Event  import *
from util import *

class Employee:

    def __init__(self, scheduler, queue, sink):
        self.clientsAttended=0
        self.scheduler = scheduler
        self.queue = queue
        self.sink=sink
        self.timeOfProcess = 150
        self.available = True

    def tractarEsdeveniment(self,event):
        self.available = False
        self.scheduler.afegirEsdeveniment(Event(self.queue, event.tid+self.timeOfProcess, EventType.FinishService, event.entitat))
        self.scheduler.afegirEsdeveniment(Event(self.sink, event.tid+self.timeOfProcess, EventType.FinshClient, event.entitat))
