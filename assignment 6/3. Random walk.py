import matplotlib.pyplot as plt
import mylibrary.lcg as lcg
def randomwalk(seed1,seed2,n):
    x=lcg.random(seed1,n)               
    y=lcg.random(seed2,n)
    X=[0.0]
    Y=[0.0]
    sum=0.0
    rms=0.0
    dis=0.0
    x2=0.0
    y2=0.0
    #Loop to find the points
    for i in range (0,n) :
        x1=((x[i]*2)-1)+x2
        y1=((y[i]*2)-1)+y2
        X.append(x1)
        Y.append(y1)
        sum+=((x1-x2)**2 +(y1-y2)**2)
        x2=x1
        y2=y1
    rms=pow((sum/n),0.5)
    dis=pow(((x1**2)+(y1**2)),0.5)
    output("The rms distance for random walk of "+str(n)+" steps is : "+str(rms)+"\n")
    output("The net displacement for random walk of "+str(n)+" steps is : "+str(dis)+"\n")
    plt.title("\nRandom walk of "+str(n)+" steps")
    plt.plot(X,Y)
    plt.show()

    #write output
def output(p):
    with open("C:\\Users\\pksam\\Desktop\\Assignment-2\\Output(Q3).txt",'a') as file:
        file.write(p)
        file.close()
    return

#create output
with open("C:\\Users\\pksam\\Desktop\\Assignment-2\\Output(Q3).txt",'w') as file:
    file.write("OUTPUT : \n")
    file.close()

randomwalk(10,27,300)
randomwalk(10,27,600)
randomwalk(10,27,900)