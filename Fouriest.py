#!/usr/bin/env python

def fft(i):
  a=[]
  for b in range(5,i+1):
    f=0
    n=i
    t=1
    while n:
      f+=((n%b)==4)
      n/=b
    if f>=t:
      t=f
      a.append([f,b])
  return [j[1] for i, j in enumerate(a) if j[0] == (sorted(a,reverse=True)[0][0]) and j[0] != 0]


for x in range(0,100):
  print str(x)+"->"+str(fft(x))

