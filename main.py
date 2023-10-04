import random as rd
import string
import sqlite3 as sql
import hashlib as hlib
import os

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


def cria_hash(senhaCrip, salt=None):
    # Cria um salt com um valor de 126 bytes 16bits
    if salt is None:
        salt = os.urandom(16)

    # Junta a senha mais o salt gerado pelo sistema
    senha_salt = senhaCrip.encode('utf-8') + salt

    # Cria a criptografia
    sha256 = hlib.sha256()
    sha256.update(senha_salt)
    hash_senha = sha256.digest()


    return salt, hash_senha

def criar_tabela_usuarios():
    conexao = sql.connect('senha_criptografadas.db')
    cursor = conexao.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS Usuarios (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        SenhaHash TEXT)''')
    conexao.commit()
    conexao.close()

#Banco de dados das senhas
def guardar_senha(senha):
    bd_senha = sql.connect('senha_criptografadas.db')
    cursor = bd_senha.cursor()
    guardar_sql = f"INSERT INTO Usuarios(SenhaHash) VALUES(?)"
    cursor.execute(guardar_sql, (senha))
    bd_senha.commit()


def verificar_dados(bd, dados = False):
    if dados:
        conexao = sql.connect(bd)
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM Usuarios")
        registros = cursor.fetchall()
        for registro in registros:
            print(registro)
        conexao.close()


#Gera a senha e armazena
def gerar_senha():
    senha = []
    for i in range(qtd):
        # Gera um numero para sortear o valor que sera usado como senha
        tipo_caractere = rd.randint(1, 4)
        if tipo_caractere == 1:
            senha.append(rd.choice(lista_letra_min))
        elif tipo_caractere == 2:
            senha.append(rd.choice(lista_letra_mai))
        elif tipo_caractere == 3:
            senha.append(str(rd.choice(lista_numeros)))
        else:
            senha.append(rd.choice(especiais))
    
    senha_texto = ''.join(senha)
    rd.shuffle(senha_texto)

    salt, hash_senha = cria_hash(senha_texto)
    guardar_senha(hash_senha)


criar_tabela_usuarios()

while True:
    qtd = int(input('\nDeseja uma senha de quantos digitos?:'))
    if 8 <= qtd <= 20:
        break
    else:
        print('A senha deve ter entre 8 e 20 digitos')
        
verificar_dados('senha_criptografadas.db', dados=True)
