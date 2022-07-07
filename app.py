class Calculator:
    
    def __init__(self,a=10,b=10,c=10) -> None:         # -> is functional annotations
        self.a = a
        self.b = b
        self.c = c
    
    def sum(self) -> int: 
        return (self.a + self.b + self.c)
    
    def diff(self) -> int:
        if self.a>self.b and self.a>self.c:
            if self.b>self.c:
                return (self.a - self.b - self.c)
            else:
                return (self.a - self.c - self.b)
        elif self.b>self.a and self.b>self.c:
            if self.a>self.c:
                return (self.b - self.a - self.c)
            else:
                return (self.b - self.c - self.a) 
        else:
            if self.a>self.b:
                return (self.c - self.a - self.b)
            else:
                return (self.c - self.b - self.a)
        
    def mul(self) -> int: 
        return (self.a * self.b * self.c) 
     
    def div(self) -> float: 
        return (self.a / self.b / self.c)      
    
    def rem(self) -> int:
        return (self.a % self.b % self.c)         