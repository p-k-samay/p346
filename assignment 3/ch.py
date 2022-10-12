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

def cholesky(A):
    print("The input matrix : \n")
    printm(A)
    n=len(A)
    for i in range (0,n):
        for j in range (0,n):
            if A[i,j]!=A[j,i]:
                print('The matrix is not symmetric hence cannot be solved by cholesky decomposition method.\n')
                return 
    L=np.matrix(A)
    T=[]
    X=[]
    Y=[]
    for i in range (0,n): 
        X.append(0.0)
    X=np.matrix(X)
    Y=np.matrix(X)
    for i in range (0,n):
        for j in range (0,n):
            if j>i:
                L[i,j]=0.0
    for i in range (0,n):
        s=0.0
        for k in range (0,i):
            s=s+(L[i,k]*L[i,k])
        L[i,i]=np.sqrt(A[i,i]-s)
        for j in range (i+1,n):
            s1=0.0
            for x in range (0,i):
                s1=s1+(L[j,x]*L[i,x])
            L[j,i]=(A[j,i]-s1)/(L[i,i])
    for i in range (0,n):
        row=[]
        for j in range (0,n):
            row.append(L[j,i])
        T.append(row)
    T=np.matrix(T)
    for i in range (0,n):
        s2=0.0
        for j in range (0,i):
            s2=s2+(L[i,j]*Y[0,j])
        Y[0,i]=((A[i,n]-s2)/L[i,i])
    for i in range (n,0,-1):
        s3=0.0
        k=i-1
        for j in range (k+1,n):
            s3= s3+ (T[k,j]*X[0,j])
        X[0,k]=((Y[0,k]-s3)/T[k,k])
    print("The solution using Cholesky decomposition method: \n")
    for i in range (0,n):
        print("x"+str(i+1)+" = "+str(X[0,i]))
    return X

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
    A=np.matrix(input(p))
    cholesky(A)
    return


