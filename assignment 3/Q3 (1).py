import my_lib.ga as gs #Gauss-Seidel
import my_lib.lu as ld #LU
def main():
    path='C:\\Users\\pksam\\Desktop\\Codes\\matrix3.csv' #arg matrix path
    lu.main(path) 
    ga.main(path) 

main()