class Hashing:
  def __init__(self,c1,c2,m):
    self.hashtable = []
    for i in range(m):
        self.hashtable.append(None)     
    self.c1 = c1
    self.c2 = c2
    self.m = m
  def hash_function(self,data):
      i = 0
      key = (data % self.m + self.c1*i + self.c2*(i**2)) % self.m
      while self.hashtable[key] != None and i < self.m:
          key = (data % self.m + self.c1*i + self.c2*(i**2)) % self.m
          i = i + 1
      return key
  def store_data(self,data):
      if self.hashtable.count(None) != 0:
          key = self.hash_function(data)
          self.hashtable[key] = data
      else:
          print('Hash table is full')
  
  def display_hashtable(self):
      return self.hashtable
      
c1 = int(input())
c2 = int(input())
m = int(input())
data=eval(input())
A = Hashing(c1,c2,m)
for i in data:
	A.store_data(i)
print(A.display_hashtable())
