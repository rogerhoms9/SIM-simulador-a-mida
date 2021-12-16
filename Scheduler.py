import bisect
from typing import List
from Event import *
from Source import *
from Util import *
from Sink import *
from WaitingQueue import *
from Employee import *
import operator



class Scheduler:

    currentTime = 0
    eventList = []
    
    def __init__(self):
        self.simulationStart=Event(self,0,EventType.SimulationStart,None)
        self.eventList.append(self.simulationStart)
        self.tempsSimulacio=100
        self.arrivaltimes=2
        self.cycletimes=10
        self.customerAtesos=0

    def __repr__(self):
        return "Simulerings Motor"
 
    def run(self):
        #configurar el model per consola, arxiu de text...
        print('Insereix temps de generació de customer ')
        self.tempsSimulacio=(float)(input("Temps Simulacio: "))
        self.arrivaltimes=(float)(input("Temps entre arribades: "))
        self.processingTime=(float)(input("Temps d'atenció a un client: "))

        self.crearModel()
        
        #rellotge de simulacio a 0
        self.currentTime=0        
        #bucle de simulacio (condicio fi simulacio llista buida)
        while  self.currentTime < self.tempsSimulacio:
            #recuperem event simulacio
            event:Event =self.eventList.pop(0)
            #actualitzem el rellotge de simulacio
            self.currentTime=event.tid
            # self.trace(event)
            # deleguem l'accio a realitzar de l'esdeveniment a l'objecte que l'ha generat
            # tambe podriem delegar l'accio a un altre objecte
            print(event)
            event.object.tractarEsdeveniment(event)
        self.recollirEstadistics()

    # def trace(self,event):
    #     if (self.veuretraza==0):
    #          return
    #     color=Colors.HEADER
    #     if event.type==EventType.Access:
    #         color=Colors.OKBLUE
    #     if event.type==EventType.Cycle:
    #         color=Colors.HEADER
    #     if event.type==EventType.NextArrival:
    #         color=Colors.OKGREEN
    #     if event.type==EventType.StepIn:
    #         color=Colors.OKCYAN
    #     if event.type==EventType.Tranfer:
    #         color=Colors.OKRARO
    #     print(color,event.tid,event.type,' ',event.objekt,Colors.ENDC)

    def afegirEsdeveniment(self,event):
        #inserir esdeveniment de forma ordenada
        self.eventList.append(event)
        self.eventList.sort(key=lambda x: x.tid, reverse=False)


    def tractarEsdeveniment(self,event):
        if (event.type==EventType.SimulationStart):
            self.source.simulationStart()  


    def crearModel(self):
        # creacio dels objectes que composen el meu model
        self.source = Source(self, self.arrivaltimes)
        self.employee1 = Employee(self,1,self.processingTime)
        self.employee2 = Employee(self,2,self.processingTime)
        self.employee3 = Employee(self,3,self.processingTime)  
        self.queue = WaitingQueue(self, self.employee1, self.employee2, self.employee3)
        self.sink = Sink()
        self.employee1.initializeEntity(self.queue, self.sink)
        self.employee2.initializeEntity(self.queue, self.sink)
        self.employee3.initializeEntity(self.queue, self.sink)


    def recollirEstadistics(self):
        self.queue.showChart()
        self.showPieChartEmployee1()
    
    def showPieChartEmployee1(self):
        workingTime=self.employee1.getWWorkingTime()

        labels = 'Working', 'IDLE'
        sizes = [workingTime, self.tempsSimulacio-workingTime] 
        fig1, ax1 = plt.subplots()   
        ax1.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
        ax1.axis('equal') 
        plt.show()

   

if __name__ == "__main__":
    scheduler = Scheduler()
    scheduler.run()
