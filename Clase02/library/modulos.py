def par_impar(num):
    if num%2 == 0:
        par = True
    else:
        par = False
    return par

def primo(num):
    i = 1
    cont = 0
    while i <= num:
        if num % i == 0:
            cont += 1
              
        i += 1

    if cont == 2:
        primo = True
    else:
        primo = False
    return primo

    def num_perfecto(num):
    i = 1
    suma = 0
    while i < num:
        if num%i == 0:
            suma = suma + i

        i += 1

    if suma == num:
        perfecto = True
    else:
        perfecto = False

    return perfecto

def f_exponencial(x):
    suma = 0

    for n in range(0, 50):
        suma += math.pow(x, n) / math.factorial(n)
    return suma  