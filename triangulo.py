def triangulo():
    x = int(input("lado x: "))
    y = int(input("lado y: "))
    z = int(input("lado z: "))
    if ((x + y) > z) and ((y + z) > x) and ((x + z) > y):
        print("é possível formar um triângulo com os valores!")
    else:
        print("não é possível formar um triângulo com os valores!")
        
triangulo()