# Work(ing) With Word(s)

![Desenvolvimento](http://img.shields.io/static/v1?label=Status&message=Em%20Desenvolvimento&color=GREEN&style=flat-square)
![Python](http://img.shields.io/static/v1?label=Python&message=v3.9&color=blue&style=flat-square&logo=PYTHON)
![PIP](http://img.shields.io/static/v1?label=PIP&message=v20.3.4&color=blue&style=flat-square&logo=PYTHON)
![PySimpleGUI](http://img.shields.io/static/v1?label=PySimpleGUI&message=v4.59.0&color=blue&style=flat-square&logo=PYTHON)

## Tópicos:

* [Descrição do Projeto](#descrição-do-projeto)
* [Funcionalidades](#funcionalidades)
* [Tecnologias Utilizadas](#tecnologias-utilizadas)

## Descrição do Projeto:

Sistema criado com o intuito de **inserir** e **buscar** nomes de pessoas em grande escala.

## Funcionalidades:

- Carregar arquivo com nomes de pessoas;
- Digitar (Inserir) texto com nomes de pessoas;
- Ler dados inseridos (arquivo ou texto);
- Salvar dados lidos em novo arquivo de texto simples (*.txt);
- Buscar registros a partir de texto digitado;
- Listar resultados da pesquisa;

## Tecnologias Utilizadas:

- [IDE JetBrains PyCharm CE](https://www.jetbrains.com/pycharm/)
- [Python Language](https://www.python.org/)
- [PySimple GUI](https://pysimplegui.readthedocs.io/)

## Modos de Execução:

> Além da Interface Gráfica, há como utilizar a aplicação através do terminal, conforme trecho subsequente do arquivo *main.py*:
~~~python
gui = True
if gui:
    layout()  # Inicia a aplicação com os recursos da Biblioteca PySimpleGUI.
else:
    terminal()  # Inicia a aplicação através do Terminal do SO.
~~~

## Fluxograma:

~~~mermaid
graph LR
start(( )) --> A{{escolher acao}}
A --Inserir Dados--> B{{modo de insercao}}
A --Iniciar Busca--> G(Digitar Texto)
B --Voltar--> A
B --Inserir--> D(Carregar Arquivo)
B --Inserir--> E(Digitar/Colar Texto)
D --Voltar--> B
D --> F[Dados inseridos]
E --Voltar--> B
E --> F
F --Voltar--> A
F --> finish(( ))
G --Voltar--> A
G --Buscar--> H{ }
H --com resultados--> I[Ver Resultados]
H --sem resultados--> G
I --voltar--> G
I --> finish(( ))
~~~