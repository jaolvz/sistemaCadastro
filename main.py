import sqlite3

def validar_email(email ):
    bd= sqlite3.connect('cadastros.db')
    cursor = bd.cursor()
    cursor.execute("SELECT * FROM pessoas")
    emails= [l[2] for l in  cursor.fetchall()]
    if email.find(".com")!=-1 and email.find("@")!=-1:
        if email in emails:
            return 0
        else:
            return 1
    else:
        return -1



def main():
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
                if validar_email(email)== 1:
                    cursor.execute(f"INSERT INTO pessoas VALUES (?,?,?)", (nome,idade,email))
                    bd.commit()
                    print("Cadastro concluído com sucesso!")
                elif validar_email(email)== -1:
                    print("Email inválido.")
                else:
                    print("Email já cadastrado")
            case 2:
                cursor.execute("SELECT * FROM pessoas")
                print(cursor.fetchall())
            case 3:
                i=3
    bd.close()

if __name__ == "__main__":
    main()


