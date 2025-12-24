def soma(lista):
    # caso base
    if not lista:
        return 0
    
    # usando primeiro item da lista atual
    usado = lista[0]
    resto_da_lista = lista[1:]
    
    # chamada recursiva
    return usado + soma(resto_da_lista)
    
# teste
numeros = [5, 6, 7, 51, 36]    
total = soma(numeros)
print(f"soma total dos números = {total}")