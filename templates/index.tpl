{% args settings %}
<html lang="pt">
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
        <title>Tela de Cadastro</title>
    </head>
    <body>
        <div>
            <form action="/login" method="post" tabindex="1">
                <input type="text" value="{{ settings.get("SSID", '') }}" name="ssid" placeholder="SSID" required />
                <input type="password" value="{{ settings.get("SSID_PASSWORD", '') }}" name="password" placeholder="Senha" required />
                <button type="submit">Salvar</button>
            </form>
        </div>
    </body>
</html>
