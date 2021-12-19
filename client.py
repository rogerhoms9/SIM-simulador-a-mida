

class Client:

   def __init__(self,id, creationTime, tipus):
      self.id=id
      self.creationTime=creationTime
      self.tipus =tipus

   def __repr__(self):
      return "Client "+str(self.id)+' de tipus '+str( "carn" if self.tipus==0 else "peix")

