from types import new_class
from Util import EventType
from Event import *
from Employee import *

class WaitingQueue:

    def __init__(self, scheduler,employee1: Employee, employee2: Employee, employee3:Employee):
        self.scheduler=scheduler
        self.personesCua=0
        self.queue=[]
        self.employee1=employee1
        self.employee2=employee2
        self.employee3=employee3
        
       

    def tractarEsdeveniment(self,event: Event):
        if(event.type==EventType.NewClient):
            self.newClient(event)
        elif(event.type==EventType.FinishService):
            self.finishService(event)

    def newClient(self, event: Event):
        if event.type==EventType.NewClient:
            self.queue.append(event.entitat)

        if(self.employee1.available):
            self.scheduler.afegirEsdeveniment(Event(self.employee1,event.tid,EventType.AtendreClient, self.queue.pop(0)))
        elif(self.employee2.available):
            self.scheduler.afegirEsdeveniment(Event(self.employee2,event.tid,EventType.AtendreClient, self.queue.pop(0)))
        elif(self.employee3.available):
            self.scheduler.afegirEsdeveniment(Event(self.employee3,event.tid,EventType.AtendreClient, self.queue.pop(0)))
        else:
            if event.type==EventType.NewClient:
                self.personesCua +=1

    def finishService(self, event: Event):
        if len(self.queue) != 0:
            self.newClient(event)
    

