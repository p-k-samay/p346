def gauss_siedel(A,b,e,n):
    r=[0 for i in range(len(A[0]))]
    for k in range(100):
        t=0
        for i in range(n):
            sum1=sum(A[i][j]*r[j] for j in range(i))
            sum2=sum(A[i][j]*r[j] for j in range(i+1,n))

            solution=(1/A[i][i])*(b[i]-sum1-sum2)
            if abs(solution-r[i])<e:
                t+=1
            r[i]=solution
        if i==n:
            break
    return r
    print(r)
A=[[-2  ,  0  ,  0   , -1  ,  0  ,  0.5],
    [0  ,  4    ,0.5 ,  0  ,  1   , 0],
    [0   , 0.5 , 1.5  , 0   , 0 ,   0],
    [-1  ,  0 ,   0   , -2 ,   0   , 1],
    [0 ,   1  ,  0   ,  0  , -2.5 , 0],
    [0.5 , 0  ,  0    , 1   , 0  , -3.75]]
b=[-1,0,2.75,2.5,-3,2]
gauss_siedel(A,b,10**-6,6)
