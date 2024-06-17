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
                    <label for="Verbete" class="col-sm-2 col-form-label"><strong>Verbete:</strong></label>
                    <div class="col-sm-10">
                        <input name="Verbete" type="text" id="Verbete" class="form-control" size="60" required>
                    </div>
                </div>
                <div class="form-group row">
                    <label for="descricao" class="col-sm-2 col-form-label"><strong>Descrição:</strong></label>
                    <div class="col-sm-10">
                        <input name="descricao" type="text" id="descricao" class="form-control" size="100" required>
                    </div>
                </div>
                <div class="form-group row">
                    <label for="contribuicao" class="col-sm-2 col-form-label"><strong>Contribuição:</strong></label>
                    <div class="col-sm-10">
                        <input name="contribuicao" type="text" id="contribuicao" class="form-control" size="30" required>
                    </div>
                </div>
                <div class="form-group row">
                    <label for="email" class="col-sm-2 col-form-label"><strong>Email:</strong></label>
                    <div class="col-sm-10">
                        <input name="email" type="email" id="email" class="form-control" size="30" required>
                    </div>
                </div>
                <div class="form-group row">
                    <label for="imagelink" class="col-sm-2 col-form-label"><strong>Link da Imagem:</strong></label>
                    <div class="col-sm-10">
                        <input name="imagelink" type="url" id="imagelink" class="form-control" size="100" required>
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
