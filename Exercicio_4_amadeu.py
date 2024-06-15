import sqlite3


def cadastrar_livro():
    
    nome_livro = input("Insira o Nome do livro:  ")
    id_autor = input("Escreva o id do autor:  ")
    id_editora = input("Escreva o id da editora:  ")
    id_categoria = input("Escreva o id da editora:  ")
    pais_de_publicacao = input("Escreva qual pais de publicacao:  ")
    
    try:    
        conn = sqlite3.connect("BIBLIOTECA_ONLINE.db")
        cursor = conn.cursor()
                 
        cursor.execute("""
                       
                CREATE TABLE IF NOT EXISTS Livros(ID_Livro INTEGER PRIMARY KEY AUTOINCREMENT,
                TITULO VARCHAR(100), 
                PAIS_PUBLICACAO VARCHAR(100),
                id_autor INTEGER,
                id_editora INTEGER,
                FOREIGN KEY(id_autor) REFERENCES Autor(ID_AUTOR),
                FOREIGN KEY(id_editora) REFERENCES EDITORA(ID_EDITORA));""")

        cursor.execute("INSERT INTO Livros(TITULO, id_autor, id_editora, id_categoria,PAIS_PUBLICACAO) VALUES (?,?,?,?,?);", (nome_livro,id_autor, id_editora,id_categoria, pais_de_publicacao))    
            
        conn.commit()
        conn.close()
    
    except ConnectionError:
        print("Erro ao cadastrar livro, tente novamente mais tarde.")
        
    except sqlite3.OperationalError as e: 
        print("Um erro ocorreu" , e)
        print("-" * 30)



def cadastrar_autor():

    try:
            conn = sqlite3.connect("BIBLIOTECA_ONLINE.db")
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
        print("Algum erro ocorreu.")
        print("-" * 30)
        
    
    
    
    
    
def cadastrar_categoria():

    try:
        conn = sqlite3.connect("BIBLIOTECA_ONLINE.db")
        cursor = conn.cursor()
        
        nome_categoria = input("Insira o nome da Categoria:  ")
                
        cursor.execute("""
                    CREATE TABLE IF NOT EXISTS Categoria(ID_CATEGORIA INTEGER PRIMARY KEY AUTOINCREMENT,
                    NOME_CATEGORIA VARCHAR(100));""") 

        cursor.execute("INSERT INTO Categoria(NOME_CATEGORIA) VALUES (?);", (nome_categoria,))    #Precisa ter , se nao o parametro nao e visto como tupla 

        conn.commit()
        conn.close()
            
    except ConnectionError:
           print("Erro ao se conectar ao banco de dados. ")
                
    except sqlite3.OperationalError: 
        print("Algum erro ocorreu...")
        print("-" * 30)
        
        
        
def cadastrar_editora():

    try:
            conn = sqlite3.connect("BIBLIOTECA_ONLINE.db")
            cursor = conn.cursor()
        
            nome_editora = input("Insira o nome da Categoria:  ")
                
            cursor.execute("""
                    CREATE TABLE IF NOT EXISTS Editora(ID_EDITORA INTEGER PRIMARY KEY AUTOINCREMENT,
                    NOME_EDITORA VARCHAR(100));""") 

            cursor.execute("INSERT INTO Editora(NOME_EDITORA) VALUES (?);", (nome_editora,))    #Precisa ter , se nao o parametro nao e visto como tupla 

            conn.commit()
            conn.close()
            
    except ConnectionError:
        print("Erro ao se conectar ao banco de dados. ")
                
    except sqlite3.OperationalError: 
        print("Algum erro ocorreu...")
        print("-" * 30)


