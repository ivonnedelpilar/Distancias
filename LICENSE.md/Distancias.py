
# coding: utf-8

# ## DISTANCIAS 

# In[17]:


import math
import random


# In[18]:


def listaAleatorios(n):
      lista = [0]  * n
      for i in range(n):
          lista[i] = random.randint(0, 1000)
      return lista

#print("Ingrese cuantos numeros aleatorios desea obtener")
#n=int(input())
n=5

aleatorios=listaAleatorios(n)
print(aleatorios)


# Distancia Euclidiana

# In[19]:


def Euclidiana(x1,x2,y1,y2):
    dist_euc = math.sqrt(math.pow(x2-x1,2) + math.pow(y2-y1,2))
    return dist_euc
Euclidiana(aleatorios[1],aleatorios[2],aleatorios[3],aleatorios[4])


# Distancia Manhattan

# In[20]:


def Manhattan(x1,x2,y1,y2):
    dist_man = abs((x1-x2) + (y1-y2))
    return dist_man
Manhattan(aleatorios[1],aleatorios[2],aleatorios[3],aleatorios[4])


# Distancia o Similitud Coseno

# In[21]:


def Coseno(x,y):
    dist_cos = x*y/math.sqrt(x^2*y^2)
    return dist_cos
Coseno(aleatorios[1],aleatorios[2])


# Distancia Jaccard

# In[33]:


def Jaccard(x, y): 
    x = set(x.split()) 
    y = set(y.split()) 
    return float(len(x & y))/len(x | y) 

Jaccard("machine learning", "deep learning")

