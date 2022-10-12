import numpy as np
import csv
def printm(A):
  n=np.size(A,0)
  m=np.size(A,1)
  for i in range (n):
    for j in range (m):
      if A[i,j]==0:
        A[i,j]=abs(A[i,j])
      print(round(float(A[i,j]),2),end='          ')
    print("\n")
  print("\n")

def swap(A):
  n=len(A)
  for i in range (0,n):
    y=A[i,i]
    x=i
    s=0
    for j in range (0,n):
      k=A[j,i]
      if k**2 > y**2:
        y=k
        x=j
    for k in range (0,n+1):
      s=float(A[x,k])
      A[x,k]=float(A[i,k])
      A[i,k]=float(s)
  print("The diagonally dominant matrix :-\n")
  printm(A)
  return A

def gauussseidel(A):
    A=swap(A)
    n=len(A)
    X1=[]
    X2=[]
    for i in range (0,n):
        X1.append(0.0)
    X1=np.matrix(X1)
    X2=np.matrix(X1)
    ep=0.0
    c=0
    for i in range (0,500):
        for j in range (0,n):
            sum=0.0
            sum2=0.0
            for l in range(j+1,n):
                sum=sum+(A[j,l]*X1[0,l])
            for m in range(1,j):
                sum2=sum2+(A[j,m]*X2[0,m])
            X2[0,j]= (A[j,n]-sum-sum2)/A[j,j]
        a=0
        if c > 0 :
            for k in range (0,n):
                ep = ((X2[0,k]-X1[0,k])*100)/X1[0,k]
                if abs(ep) < 10**-6 :
                    a+=1
        if a==n:
            break
        X3=np.matrix(X2)
        X1=X3
    print("The solution using Gauss-Seidel method: \n")
    for i in range (0,n):
        print("x"+str(i+1)+" = "+str(X2[0,i]))

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
    X=np.matrix(input(p))
    print("The input matrix : \n")
    printm(X)
    gauussseidel(X)
    return
