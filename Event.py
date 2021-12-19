
class Event:
    def __init__(self,object,temps,tipus,entitat=None,fra=None):
            # inicialitzar element de simulacio
        self.entitatsTractades=0
        self.type=tipus
        self.object=object
        self.tid=temps
        self.entitat=entitat

