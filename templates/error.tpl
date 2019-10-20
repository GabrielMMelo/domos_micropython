{% args error %}
<html>
    <head>
        <style rel="stylesheet" type="text/css">
            body{
                background-color: #5382e8;
                font-family: "Trebuchet MS", Arial, Helvetica, sans-serif;
            }
            .container {
                width: 50%;
                margin: 0 auto;
                margin-top: 100px!important;
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
                color: #001d68;
                font-weight: bold;
                font-size: 22px;
            }

            .progressBar li.active:before {
                border-color: #001d68;
                background-color: #001d68;
            }

            .progressBar .active:after {
                background-color: #001d68;
            } 

            .progressBar li.error {
                color: #FF4242;
                font-weight: bold;
                font-size: 22px;
            }

            .progressBar li.error:before {
                border-color: #FF4242;
                background-color: #FF4242;
            }

            .progressBar .error:after {
                background-color: #FF4242;
            } 
        </style>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    </head>
    <body>
        <div class="container" style="color: white;">
            <center>
                <h1 style="color: white;">Erro ao configurar {{error}}.</h1>
                <h3 style="color: white;">Verifique os dados inseridos e  <a href="/">configure novamente</a></h3>
            </center>
        </div>
        <div class="row">
            <div class="col-xs-12 col-md-8 offset-md-2 block border">
                <div class="wrapper-progressBar">
                    <ul class="progressBar">
                        {% if error == "rede" %}
                            <li class="error">Configurando a rede</li>
                            <li>Configurando login</li>
                            <li>Sistema configurado!</li>
                        {% else %}
                            <li class="active">Configurando a rede</li>
                            <li class="error">Configurando login</li>
                            <li>Sistema configurado!</li>
                        {% endif %}

                    </ul>
                </div>
            </div>
        </div>
    </body>
</html>
