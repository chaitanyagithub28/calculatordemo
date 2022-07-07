class Calculator:
    
    def __init__(self,a=10,b=10,c=10) -> None:         # -> is functional annotations
        self.a = a
        self.b = b
        self.c = c
    
    def sum(self) -> int: 
        return (self.a + self.b + self.c)
    
    def diff(self) -> int:
        return (self.a - self.b - self.c)
        
    def mul(self) -> int: 
        return (self.a * self.b * self.c) 
     
    def div(self) -> float: 
        return (self.a / self.b / self.c)      
    
    def rem(self) -> int:
        return (self.a % self.b % self.c)         