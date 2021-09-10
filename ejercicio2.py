from library.modulos import primo

def principal ():
    numero=int(input("digite un nummero"))
    if primo(numero):
        print("este numero es primo")
    else:
        print("este numero no es primo")



if __name__ == "__main__":
      principal()
