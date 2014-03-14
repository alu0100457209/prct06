#!/usr/bin/python

import sys

PI = 3.1415926535897931159979634685441852

def aproximacion_pi(n):
  suma = 0.0
  for i in range(1, n+1):
    x_i = (i - 0.5) / float(n)
    fx_i = 4.0 / (1.0 + x_i * x_i)
    suma = suma + fx_i
  aproximacion = suma / float(n)
  return aproximacion

lista = []
n = int(sys.argv[1])
veces = int(sys.argv[2])
  
for i in range(1,veces+1):
  a = i * n
  s = aproximacion_pi(a)
  lista = lista + [s]

print ('i    PI35DT     lista i    PI35DT - lista i')
for i in range(veces):
  print ('%i %.10f %.10f %.10f') %(i+1, PI, lista[i], abs(PI-lista[i]))