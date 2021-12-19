from enum import Enum


class EventType(Enum):
    ScheduleArrival=1
    Tranfer=2
    Cycle=3
    FinshClient=4
    FinishService1=5
    FinishService2=6
    FinishService3=7
    SimulationStart=8
    NewClient=9
    AtendreClient=10
