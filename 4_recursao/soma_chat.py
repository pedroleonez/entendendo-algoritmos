def comer_numeros(lista):
    # Caso base: se a lista estiver vazia, paramos
    if not lista:
        print("A lista acabou! Tudo devorado.")
        return 0
    
    # "Comendo" o primeiro item
    comido = lista[0]
    resto_da_lista = lista[1:]
    
    print(f"Comi o número {comido}. Restam: {resto_da_lista}")
    
    # Chamada recursiva: a função chama a si mesma com a lista menor
    return comido + comer_numeros(resto_da_lista)

# Testando
meus_numeros = [10, 20, 30, 40]
total = comer_numeros(meus_numeros)
print(f"Total digerido: {total}")