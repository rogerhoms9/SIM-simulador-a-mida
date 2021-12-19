from typing import List
from Event import *
from Source import *
from Util import *
from Sink import *
from WaitingQueue import *
from Employee import *



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
        self.tempsSimulacio=(float)(input("Temps Simulacio: "))
        self.arrivaltimes=(float)(input("Temps entre arribades: "))
        self.mediana=(float)(input("Introdueix la mediana del temps d'atenció d'un client: "))
        self.variancia=(float)(input("Introdueix la variancia del temps d'atenció d'un client: "))
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
            print(str(event))
            event.object.tractarEsdeveniment(event)
        self.recollirEstadistics()

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
        self.employee1 = Employee(self,1,self.mediana, self.variancia)
        self.employee2 = Employee(self,2,self.mediana, self.variancia)
        self.employee3 = Employee(self,3,self.mediana, self.variancia)  
        self.queue = WaitingQueue(self, self.employee1, self.employee2, self.employee3)
        self.sink = Sink()
        self.employee1.initializeEntity(self.queue, self.sink)
        self.employee2.initializeEntity(self.queue, self.sink)
        self.employee3.initializeEntity(self.queue, self.sink)


    def recollirEstadistics(self):
        sum=0
        for i in self.queue.waitTime:
            sum+=i
        print("AVERAGE TIME ON QUEUE:")
        if len(self.queue.waitTime)!=0:
            print(str(sum/len(self.queue.waitTime))+"seconds")
        self.showQueueOcupation()
        self.showPieChartEmployees()
    
    def showPieChartEmployees(self):
        labels = 'Working', 'IDLE'

        workingTime=self.employee1.getWorkingTime()
        sizes = [workingTime, self.tempsSimulacio-workingTime] 
        fig1, ax1 = plt.subplots()   
        ax1.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
        ax1.axis('equal')
        ax1.set_title('Employee 1 workload') 
        
        workingTime=self.employee2.getWorkingTime()
        sizes = [workingTime, self.tempsSimulacio-workingTime] 
        fig2, ax2 = plt.subplots()   
        ax2.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
        ax2.axis('equal') 
        ax2.set_title('Employee 2 workload')

        workingTime=self.employee3.getWorkingTime()
        sizes = [workingTime, self.tempsSimulacio-workingTime] 
        fig3, ax3 = plt.subplots()   
        ax3.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
        ax3.axis('equal') 
        ax3.set_title('Employee 3 workload')
        plt.show()

    def showQueueOcupation(self):
        plt.plot(self.queue.times, self.queue.totalOcupation, color='red', marker='o')
        plt.title('Queue occupation')
        plt.xlabel('Time')
        plt.ylabel('People')
        plt.show()
    

   

if __name__ == "__main__":
    scheduler = Scheduler()
    scheduler.run()
