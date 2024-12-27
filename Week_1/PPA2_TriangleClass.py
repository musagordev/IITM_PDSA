class Triangle:
    def __init__(self, a,b,c):
        self.a = a
        self.b = b
        self.c = c
    
    def Is_valid(self):
        if self.a + self.b > self.c and self.a + self.c > self.b and self.b + self.c > self.a:
            return('Valid')
        else:
            return('Invalid')
    
    def Side_Classification(self):
        if Triangle(self.a,self.b,self.c).Is_valid() == 'Invalid':
            return('Invalid')
        else:
            if self.a == self.b == self.c:
                return('Equilateral')
            elif self.a == self.b or self.a == self.c or self.b == self.c:
                return('Isosceles')
            else:
                return('Scalene')
    
    def Angle_Classification(self):
        if Triangle(self.a,self.b,self.c).Is_valid() == 'Invalid':
            return('Invalid')
        else:
            l=[self.a,self.b,self.c]
            small,mid,high = sorted(l)
            if small ** 2 + mid ** 2 > high ** 2:
                return('Acute')
            elif small ** 2 + mid ** 2 == high ** 2:
                return('Right')
            elif small ** 2 + mid ** 2 < high ** 2:
                return('Obtuse')
        
    def Area(self):
        if Triangle(self.a,self.b,self.c).Is_valid() == 'Invalid':
            return('Invalid')
        else:
            s = (self.a+self.b+self.c)/2
            area = (s*(s-self.a)*(s-self.b)*(s-self.c))**0.5
            return(area)
        
a=int(input())
b=int(input())
c=int(input())
T=Triangle(a,b,c)
print(T.Is_valid())
print(T.Side_Classification())
print(T.Angle_Classification())
print(T.Area())