def listar_tudo_sobre_livro():
    try:
        conn = sqlite3.connect("BIBLIOTECA_ONLINE.db")
        cursor = conn.cursor()
        
        print("Listando todos os Livros cadastrados ate o momento:  ")
        print("-" * 30)
                    
        cursor.execute("""
        
            SELECT Livros.TITULO AS Livro, Autor.NOME_AUTOR AS Autor, CATEGORIA.NOME_CATEGORIA AS Categoria, Editora.NOME_EDITORA AS Editora, Livros.PAIS_PUBLICACAO AS Pais_Publicacao
            FROM Livros
            JOIN Livros ON Livros.id_autor = Autor.ID_AUTOR
            JOIN Livros ON Livros.id_editora = Editora.ID_EDITORA
            JOIN Livros ON Livros.id_categoria = CATEGORIA.ID_CATEGORIA;                                  
                       
                    """)     

        livros_info_total = cursor.fetchall()
        print(livros_info_total)        
        print("-" * 30)
            
        conn.commit()
        conn.close()        
        
        
    except ConnectionError:
        print("Erro ao se conectar ao banco de dados. ")
    
    except sqlite3.OperationalError as e: 
        print("Um erro ocorreu", e)
        print("-" * 30)    
    
    


def listar_todos_autor():

    try:
        conn = sqlite3.connect("BIBLIOTECA_ONLINE.db")
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
        


def listar_todos_livros():

    try:
        conn = sqlite3.connect("BIBLIOTECA_ONLINE.db")
        cursor = conn.cursor()
        
        print("Listando todos os Autores cadastrados ate o momento:  ")
        print("-" * 30)
                    
        cursor.execute("SELECT * FROM Livros;")     # TALVEZ SELECT NOME_AUTOR

        livros = cursor.fetchall()
        print(livros)        
        print("-" * 30)
            
        conn.commit()
        conn.close()        
        
        
    except ConnectionError:
        print("Erro ao se conectar ao banco de dados. ")
    
    except sqlite3.OperationalError: 
        print("Vazio.")
        print("-" * 30)
        
        


def listar_todas_categorias():

    try:
        conn = sqlite3.connect("BIBLIOTECA_ONLINE.db")
        cursor = conn.cursor()
        
        print("Listando todos os Autores cadastrados ate o momento:  ")
        print("-" * 30)
                    
        cursor.execute("SELECT * FROM Categoria;")     

        categoria = cursor.fetchall()
        print(categoria)        
        print("-" * 30)
            
        conn.commit()
        conn.close()        
        
        
    except ConnectionError:
        print("Erro ao se conectar ao banco de dados. ")
    
    except sqlite3.OperationalError: 
        print("Vazio.")
        print("-" * 30)
        
        
        
        
def listar_todas_editoras():

    try:
        conn = sqlite3.connect("BIBLIOTECA_ONLINE.db")
        cursor = conn.cursor()
        
        print("Listando todas as editoras cadastrados ate o momento:  ")
        print("-" * 30)
                    
        cursor.execute("SELECT * FROM Editora;")     # TALVEZ SELECT NOME_AUTOR

        editoras = cursor.fetchall()
        print(editoras)        
        print("-" * 30)
            
        conn.commit()
        conn.close()        
        
        
    except ConnectionError:
        print("Erro ao se conectar ao banco de dados. ")
    
    except sqlite3.OperationalError: 
        print("Vazio.")
        print("-" * 30)
        




        

def menu():
    
    while True:
    
        print(" [1] Cadastrar Autor\n [2] Cadastrar Livro\n [3] Cadastrar Categoria\n [4] Cadastrar Editora\n [5] Listar Autores\n [6] Listar Livros\n [7] Listar Categoria\n [8] Listar Editora\n [9] Listar Todas informacoes sobre livro\n [10] Sair")
        print("-" * 30)
        escolha_usuario = input("Escolha:  ")
        
        match(escolha_usuario):
            
            case '1':
                cadastrar_autor()
                
            case '2':
                cadastrar_livro()
                
            case '3':
                cadastrar_categoria()
                                
            case '4':
                cadastrar_editora()

            case '5':
                listar_todos_livros()
            
            case '6':
                listar_todos_autor() 
        
            case '7':
                listar_todas_categorias()

            case '8':
                listar_todas_editoras()    
        
            
            case '9':
                listar_tudo_sobre_livro()
            
                        
            case '10':
                break
                    
            case _:
                print("Escolha inválida")
                
                
menu()