def maior(array):
    maior = array[0]
    for i in range(len(array)):
        if (array[i] > maior):
           maior = array[i]
    print(f"o maior número é {maior}")    

def menor(array):
    manor = array[0]
    for i in range(len(array)):
        if (array[i] < manor):
           menor = array[i] 
    print(f"o menor número é {menor}")
    
def media(array):
    quantidade = 0
    soma = 0
    for i in range(len(array)):
        quantidade += 1
        soma += array[i]
    media = soma / quantidade
    print(f"a média dos números no array é {media}")
    
def analise(array):
    maior(array)
    menor(array)
    media(array)

lista = [1, 4, 9, 9, 99, 8, 0, 33]

analise(lista)