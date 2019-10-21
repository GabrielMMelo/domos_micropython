{% args settings %}
<html>
    <head>
        <style rel="stylesheet" type="text/css">
            body{
                background-color: cadetblue;
                font-family: "Trebuchet MS", Arial, Helvetica, sans-serif;
            }
            .container {
                width: 50%;
                margin: 0 auto;
                margin-top: 100px!important;
            }

            #data {
                border-collapse: collapse;
                width: 100%;
            }

            #data td, #data th {
                border: 1px solid #ddd;
                padding: 8px;
            }

            #data tr{background-color: #f2f2f2;}

            #data tr:hover {background-color: #ddd;}

            #data th {
                padding-top: 12px;
                padding-bottom: 12px;
                text-align: left;
                background-color: #3f696b;
                color: white;
            }

            .confirm-button {
                margin-top: 30px;
                width: 100%;
                font-size: 18px;
                border-radius: 4px;
                color: #fff;
                height: 40px;
                opacity: .8;
                margin-bottom: 20px;
                cursor: pointer;
                background: #001d68;
                display: block;
                border: none;
                border-bottom: 1px solid #500707;
                border-right: 1px solid #500707;
                transition: 1s;
            }

            .confirm-button:hover {
                opacity: 1;
            }

            .row {
                margin-top: 80px;
            }

            .wrapper-progressBar {
                width: 100%
            }

            .progressBar {
            }

            .progressBar li {
                list-style-type: none;
                float: left;
                width: 33%;
                position: relative;
                text-align: center;
                color: white;
            }

            .progressBar li:before {
                content: " ";
                line-height: 30px;
                border-radius: 50%;
                width: 30px;
                height: 30px;
                border: 1px solid #ddd;
                display: block;
                text-align: center;
                margin: 0 auto 10px;
                background-color: white
            }

            .progressBar li:after {
                content: "";
                position: absolute;
                width: 100%;
                height: 4px;
                background-color: #ddd;
                top: 15px;
                left: -50%;
                z-index: -1;
            }

            .progressBar li:first-child:after {
                content: none;
            }

            .progressBar li.active {
                color: #3f696b;
                font-weight: bold;
                font-size: 22px;
            }

            .progressBar li.active:before {
                border-color: #3f696b;
                background-color: #3f696b;
            }

            .progressBar .active:after {
                background-color: #3f696b;
            } 
        </style>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    </head>
    <body>
        <div class="container" style="color: white;">
            <center>
                <h1 style="color: white;">Login realizado com sucesso! Seu dispositivo está pronto para uso.</h1>
                <h3 style="color: white;">Configure o seletor para a posição 'Ativo' e reinicie o sistema</h3>
                <h3 style="color: white;">Ou <a href="/">configure novamente</a> caso alguma informação esteja incorreta</h3>
                <h4 style="color: white;">Seus dados:</h4>
                <table id="data">
                    <tr>
                        <th>SSID</th> 
                        <td><center>{{ settings["SSID"] }}</center></th> 
                    </tr>
                    <tr>
                        <th>Senha</th> 
                        <td><center>******</center></th> 
                    </tr>
                    <tr>
                        <th>Host</th> 
                        <td><center>{{ settings["HOST"] }}</center></th> 
                    </tr>
                    <tr>
                        <th>Nome de usuário</th> 
                        <td><center>{{ settings["USERNAME"] }}</center></th> 
                    </tr>
                    <tr>
                        <th>Senha</th> 
                        <td><center>******</center></th> 
                    </tr>
                </table>
            </center>
        </div>
        <div class="row">
            <div class="col-xs-12 col-md-8 offset-md-2 block border">
                <div class="wrapper-progressBar">
                    <ul class="progressBar">
                        <li class="active">Configurando a rede</li>
                        <li class="active">Configurando login</li>
                        <li class="active">Sistema configurado!</li>
                    </ul>
                </div>
            </div>
        </div>
    </body>
</html>
