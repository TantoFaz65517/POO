class retangulo:
    def __init__(self, a, b):
        if b <= 0 or a <= 0:
            raise ValueError(" valor positivo")
        self.__b = b
        self.__a = a

    def set_altura(self, a):
        x = int(input())
        set.a(x)
    
    def set_base(self, b):
        
    def CalcArea(self):
        return self.b * self.a
    
    def CalcDiagonal(self)
        return (self.a**2 + self.b**2) * 0.5
