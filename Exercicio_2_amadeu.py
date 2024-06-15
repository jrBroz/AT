import sqlite3

    
def cadastrar_livro():
    
    nome_livro = input("Insira o Nome do livro:  ")
    isbn = input("Insira o ISBN:  ")
    categoria = input("Insira a categoria do livro:  ")
    id_autor = input("Insira um id: ")
    try:    
        conn = sqlite3.connect("Biblioteca.db")
        cursor = conn.cursor()
                 
        cursor.execute("""
                       
                CREATE TABLE IF NOT EXISTS Livros(ID_Livro INTEGER PRIMARY KEY AUTOINCREMENT,
                NOME_LIVRO VARCHAR(100),
                ISBN VARCHAR(255),
                CATEGORIA VARCHAR(100),
                id_autor INTEGER,
                FOREIGN KEY(id_autor) REFERENCES Autor(ID_AUTOR));""")
            
        cursor.execute("INSERT INTO Livros(NOME_LIVRO, ISBN, CATEGORIA, id_autor) VALUES (?,?,?,?);", (nome_livro, isbn, categoria, id_autor))    
            
        conn.commit()
        conn.close()
    
    except ConnectionError:
        print("Erro ao cadastrar livro, tente novamente mais tarde.")
        
    except sqlite3.OperationalError as e: 
        print("Um erro ocorreu" , e)
        print("-" * 30)



def cadastrar_autor():

    try:
            conn = sqlite3.connect("Biblioteca.db")
            cursor = conn.cursor()
        
            nome_autor = input("Insira o nome do autor:  ")
                
            cursor.execute("""
                    CREATE TABLE IF NOT EXISTS Autor(ID_AUTOR INTEGER PRIMARY KEY AUTOINCREMENT,
                    NOME_AUTOR VARCHAR(100));""") 

            cursor.execute("INSERT INTO Autor(NOME_AUTOR) VALUES (?);", (nome_autor,))    #Precisa ter , se nao o parametro nao e visto como tupla 

            conn.commit()
            conn.close()
            
    except ConnectionError:
        print("Erro ao se conectar ao banco de dados. ")
                
    except sqlite3.OperationalError: 
        print("O que vc procura não existe.")
        print("-" * 30)
    
                
def listar_todos_autor():

    try:
        conn = sqlite3.connect("Biblioteca.db")
        cursor = conn.cursor()
        
        print("Listando todos os Autores cadastrados ate o momento:  ")
        print("-" * 30)
                    
        cursor.execute("SELECT * FROM Autor;")     # TALVEZ SELECT NOME_AUTOR

        autor = cursor.fetchall()
        print(autor)        
        print("-" * 30)
            
        conn.commit()
        conn.close()        
        
        
    except ConnectionError:
        print("Erro ao se conectar ao banco de dados. ")
    
    except sqlite3.OperationalError: 
        print("Vazio.")
        print("-" * 30)

    



def listar_todos_livro():
    
    try:
        conn = sqlite3.connect("Biblioteca.db")
        cursor = conn.cursor()
        
    
        print("Listando todos os Livros cadastrados ate o momento:  ")
        print("-" * 30)
                    
        cursor.execute("SELECT * FROM Livros;")    

        livro = cursor.fetchall()
        print(livro)
        print("-" * 30)
            
    except ConnectionError:
        print("Erro ao se conectar ao banco de dados. ")
        
    except sqlite3.OperationalError: 
        print("Vazio.")
        print("-" * 30)
    
    
            
def atualizar_autor():
    listar_todos_autor()
    
            
    try:   
        conn = sqlite3.connect("Biblioteca.db")
        cursor = conn.cursor()
                
        print("Qual Autor desejas atualizar?")
        
        primeiro_nome_autor = input("Nome atual do autor: ")
        
            
        escolha = input("[1] Para mudar o Nome do autor:")
        
        match (escolha):    
            
            case '1':
                novo_nome = input("Escreva o novo nome:  ")
                cursor.execute("UPDATE AUTOR SET NOME_AUTOR=(?) WHERE NOME_AUTOR=(?);", (novo_nome,primeiro_nome_autor))     
                conn.commit()
                conn.close()
                
            case _:
                
                print("Comando não se reconhecido.")
                
    except ConnectionError:
        print("Erro ao se conectar ao banco de dados. ")
        print("-" * 30)
        
    except sqlite3.OperationalError: 
        print("Houve um erro.")
        print("-" * 30)
        
    
        
