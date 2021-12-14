from types import new_class
from util import EventType
from Event import *


class WaitingQueue:

    def __init__(self, scheduler,employee1, employee2, employee3):
        self.personesCua=0
        self.employee1=employee1
        self.employee2=employee2
        self.employee3=employee3
        self.queue=[]
        self.scheduler=scheduler
        pass

    def tractarEsdeveniment(self,event):
        if(event.type==EventType.NewClient):
            self.newClient(event)
        elif(event.type==EventType.FinishService):
            self.finishService(event)

    def newClient(self, event):
        if event.type==EventType.NewClient:
            self.queue.push(event.entitat)

        if(self.employee1.available):
            self.scheduler.afegirEsdeveniment(Event(self.employee1,event.tid,EventType.AtendreClient, self.queue.pop(0)))
        elif(self.employee2.available):
            self.scheduler.afegirEsdeveniment(Event(self.employee2,event.tid,EventType.AtendreClient, self.queue.pop(0)))
        elif(self.employee3.available):
            self.scheduler.afegirEsdeveniment(Event(self.employee3,event.tid,EventType.AtendreClient, self.queue.pop(0)))
        else:
            if event.type==EventType.NewClient:
                self.personesCua +=1

    def finishService(self, event):
        if len(self.queue) != 0:
            self.newClient(event)
    

