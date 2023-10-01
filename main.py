import random as rd
import string

print('=*'*15)
print("Bem vindo ao gerador de Senhas")
print('=*'*15)

especiais = ['!', '@', '#', '$', '%', '?', '*', '&']
print('Explicação sobre a senha:')
print('(1) Terá no minimo são 8 digitos')
print("(2) O maximo de caracteres são 20")
print('(3) Sera uma mescla de letras maiusculas e minusculas, numero e caracteres espaciais:', especiais)

alfabeto_min = string.ascii_lowercase
alfabeto_mai = string.ascii_uppercase
lista_letra_min = list(alfabeto_min)
lista_letra_mai = list(alfabeto_mai)
lista_numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
senha = []

while True:
    qtd = int(input('\nDeseja uma senha de quantos digitos?:'))
    if 8 <= qtd <= 20:
        break
    else:
        print('A senha deve ter entre 8 e 20 digitos')


for i in range(qtd):
    tipo_caractere = rd.randint(1, 4)

    if tipo_caractere == 1:
        senha.append(rd.choice(lista_letra_min))
    elif tipo_caractere == 2:
        senha.append(rd.choice(lista_letra_mai))
    elif tipo_caractere == 3:
        senha.append(str(rd.choice(lista_numeros)))
    else:
        senha.append(rd.choice(especiais))

rd.shuffle(senha)
print("Sua senha é: ", end='')
for i in senha:
    print(i, end='')
