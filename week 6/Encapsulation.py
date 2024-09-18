class Person:
    def _init_(self):
        self.A = "James"
        self._B = "James Bond"
    def Printname(self):
        print(self.A)
        print(self._B)
        
p = Person()
p.A
# p._B
    
p.Printname()