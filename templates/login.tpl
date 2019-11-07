{% args req %}
<html lang="pt">
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
        <title>Tela de Cadastro</title>
    </head>
    <body>
        <div>
            <form action="/finish" method="post" tabindex="1">
                <input type="text" name="host" value="domos.icu" placeholder="Host (e.g., 'domos.icu')" required />
                <input type="email" name="email" placeholder="E-mail" required />
                <input type="password" name="password" placeholder="Senha" required />
                <button type="submit">Enviar</button>
            </form>
        </div>
    </body>
</html>
