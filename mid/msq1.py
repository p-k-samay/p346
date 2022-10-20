import my_lib.lcg as lcg
def area_ellipse(n):
    count=0
    total=0
    x=lcg.random(0,n)
    y=lcg.random(0,n)
    for i,j in zip(x,y):
      if (i**2/1 + j**2/4) <= 1:
        count+=1
    for i,j in zip(x,y):
      if i<= 2 and j <= 1:
        total+=1

    area = count/total
    print('The area of ellipse is : '+str(area))
area_ellipse(1100)