import sqlite3

def cadastrar_aluno():
    nome_aluno = input("Insira o Nome do aluno: ")

    try:    
        conn = sqlite3.connect("Escola.db")
        cursor = conn.cursor()
                 
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Alunos(
                ID_ALUNOS INTEGER PRIMARY KEY AUTOINCREMENT,
                NOME_ALUNO VARCHAR(100)
            );
        """)
            
        cursor.execute("INSERT INTO Alunos(NOME_ALUNO) VALUES (?);", (nome_aluno,))
        conn.commit()
        conn.close()
    
    except sqlite3.Error as e:
        print("Erro ao cadastrar aluno:", e)
        print("-" * 30)

def cadastrar_em_disciplina_aluno():
    id_aluno = input("Insira id do aluno: ")
    id_disciplina = input("Insira um id de disciplina: ")

    try:    
        conn = sqlite3.connect("Escola.db")
        cursor = conn.cursor()
                 
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Alunos_Matriculados(
                ID_ALUNOS_MATRICULADOS INTEGER PRIMARY KEY AUTOINCREMENT,
                id_aluno INTEGER,
                id_disciplina INTEGER,
                FOREIGN KEY(id_disciplina) REFERENCES Disciplinas(ID_DISCIPLINA),
                FOREIGN KEY(id_aluno) REFERENCES Alunos(ID_ALUNO)
            );
        """)
            
        cursor.execute("INSERT INTO Alunos_Matriculados(id_aluno, id_disciplina) VALUES (?,?);", (id_aluno, id_disciplina))
        conn.commit()
        conn.close()
    
    except sqlite3.Error as e:
        print("Erro ao cadastrar aluno em disciplina:", e)
        print("-" * 30)

def listar_alunos_matriculados_em_disciplinas():
    try:
        conn = sqlite3.connect("Escola.db")
        cursor = conn.cursor()
    
        materia_para_ver = input("De qual Matéria, deseja ver os alunos cadastrados? ")
        cursor.execute("""
            SELECT Alunos.NOME_ALUNO AS Nome_do_Aluno, Disciplinas.NOME_DISCIPLINA AS Nome_da_Disciplina
            FROM Alunos
            JOIN Alunos_Matriculados ON Alunos.ID_ALUNOS = Alunos_Matriculados.id_aluno
            JOIN Disciplinas ON Disciplinas.ID_DISCIPLINA = Alunos_Matriculados.id_disciplina
            WHERE Disciplinas.NOME_DISCIPLINA = ?;
        """, (materia_para_ver,))

        tudo = cursor.fetchall()
        print(tudo)
        print("-" * 30)
        conn.commit()
        conn.close()
        
    except sqlite3.Error as e:
        print("Erro ao listar alunos matriculados:", e)
        print("-" * 30)

def listar_todos_alunos():
    try:
        conn = sqlite3.connect("Escola.db")
        cursor = conn.cursor()
        
        print("Listando todos os alunos cadastrados até o momento:")
        print("-" * 30)
                    
        cursor.execute("SELECT * FROM Alunos;")
        alunos = cursor.fetchall()
        print(alunos)
        print("-" * 30)
        conn.commit()
        conn.close()
        
    except sqlite3.Error as e:
        print("Erro ao listar todos os alunos:", e)
        print("-" * 30)

def listar_todas_disciplinas():
    try:
        conn = sqlite3.connect("Escola.db")
        cursor = conn.cursor()
        
        print("Listando todas as disciplinas cadastradas até o momento:")
        print("-" * 30)
                    
        cursor.execute("SELECT * FROM Disciplinas;")
        disciplinas = cursor.fetchall()
        print(disciplinas)
        print("-" * 30)
        conn.commit()
        conn.close()
        
    except sqlite3.Error as e:
        print("Erro ao listar todas as disciplinas:", e)
        print("-" * 30)

def cadastrar_disciplina():
    nome_disciplina = input("Insira o Nome da disciplina: ")

    try:    
        conn = sqlite3.connect("Escola.db")
        cursor = conn.cursor()
                 
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Disciplinas(
                ID_DISCIPLINA INTEGER PRIMARY KEY AUTOINCREMENT,
                NOME_DISCIPLINA VARCHAR(100)
            );
        """)
            
        cursor.execute("INSERT INTO Disciplinas(NOME_DISCIPLINA) VALUES (?);", (nome_disciplina,))
        conn.commit()
        conn.close()
    
    except sqlite3.Error as e:
        print("Erro ao cadastrar disciplina:", e)
        print("-" * 30)

def listar_disciplinas_de_aluno():
    id_aluno = input("Insira o ID do aluno para listar as disciplinas: ")

    try:
        conn = sqlite3.connect("Escola.db")
        cursor = conn.cursor()

        cursor.execute("""
            SELECT Disciplinas.NOME_DISCIPLINA AS Nome_da_Disciplina
            FROM Alunos
            JOIN Alunos_Matriculados ON Alunos.ID_ALUNOS = Alunos_Matriculados.id_aluno
            JOIN Disciplinas ON Disciplinas.ID_DISCIPLINA = Alunos_Matriculados.id_disciplina
            WHERE Alunos.ID_ALUNOS = ?;
        """, (id_aluno,))

        disciplinas = cursor.fetchall()
        if disciplinas:
            print(f"Disciplinas do aluno ID {id_aluno}:")
            for disciplina in disciplinas:
                print(disciplina[0])
            print("-" * 30)
        else:
            print(f"Aluno ID {id_aluno} não está matriculado em nenhuma disciplina.")
            print("-" * 30)

        conn.close()

    except sqlite3.Error as e:
        print("Erro ao listar disciplinas do aluno:", e)
        print("-" * 30)

def menu():
    while True:
        print(" [1] Cadastrar Aluno\n [2] Cadastrar Disciplina\n [3] Listar Todos Alunos\n [4] Listar Todas Disciplinas\n [5] Matricular Aluno em disciplina\n [6] Listar alunos matriculados em disciplinas\n [7] Listar disciplinas de um aluno\n [8] Sair")
        print("-" * 30)
        escolha_usuario = input("Escolha: ")

        match(escolha_usuario):
            case '1':
                cadastrar_aluno()
            case '2':
                cadastrar_disciplina()
            case '3':
                listar_todos_alunos()
            case '4':
                listar_todas_disciplinas()
            case '5':
                cadastrar_em_disciplina_aluno()
            case '6':
                listar_alunos_matriculados_em_disciplinas()
            case '7':
                listar_disciplinas_de_aluno()
            case '8':
                break
            case _:
                print("Escolha inválida")

menu()
