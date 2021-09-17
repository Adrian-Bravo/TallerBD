from library.modulos import num_perfecto

def principal():
    numero = int(input("Digite un numero: "))
    if num_perfecto(numero):
        print("Es perfecto")
    else:
        print("No es perfecto")


if __name__ == "__main__":
    principal()
