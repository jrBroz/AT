<!DOCTYPE html>
<html>
<head>
    <!-- Incluindo o CSS do Bootstrap -->
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
    <style>
        html, body {
            height: 100%;
            margin: 0;
        }
        .center-container {
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100%;
        }
        .responsive-img {
            width: 50%; /* Ajuste a largura conforme necessário */
            height: auto; /* Mantém a proporção */
        }
    </style>
</head>
<body>
    <div class="container center-container">
        <div class="text-center">
            <img src="Logo.jfif" class="responsive-img" alt="Logo">
            <?php

            ini_set('display_errors', 'Off');
            error_reporting(E_ALL & ~E_NOTICE & ~E_WARNING);
            if ($_SERVER['REQUEST_METHOD'] == 'POST') {
                // Obter a Verbete do formulário
                $Nome_Livro = $_POST['Nome_Livro'];

                // Conectar ao banco de dados usando mysqli
                $conexao = mysqli_connect('localhost', 'id22328890_rafael', 'Chave13!');
                mysqli_select_db($conexao, 'id22328890_banco123');
                // Verificar conexão
                if ($conexao->connect_error) {
                    die('Erro de conexão: ' . $conexao->connect_error);
                }

                // Preparar a consulta
                $consulta = $conexao->prepare('SELECT * FROM registros WHERE Nome LIKE ?');
                $param = '%' . $Nome_Livro . '%';
                $consulta->bind_param('s', $param);

                // Executar a consulta
                $consulta->execute();
                $resultado = $consulta->get_result();

                // Verificar se o registro foi encontrado
                if ($resultado->num_rows > 0) {
                    echo '<table class="table mt-3">';
                    while ($campo = $resultado->fetch_array(MYSQLI_NUM)) {
                        echo '<tr><td><strong>Nome:</strong></td><td>' . htmlspecialchars($campo[0]) . '</td></tr>';
                        echo '<tr><td><strong>Resenha:</strong></td><td>' . htmlspecialchars($campo[1]) . '</td></tr>';
                        echo '<tr><td><strong>Escritor:</strong></td><td>' . htmlspecialchars($campo[2]) . '</td></tr>';
                        echo '<tr><td><strong>Email:</strong></td><td>' . htmlspecialchars($campo[3]) . '</td></tr>';
                        // Adicionar a coluna para exibir a imagem
                        echo '<tr><td><strong>Capa_Livro:</strong></td><td><img src="' . htmlspecialchars($campo[4]) . '" class="responsive-img"></td></tr>';
                    }
                    echo '</table>';
                } else {
                    echo '<div class="alert alert-warning mt-3">Registro não encontrado</div>';
                }

                // Fechar a conexão
                $conexao->close();
            }
            ?>

            <!-- Formulário para pesquisa -->
            <form action="" method="post" class="mt-3">
                <div class="form-group">
                    <input name="Nome_Livro" type="text" class="form-control" placeholder="Digite livro  para pesquisar a resenha" required>
                </div>
                <input name="submit" type="submit" value="Pesquisar" class="btn btn-primary">
            </form>

            <!-- Botão "Inserir" -->
            <form action="inserir.php" method="post" class="mt-3">
                <input name="submit" type="submit" value="Inserir" class="btn btn-secondary">
            </form>

            <!-- Botão "Voltar" -->
            <a href="index.php" class="btn btn-secondary mt-3">Voltar</a>
        </div>
    </div>
</body>
</html>
