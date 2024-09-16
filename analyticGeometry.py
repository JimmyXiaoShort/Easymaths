class point:
    
    def __init__(self,x:int|float,y:int|float) -> None:
        self.x = x
        self.y = y
    
    def __repr__(self) -> str:
        return f"Point ({self.x}, {self.y})"
    
    def __str__(self) -> str:
        return f"Point ({self.x}, {self.y})"

class line:

    def __init__(self,A:int|float,B:int|float,C:int|float) -> None:
        self.A = A
        self.B = B
        self.C = C

    def __repr__(self) -> str:
        return f"Line {self.A}x + {self.B}y + {self.C} = 0"
    
    def __str__(self) -> str:
        return f"Line {self.A}x + {self.B}y + {self.C} = 0"
    
    def getSlope(self) -> float:
        if self.B != 0:
            return -(self.A / self.B)
        else:
            raise SyntaxError("The slope is unavilable")
    
    def getIntercept_Y(self) -> float:
        if self.A != 0:
            return (self.C / self.B)
        else:
            raise SyntaxError("The intercept on Y is unavilable")
    
    def getIntercept_X(self) -> float:
        if self.B != 0:
            return (self.C / self.A)
        else:
            raise SyntaxError("The intercept on X is unavilable")
        
    def getIntersection(self, other) -> point:
        try:
            if (self.getSlope() == other.getSlope()):
                raise SyntaxError("The intersection is unavilable")
        except SyntaxError:
            raise SyntaxError("The intersection is unavilable")
        else:
            x = (self.B * other.C - other.B * self.C) / (self.A * other.B - other.A * self.B)
            y = (self.A * other.C - other.A * self.C) / (other.A * self.B - self.A * other.B)
            return point(x, y)
