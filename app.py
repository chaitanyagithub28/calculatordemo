class Calculator:
    
    def __init__(self,a=10,b=10) -> None:         # -> is functional annotations
        self.a = a
        self.b = b
    
    def sum(self) -> int: 
        return (self.a + self.b)
    
    def diff(self) -> int:
        if self.a > self.b:
            return (self.a - self.b)
        else:
            return (self.b - self.a)
        
    def mul(self) -> int: 
        return (self.a * self.b) 
     
    def div(self) -> float: 
        return (self.a / self.b)      
    
    def rem(self) -> int:
        if self.a > self.b: 
            return (self.a % self.b)   
        else:
            return (self.b % self.a)   