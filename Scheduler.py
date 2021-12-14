import bisect
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
        self.configurar()
        self.crearModel()
        
        #rellotge de simulacio a 0
        self.currentTime=0        
        #bucle de simulacio (condicio fi simulacio llista buida)
        while  self.currentTime<50:
            #recuperem event simulacio
            event:Event =self.eventList.pop(0)
            #actualitzem el rellotge de simulacio
            self.currentTime=event.tid
            # self.trace(event)
            # deleguem l'accio a realitzar de l'esdeveniment a l'objecte que l'ha generat
            # tambe podriem delegar l'accio a un altre objecte
            print(self.currentTime)
            event.object.tractarEsdeveniment(event)
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
        self.eventList.append(event)
        #bisect.insort(self.eventList, event)


    def tractarEsdeveniment(self,event):
        if (event.type==EventType.SimulationStart):
            self.source.simulationStart()
            # self.employee1.simulationStart()
            # self.employee2.simulationStart()
            # self.employee3.simulationStart()
            # self.sink.simulationStart()
    
    def configurar(self):
        print('Insereix temps de generació de customer ')
        self.tempsSimulacio=(float)(input("Temps Simulacio: "))
        self.arrivaltimes=(float)(input("Temps entre arribades: "))


    def crearModel(self):
        # creacio dels objectes que composen el meu model
        self.source = Source(self, self.arrivaltimes)
        self.employee1 = Employee(self)
        self.employee2 = Employee(self)
        self.employee3 = Employee(self)  
        self.queue = WaitingQueue(self, self.employee1, self.employee2, self.employee3)
        self.sink = Sink()
        self.employee1.initializeEntity(self.queue, self.sink)
        self.employee2.initializeEntity(self.queue, self.sink)
        self.employee3.initializeEntity(self.queue, self.sink)


    def recollirEstadistics(self):
        pass
        # print(Colors.HEADER,"ESTADÍSTICS",Colors.ENDC)

        # self.gainn.summary()
        # self.gataO.summary()
        # self.gataE.summary()
        # self.gataN.summary()
        # self.gataS.summary()
        # self.polite.summary()
        # self.gaut.summary()
   

if __name__ == "__main__":
    scheduler = Scheduler()
    scheduler.run()
