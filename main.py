# coding=utf8

# from layout import layout
from Components.insert_data import insert_file, insert_text
from Components.search_data import search

# layout()

entry, entries = 0, [1, 2]
while entry not in entries:
    entry = int(
        input(
            'Escolha a ação a ser realizada:\n'
            '\t1 - Carregar lista de nomes\n'
            '\t2 - Buscar nome em lista\n'
        )
    )
    if entry not in entries:
        print('Opção inválida!\n')
if entry not in entries:
    print('Opção inválida!\n')
elif entry == 1:
    entry = 0
    while entry not in entries:
        entry = int(
            input(
                'Escolha a forma para inserir os dados:\n'
                '\t1 - Carregar Arquivo de Texto Simples\n'
                '\t2 - Inserir Dados da Área de Transferência\n'
            )
        )
        if entry not in entries:
            print('Opção inválida!\n')
    if entry == 1:
        insert = insert_file(names=input(str('Insira o caminho do arquivo de Texto:\n\t')))
        if insert:
            pass
    elif entry == 2:
        insert = insert_text(names=input(str('Insira a lista de nomes:\n\t')))
search(name='')
