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