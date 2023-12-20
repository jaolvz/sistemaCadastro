import sqlite3
bd = sqlite3.connect('cadastros.db')
cursor = bd.cursor()

cursor.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND name='pessoas'")
if cursor.fetchone() is None:
    cursor.execute("CREATE TABLE pessoas (nome text, idade integer, email text)")
    bd.commit()

i=0
while(i!=3):
    dec = int(input("1 - Cadastrar novo usuário\n2 - Mostrar todos usuários\n3 - Sair\n"))
    match dec:
        case 1:
            nome = input("Informe o nome: ")
            idade = int(input("Informe a idade: "))
            email = input("Informe seu email: ")
            cursor.execute(f"INSERT INTO pessoas VALUES (?,?,?)", (nome,idade,email))
            bd.commit()
            print("Cadastro concluído com sucesso!")
        case 2:
            cursor.execute("SELECT * FROM pessoas")
            print(cursor.fetchall())
        case 3:
            i=3



