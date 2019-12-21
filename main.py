

def armonica(n):
  return(1/(n+1))
def hiperarmonica(n):
  return((1/(n+1)**2))
def telescopica(n):
 return(1/2**n)
def leibniz(n):
  return((4*(-1)**n)/(2*n+1))
def serie(f,n):
  a=0
  for i in range(n):
    a=a+f(i)
    print(a)
  return(a)
print(serie(leibniz,1000000))
#print(serie(telescopica,60))

