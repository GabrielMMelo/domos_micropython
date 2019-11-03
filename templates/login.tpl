{% args req %}
<html lang="pt">
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

            .form-contact {
                width: 100%;
            }

            .form-contact-input {
                width: 100%;
                color: #292929;
                font-size: 18px;
                background-color: #E9E9E9;
                border: 1px solid #E9E9E9;
                -moz-border-radius: 5px;
                -webkit-border-radius: 5px;
                border-radius: 5px;
                height: 40px;
                margin-bottom: 20px;
                border-bottom: 1px solid #ccc;
                border-left: 1px solid #ccc;
                text-indent: 20px;
            }

            .form-button {
                width: 100%;
                font-size: 18px;
                border-radius: 4px;
                color: #fff;
                height: 40px;
                opacity: .8;
                margin-bottom: 20px;
                cursor: pointer;
                background: #3f696b;
                display: block;
                border: none;
                border-bottom: 1px solid #500707;
                border-right: 1px solid #500707;
                transition: 1s;
            }

            .form-button:hover {
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
        <title>Tela de Cadastro</title>
    </head>
    <body>
        <div class="container">
            <form action="/finish" class="form-contact" method="post" tabindex="1">
                <input type="text" class="form-contact-input" name="host" value="domos.icu" placeholder="Host (e.g., 'www.domopen.net:8081')" required />
                <input type="email" class="form-contact-input" name="email" placeholder="E-mail" required />
                <input type="password" class="form-contact-input" name="password" placeholder="Senha" required />
                <button type="submit" class="form-button">Enviar</button>
            </form>
        </div>
        <div class="row">
            <div class="col-xs-12 col-md-8 offset-md-2 block border">
                <div class="wrapper-progressBar">
                    <ul class="progressBar">
                        <li class="active">Configurando a rede</li>
                        <li class="active">Configurando login</li>
                        <li>Sistema configurado!</li>
                    </ul>
                </div>
            </div>
        </div>
    </body>
</html>
