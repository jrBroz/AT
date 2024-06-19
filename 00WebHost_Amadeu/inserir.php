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

            <form action="adiciona.php" method="post" class="mt-3">
                <div class="form-group row">
                    <label for="Nome_Livro" class="col-sm-2 col-form-label"><strong>Nome Livro:</strong></label>
                    <div class="col-sm-10">
                        <input name="Nome_Livro" type="text" id="Nome_Livro" class="form-control" size="60" required>
                    </div>
                </div>
                <div class="form-group row">
                    <label for="descricao" class="col-sm-2 col-form-label"><strong>Resenha:</strong></label>
                    <div class="col-sm-10">
                        <input name="Resenha" type="text" id="Resenha" class="form-control" size="100" required>
                    </div>
                </div>
                <div class="form-group row">
                    <label for="Escritor" class="col-sm-2 col-form-label"><strong>Escritor:</strong></label>
                    <div class="col-sm-10">
                        <input name="Escritor" type="text" id="Escritor" class="form-control" size="30" required>
                    </div>
                </div>
                <div class="form-group row">
                    <label for="Email" class="col-sm-2 col-form-label"><strong>Email:</strong></label>
                    <div class="col-sm-10">
                        <input name="Email" type="email" id="Email" class="form-control" size="30" required>
                    </div>
                </div>
                <div class="form-group row">
                    <label for="Capa_Livro" class="col-sm-2 col-form-label"><strong>Link Capa do Livro</strong></label>
                    <div class="col-sm-10">
                        <input name="Capa_Livro" type="url" id="Capa_Livro" class="form-control" size="100" required>
                    </div> 
                </div>
                <div class="form-group row">
                    <div class="col-sm-10 offset-sm-2">
                        <input name="submit" type="submit" value="Inserir" class="btn btn-primary">
                    </div>
                </div>
            </form>
        </div>
    </div>
</body>
</html>
