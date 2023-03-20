import variables as variables
from math import factorial
# Halla el número de combinaciones de n objetos de r a la vez. 
def combinatoria_simple(n,r):
   C = 0
   # Verificar que los valores numéricos sean enteros y que r sea 
   # menor que n
   if type(n) == int and type(r) == int and r <= n:
      if n>0 and r>0: 
         C = factorial(n)/(factorial(r)*factorial(n-r))
         return C 
      else:
         raise Exception("Variables ingresadas no negativas.")
   else:
      raise Exception("Variables ingresadas no válidas.") 
     
# Halla el número de combinaciones entre dos conjuntos de objetos 
# y de dos r a la vez. 
def combinatoria_doble(n1,r1,n2,r2):
   C =combinatoria_simple(n1,r1)*combinatoria_simple(n2,r2)
   return C 
    
# Halla la probabilidasd de que un evento ocurra
def calcular_probabilidad(pm,em):
 P = 0
 if em > 0:
    P = round(pm/em,4)*100
    return P
 else:
      return None
 
#Verifica los datos ingresados por el usuario
def verificar_entrada(boletos,premios,organizador):
  if boletos >= variables.boletos_min and boletos <= variables.boletos_max:
    if premios >= variables.premios_min and premios <= variables.premios_max:
      if  organizador >= variables.organizadores_min and organizador <= variables.organizadores_max:
         if premios < organizador: 
          return True
  else:  
    return False
    
#Calcula la cantidad exacta de premios ganados (Punto B), de acuerdo al 60% de los premios 
def calcular_premios(premios):
   premios_b = int (.67*premios)
   return premios_b
    
def espacio_muestral(boletas,premios):
   if (boletas>=premios):
    return combinatoria_simple(boletas,premios)
   else: 
    return False

#Verifica que los valores ingresados por el usuario hayan sido numéricos
def verificar_numeros(boletos, premios, organizador):
   if type(boletos) == int and type(premios) == int and type(organizador) == int: 
      return True
   else: 
      return False