def atualizar_livro():
    listar_todos_livro()
    
    try:
        conn = sqlite3.connect("Biblioteca.db")
        cursor = conn.cursor()
    
        
        print("Qual Livro desejas atualizar?")
        
        
        
        escolha = input("Gostaria de mudar [1] Nome do Livro, [2] ISBN ou [3] Categoria:  ")
        
        match (escolha):    
            
            case '1':
                livro_para_atualizacao = input("Nome do livro para atualizacao:  ")
                novo_nome = input("Escreva o novo nome:  ")
                cursor.execute("UPDATE Livros SET NOME_LIVRO=(?) WHERE NOME_LIVRO=(?);", (novo_nome, livro_para_atualizacao))     
                conn.commit()
                conn.close()
            case '2':
                
                isbn_antigo = input("Insira o ISBN antigo:  ")
                novo_isbn = input("Insira o novo ISBN:   ")
                cursor.execute("UPDATE Livros SET ISBN=(?) WHERE ISBN=(?);", (novo_isbn,isbn_antigo))     
                conn.commit()
                conn.close()    
                
            case '3':
            
                categoria_antiga = input("Escreva a antiga Categoria:  ") 
                nova_categoria = input("Escreva a nova Categoria :  ")                
                cursor.execute("UPDATE Livros SET CATEGORIA=(?) WHERE CATEGORIA=(?);", (nova_categoria,categoria_antiga))
                conn.commit()
                conn.close()
    
            case _:
                print("Insira uma opcao válida.")
                return
    
    except ConnectionError:
        print("Erro ao se conectar ao banco de dados. ")
        
    except sqlite3.OperationalError as e: 
        print("Houve um erro.", e)
        return
        
                
def deletar_autor():
    
    listar_todos_autor()
    
    try:
    
        conn = sqlite3.connect("Biblioteca.db")
        cursor = conn.cursor()
    
        id_autor = input("Qual ID do autor que desejas deletar: ")        
        cursor.execute("DELETE FROM AUTOR WHERE ID_AUTOR=(?);", (id_autor))
        conn.commit()
        conn.close()
        print("-" * 30)
        print("Autor deletado com sucesso.")
        
    except ConnectionError:
        print("Erro ao se conectar ao banco de dados. ")
                
    except sqlite3.OperationalError: 
        print("O que vc procura não existe.")
        # return
        

            
def deletar_livro():
    
    listar_todos_livro()
    try:
    
        conn = sqlite3.connect("Biblioteca.db")
        cursor = conn.cursor()
    
        id_livro = input("Qual ID do autor que desejas deletar: ")        
        cursor.execute("DELETE FROM LIVROS WHERE ID_LIVRO=(?);", (id_livro))
        conn.commit()
        conn.close()
        print("-" * 30)
        print("Livro deletado com sucesso.")
    
    except ConnectionError:
        print("Erro ao se conectar ao banco de dados. ")
        
    except sqlite3.OperationalError: 
        print("O que vc procura não existe.")
        # return



def listar_livros_publicados_por_autor():
    try:
    
        listar_todos_autor()
    
        conn = sqlite3.connect("Biblioteca.db")
        cursor = conn.cursor()
    
        autor_para_listar = input("Sobre qual autor, deseja ver os livros publicados?  ")
        cursor.execute("""

            SELECT Livros.NOME_Livro AS Nome_Do_Livro, Autor.NOME_AUTOR AS Autor
            FROM Livros
            JOIN Autor ON Livros.id_autor = Autor.ID_AUTOR
            WHERE AUTOR.NOME_AUTOR = (?) """, (autor_para_listar,))


        
        tudo = cursor.fetchall()
        print(tudo)        
        print("-" * 30)
        conn.commit()
        conn.close()
        
    
    except ConnectionError:
        print("Erro ao se conectar ao banco de dados. ")
        
    except sqlite3.OperationalError: 
        print("O que vc procura não existe.")
        


def menu():
    
    while True:
    
        print("[1] Cadastrar Autor, [2] Cadastrar Livro, [3] Atualizar Livro, [4] Atualizar Autor, [5] Listar Livro, [6] Listar Autor, [7] Deletar Livro, [8] Deletar Autor [9]Listar Livros por autor especifico, [10] Sair")
        print("-" * 30)
        escolha_usuario = input("Escolha:  ")
        
        match(escolha_usuario):
            
            case '1':
                cadastrar_autor()
                
            case '2':
                cadastrar_livro()
                
            case '3':
                atualizar_livro()
                                
            case '4':
                atualizar_autor()
                
            case '5':
                listar_todos_livro()
                
            case '6':
                listar_todos_autor()
                            
                
            case '7':
                deletar_livro()
                            
            case '8':
                deletar_autor()
                
            case '9':
                listar_livros_publicados_por_autor()
                
            case '10':
                break     
                    
            case _:
                print("Escolha inválida")
                            
menu()