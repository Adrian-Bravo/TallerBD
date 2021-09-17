from library.modulos import f_exponencial

def principal():
    x = float(input("Digite el valor de X: "))
    resultado = f_exponencial(x)
    print(f"El resultado de la funcion exponencial es {resultado}")


if __name__ == "__main__":
    principal()