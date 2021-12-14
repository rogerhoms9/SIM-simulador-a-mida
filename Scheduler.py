import bisect
from Event import *
from Source import *
from util import *
from Sink import *


class SimuleringsMotor:

    currentTime = 0
    eventList = []
    
    def __init__(self):
    
        self.simulationStart=Event(self,0,EventType.SimulationStart,None)
        self.eventList.append(self.simulationStart)
        self.tempsSimulacio=100
        self.arrivaltimes=2
        self.cycletimes=10
        self.customerAtesos=0
        self.veuretraza=0

    def __repr__(self):
        return "Simulerings Motor"
 
    def run(self):
        #configurar el model per consola, arxiu de text...
        self.configurar()
        self.crearModel()
        
        #rellotge de simulacio a 0
        self.currentTime=0        
        #bucle de simulacio (condicio fi simulacio llista buida)
        endSimulation = input("Stopsim with -1")
        while endSimulation!=-1:
            #recuperem event simulacio
            event=self.eventList.pop(0)
            #actualitzem el rellotge de simulacio
            self.currentTime=event.tid
            self.trace(event)
            # deleguem l'accio a realitzar de l'esdeveniment a l'objecte que l'ha generat
            # tambe podriem delegar l'accio a un altre objecte
            event.objecte.tractarEsdeveniment(event)
            #endSimulation = input("Stopsim with -1")

        
        #recollida d'estadistics
        self.recollirEstadistics()

    def trace(self,event):
        if (self.veuretraza==0):
             return
        color=Colors.HEADER
        if event.type==EventType.Access:
            color=Colors.OKBLUE
        if event.type==EventType.Cycle:
            color=Colors.HEADER
        if event.type==EventType.NextArrival:
            color=Colors.OKGREEN
        if event.type==EventType.StepIn:
            color=Colors.OKCYAN
        if event.type==EventType.Tranfer:
            color=Colors.OKRARO
        print(color,event.tid,event.type,' ',event.objekt,Colors.ENDC)

    def afegirEsdeveniment(self,event):
        #inserir esdeveniment de forma ordenada
        self.eventList.push(event)
        #bisect.insort(self.eventList, event)


    def tractarEsdeveniment(self,event):
        if (event.type==EventType.SimulationStart):
            self.source.simulationStart()
            self.queue.simulationStart()
            self.employee1.simulationStart()
            self.employee2.simulationStart()
            self.employee3.simulationStart()
            self.sink.simulationStart()
    
    def configurar(self):
        print('Insereix temps de generació de customer ')
        self.tempsSimulacio=(float)(input("Temps Simulacio: "))
        self.arrivaltimes=(float)(input("Temps entre arribades: "))


    def crearModel(self):
        # creacio dels objectes que composen el meu model
        self.source = Source(self, self.arrivaltimes)
        self.queue = WaitingQueue(self)
        self.employee1 = Employee(self, "1")
        self.employee2 = Employee(self, "2")
        self.employee3 = Employee(self, "3")     
        self.sink = Sink(self.veuretraza)


    def recollirEstadistics(self):
        print(Colors.HEADER,"ESTADÍSTICS",Colors.ENDC)

        self.gainn.summary()
        self.gataO.summary()
        self.gataE.summary()
        self.gataN.summary()
        self.gataS.summary()
        self.polite.summary()
        self.gaut.summary()
   

if __name__ == "__main__":
    scheduler = SimuleringsMotor()
    scheduler.run()
