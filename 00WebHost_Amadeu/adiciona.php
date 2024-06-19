<?php
if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    // Obter os dados do formulário
    $nome = $_POST['Nome_Livro'];
    $Resenha = $_POST['Resenha'];
    $Escritor = $_POST['Escritor'];
    $Email = $_POST['Email'];
    $Capa_Livro = $_POST['Capa_Livro']; // novo campo para o link da imagem

    // Conectar ao banco de dados usando mysqli
    $conexao = mysqli_connect('localhost', 'id22328890_rafael', 'Chave13!');
    mysqli_select_db($conexao, 'id22328890_banco123');
    
    // Verificar conexão
    if ($conexao->connect_error) {
        die('Erro de conexão: ' . $conexao->connect_error);
    }

    // Preparar a consulta
    $consulta = $conexao->prepare('INSERT INTO registros (Nome, Resenha, Escritor, Email,Capa_Livro) VALUES (?, ?, ?, ?, ?)');
    $consulta->bind_param('sssss', $nome, $Resenha, $Escritor, $Email, $Capa_Livro);

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
