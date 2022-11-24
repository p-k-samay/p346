#volume of an octant of a sphere
import mylibrary.lcg as lcg
def volume_octant(x0,n):
    count=0
    x=lcg.random(x0,n)
    y=lcg.random(x0,n)
    z=lcg.random(x0,n)
    #Loop to count the points inside the octant
    for i,j,k in zip(x,y,z):
      if (i**2 + j**2 + k**2) <= 1:
        count+=1
    volume = count/n
    output('The volume of one octant of the sphere is : '+str(volume))

#write output
def output(s):
    with open("C:\\Users\\pksam\\Desktop\\Assignment-2\\Output(Q2).txt",'a') as file:
        file.write(s)
        file.close()
    return

#create output
with open("C:\\Users\\pksam\\Desktop\\Assignment-2\\Output(Q2).txt",'w') as file:
    file.write("OUTPUT : \n")
    file.close()

volume_octant(10,1000)