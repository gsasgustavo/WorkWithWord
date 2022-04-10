# Work(ing) With Word(s)

![Desenvolvimento](http://img.shields.io/static/v1?label=Status&message=Em%20Desenvolvimento&color=GREEN&style=flat-square)
![Python](http://img.shields.io/static/v1?label=Python&message=v3.9&color=blue&style=flat-square&logo=PYTHON)
![PIP](http://img.shields.io/static/v1?label=PIP&message=v20.3.4&color=blue&style=flat-square&logo=PYTHON)
![PySimpleGUI](http://img.shields.io/static/v1?label=PySimpleGUI&message=v4.59.0&color=blue&style=flat-square&logo=PYTHON)

## Tópicos:

* [Descrição do Projeto](#descrio-do-projeto)
* [Funcionalidades](#funcionalidades)
* [Tecnologias Utilizadas](#tecnologias-utilizadas)
* [Dependências](#dependncias)
* [Modos de Execução](#modos-de-execuo)
* [Fluxograma](#fluxograma)

## Descrição do Projeto:

Sistema criado com o intuito de **inserir** e **buscar** nomes de pessoas em grande escala. No decurso da execução do
sistema, é permitido ao usuário realizar ações que permeiam entre inserção e busca de nomes de pessoas.

No que tange a inserção dos nomes, a mesma pode ser realizada com o carregamento (upload) de arquivos de texto simples, 
tais como *\*.txt*, *\*.csv*, ou por inserção de texto, seja digitação ou colagem. Em ambos os casos, os nomes são 
delimitados por linhas e, ao confirmar esse envio de dados, um novo arquivo `/Assets/names.txt` é gerado.

Para a realização de busca/pesquisa de nomes, o usuário pode digitar nomes completos ou apenas algumas letras e optar 
pelas buscas relativa ou exata. A busca relativa fará com que o sistema aplique uma coersão para que o texto digitado e 
os dados salvos sejam lidos como *unicode* e *case-insensitive*. Na busca exata, o sistema procurará o texto confome 
informado pelo usuário. Em qualquer modo de busca, o sistema lerá o arquivo de texto `/Assets/names.txt` e retornará 
todas as ocorrências da pesquisa, caso haja.

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
- [Package Installer for Python](https://pip.pypa.io/en/stable/getting-started/)

## Dependências:

> A Instalação da Linguagem Python e o Pacote de Instalação (PIP) pode ser apreciada nos links dispostos em [Tecnologias Utilizadas](#tecnologias-utilizadas).

Para a criação da Interface Gráfica foi utilizada a Biblioteca [PySimple GUI](https://pysimplegui.readthedocs.io/):

`pip install PySimpleGUI`

A Biblioteca Unidecode foi utilizada para a remoção de caracteres especiais:

`pip install Unidecode`

Para analisar o consumo de Hardware utilizou-se a biblioteca PSUtil:

`pip install psutil`

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
start(( )) --> A{ }
A --Inserir Dados--> B{ }
A --Iniciar Busca--> C(Digitar Texto)
B --> A
B --Carregar Arquivo--> D[Dados inseridos]
B --Inserir Texto--> D
D --> finish
C --> A
C --com resultados--> E[Ver Resultados]
C --sem resultados--> C
E --> C
E --> F[Analisar]
E --> finish(( ))
F --> E
F --> finish(( ))
~~~
