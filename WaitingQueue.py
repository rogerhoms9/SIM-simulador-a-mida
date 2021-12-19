from types import new_class
from Util import EventType
from Event import *
from Employee import *
import matplotlib.pyplot as plt

class WaitingQueue:

    def __init__(self, scheduler,employee1: Employee, employee2: Employee, employee3:Employee):
        self.scheduler=scheduler
        self.personesCua=0
        self.totalOcupation=[]
        self.times=[]
        self.queue=[]
        self.employee1=employee1
        self.employee2=employee2
        self.employee3=employee3
        self.waitTime=[]
        
       

    def tractarEsdeveniment(self,event: Event):
        if(event.type==EventType.NewClient):
            self.newClient(event)
        else:
            self.finishService(event)

    def newClient(self, event: Event):
        if event.type==EventType.NewClient:
            print("inside queue")
            self.queue.append(event.entitat)

        if(self.employee1.available):
            self.waitTime.append( event.tid-self.queue[0].creationTime )
            self.scheduler.afegirEsdeveniment(Event(self.employee1,event.tid,EventType.AtendreClient, self.queue.pop(0)))
        elif(self.employee2.available):
            self.waitTime.append( event.tid-self.queue[0].creationTime )
            self.scheduler.afegirEsdeveniment(Event(self.employee2,event.tid,EventType.AtendreClient, self.queue.pop(0)))
        elif(self.employee3.available):
            self.waitTime.append( event.tid-self.queue[0].creationTime )
            self.scheduler.afegirEsdeveniment(Event(self.employee3,event.tid,EventType.AtendreClient, self.queue.pop(0)))
        else:
            if event.type==EventType.NewClient:
                self.personesCua +=1
        self.computeOcupation(event)
    
    def computeOcupation(self,event):
        self.times.append(event.tid)
        self.totalOcupation.append(len(self.queue))

    def finishService(self, event: Event):
        if event.type==EventType.FinishService1:
            self.employee1.available=True
        elif event.type==EventType.FinishService2:
            self.employee2.available=True
        elif event.type==EventType.FinishService3:
            self.employee3.available=True
        if len(self.queue) != 0:
            print("QUEUE:")
            print(self.queue)
            self.newClient(event)
    
   

