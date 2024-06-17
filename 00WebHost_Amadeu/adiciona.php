<?php
if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    // Obter os dados do formulário
    $verbete = $_POST['Verbete'];
    $descricao = $_POST['descricao'];
    $contribuicao = $_POST['contribuicao'];
    $email = $_POST['email'];
    $imagelink = $_POST['imagelink']; // novo campo para o link da imagem

    // Conectar ao banco de dados usando mysqli
    $conexao = mysqli_connect('localhost', 'id22328890_rafael', 'Chave13!');
    mysqli_select_db($conexao, 'id22328890_banco123');
    
    // Verificar conexão
    if ($conexao->connect_error) {
        die('Erro de conexão: ' . $conexao->connect_error);
    }

    // Preparar a consulta
    $consulta = $conexao->prepare('INSERT INTO registros (Verbete, Significado, Contribuicao, Email, Imagelink) VALUES (?, ?, ?, ?, ?)');
    $consulta->bind_param('sssss', $verbete, $descricao, $contribuicao, $email, $imagelink);

    // Executar a consulta
    if ($consulta->execute()) {
        echo "<meta HTTP-EQUIV='Refresh' CONTENT='0;URL=index.php'>";
    } else {
        echo 'Houve um erro ao tentar inserir o registro: ' . $consulta->error;
    }

    // Fechar a conexão
    $conexao->close();
}
?>
