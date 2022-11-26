import numpy as np
import csv
def printmatrix(M):
  n=np.size(M,0)
  m=np.size(M,1)
  for i in range (n):
    for j in range (m):
      if M[i,j]==0:
        M[i,j]=abs(M[i,j])
      print(round(float(M[i,j]),2),end=' \t')
    print("\n")
  print("\n")

def swap(M):
  n=len(M)
  for i in range (0,n):
    y=M[i,i]
    x=i
    s=0
    for j in range (0,n):
      k=M[j,i]
      if k**2 > y**2:
        y=k
        x=j
    for k in range (0,n+1):
      s=float(M[x,k])
      M[x,k]=float(M[i,k])
      M[i,k]=float(s)
  return M

def gauss_seidel(M):
    M=swap(M)
    n=len(M)
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
                sum=sum+(M[j,l]*X1[0,l])
            for m in range(0,j):
                sum2=sum2+(M[j,m]*X2[0,m])
            X2[0,j]= (M[j,n]-sum-sum2)/M[j,j]
        a=0
        if c > 0 :
            for k in range (0,n):
                ep = ((X2[0,k]-X1[0,k])*100)/X1[0,k]
                if abs(ep) < 10**-6 :
                    a+=1
        if a==n:
            break
        x3=np.matrix(X2)
        X1=x3
    print("The solution of the given linear equations using Gauss-Seidel method is : \n")
    for i in range (0,n):
        print("x"+str(i+1)+" = "+str(X2[0,i]))

def input(path):
  i=0
  j=0
  M=[]
  with open(path) as x:
    cr=csv.reader(x)
    next(cr)
    for line in cr:
      row=[]
      for n in line:
        row.append(float(n))
      M.append(row)
  return (np.matrix(M))

def main(q):
    q=str(q)
    A=np.matrix(input(q))
    print("The input matrix is : \n")
    printmatrix(A)
    gauss_seidel(A)
    return