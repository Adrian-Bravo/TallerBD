

from library.modulos import par_impar

def principal():
    numero=int (input("Digite un numero"))
    if par_impar(numero):
        print("Este numero es par ")
    else: 
        print("Este numero es impar")

if __name__ == "__main__":
      principal()

