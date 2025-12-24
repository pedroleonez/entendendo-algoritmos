def mais_alto(lista):
    if not lista:
        return 0
    
    sub_maior = mais_alto(lista[1:])
    
    if lista[0] > sub_maior:
        return lista[0]
    else:
        return sub_maior
    
valores = [5, 9, 12, 60, 54]
valor_mais_alto = mais_alto(valores)
print(f"o valor mais alto é = {valor_mais_alto}")