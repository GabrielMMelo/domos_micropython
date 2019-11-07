{% args settings %}
<html>
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    </head>
    <body>
        <div>
            <center>
                <h1>Login realizado com sucesso! Seu dispositivo está pronto para uso.</h1>
                <h3>Configure o seletor para a posição 'Ativo' e reinicie o sistema</h3>
                <h3>Ou <a href="/">configure novamente</a> caso alguma informação esteja incorreta</h3>
                <h4>Seus dados:</h4>
                <table>
                    <tr>
                        <th>SSID</th> 
                        <td><center>{{ settings["SSID"] }}</center></th> 
                    </tr>
                    <tr>
                        <th>Senha SSID</th> 
                        <td><center>******</center></th> 
                    </tr>
                    <tr>
                        <th>Host</th> 
                        <td><center>{{ settings["HOST"] }}</center></th> 
                    </tr>
                    <tr>
                        <th>Endereço de e-mail</th> 
                        <td><center>{{ settings["EMAIL"] }}</center></th> 
                    </tr>
                    <tr>
                        <th>Senha</th> 
                        <td><center>******</center></th> 
                    </tr>
                </table>
            </center>
        </div>
    </body>
</html>
