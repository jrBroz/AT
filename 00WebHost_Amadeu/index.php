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
                
                <form action="pesquisa.php" method="post" class="mt-3">
                    <div class="form-row justify-content-center">
                        <div class="col-auto">
                            <input name="frase" type="text" id="frase" class="form-control" placeholder="Digite sua pesquisa" required>
                        </div>
                        <div class="col-auto">
                            <input name="submit" type="submit" value="Pesquisar" class="btn btn-primary">
                        </div>
                        <div class="col-auto">
                            <a href="inserir.php" class="btn btn-secondary">Cadastrar Novo Verbete</a>
                        </div>
                    </div>
                </form>
            </div>
        </div>
    </body>
</html>
