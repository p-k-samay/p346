import my_lib.ch as ch #Cholesky
import my_lib.gs as gs #Gauss-Seidel
def main():
    path='C:\\Users\\pksam\\Desktop\\Codes\\matrix2.csv' #arg matrix path
    ch.main(path) 
    gs.main(path) 

main()