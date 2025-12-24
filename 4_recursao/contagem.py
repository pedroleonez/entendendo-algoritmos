def contagem(lista):
    if not lista:
        return 0
    
    soma = 0
    soma += 1
    resto_da_lista = lista[1:]
    
    return soma + contagem(resto_da_lista)

itens = [6, 7, 9, 6, 2, 1]
total = contagem(itens)
print(f"a quantidade de itens é = {total}")

def contagem_melhor(lista):
    if not lista:
        return 0
    return 1 + contagem_melhor(lista[1:])