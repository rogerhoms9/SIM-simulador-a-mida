from oppregninger import *

class Event:
    def __init__(self,object,temps,tipus,entitat=None,fra=None):
            # inicialitzar element de simulacio
        self.entitatsTractades=0
        self.type=tipus
        self.object=object
        self.tid=temps
        self.entitat=entitat
        self.fra=fra

    def __repr__(self):
        return str(self.tid)+' '+str(self.type)

    def __gt__(self, event):
        return self.tid > event.tid
    