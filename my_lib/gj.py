import numpy as np
import csv
def printm(A):
  n=len(A)
  for i in range (n):
    for j in range (n+1):
      if A[i,j]==0:
        A[i,j]=abs(A[i,j])
      print(float(A[i,j]),end='         ')
    print("\n")
  print("\n") 

def swap(A,n):
  x=n
  y=A[n,n]
  m=len(A)
  for i in range (m):
    for j in range (n,(n+1)):
      k=A[i,j]
      if k**2 >= y**2:
        y=k
        x=i
  if x<n:
    return
  r=np.matrix(A[x])
  A[x]=A[n]
  A[n]=r

def gaussjordan(A):
  n=len(A)-1
  c=0.0
  for i in range (0,n+1):
    if A[i,i]==0:
      swap(A,i)
    A[i]=A[i]/A[i,i]
    for j in range (i+1,n+1):
      c=(A[j,i])/(A[i,i])
      A[j]=A[j]-(c*A[i])

  for i in range (0,n):
    k=n-i
    for j in range (0,k):
      l=k-j-1
      c=(A[l,k])/(A[k,k])
      A[l]=A[l]-(c*A[k])
  return (A)

def input(path):
  i=0
  j=0
  A=[]
  with open(path) as x:
    cr=csv.reader(x)
    next(cr)
    for line in cr:
      row=[]
      for n in line:
        row.append(float(n))
      A.append(row)
  return (np.matrix(A))

def main(p):
  p=str(p)
  X = input(p)
  print("The input matrix : \n")
  printm(X)
  Y=gaussjordan(X)
  n=len(Y)
  print("The solution using Gauss-Jordon elimination : \n")
  for i in range (0,n):
    print("x"+str(i+1)+" = "+str(Y[i,n]))
  return


