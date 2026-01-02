import unicodedata

def palindromo(frase):
    
    frase.lower()
    
    frase_sem_acentos = unicodedata.normalize('NFKD', frase).encode('ascii', 'ignore').decode('utf-8')
    
    letras = [letra for letra in frase_sem_acentos if letra.isalpha()]   
    
    letras_invertidas = letras[::-1]
    
    if (letras == letras_invertidas):
        print("é palíndromo!")
    else:
        print("não é palíndromo!")
        
palindromo("ame o poema")