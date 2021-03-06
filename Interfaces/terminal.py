# coding=utf8

from Components.insert_data import insert_file, insert_text
from Components.search_data import search_name
from unidecode import unidecode


def terminal():
    entry, entries = '0', ['1', '2']
    while entry not in entries:
        entry = str(
            input(
                'Escolha a ação a ser realizada:\n'
                '\t1 - Carregar lista de nomes\n'
                '\t2 - Buscar nome em lista\n\t'
            )
        )
        if entry not in entries:
            print('Opção inválida!\n')
    if entry == '1':
        entry = '0'
        while entry not in entries:
            entry = str(
                input(
                    'Escolha a forma para inserir os dados:\n'
                    '\t1 - Carregar Arquivo de Texto Simples\n'
                    '\t2 - Inserir Dados da Área de Transferência\n\t'
                )
            )
            if entry not in entries:
                print('Opção inválida!\n')
        if entry == '1':
            insert = insert_file(names=input(str('Insira o caminho do arquivo de Texto:\n\t')))
            if insert:
                pass
        elif entry == '2':
            insert = insert_text(names=input(str('Insira a lista de nomes:\n\t')))
            if insert:
                pass
    elif entry == '2':
        name = str(input('Digite o nome a pesquisar:\n\t'))
        mode = str(
            input(
                'Escolha o modo de pesquisa:\n'
                '\t1 - Busca exata ao texto digitado\n'
                '\t2 - Busca relativa\n\t'
            )
        )
        name = unidecode(name.lower()) if mode == 2 else name
        result = search_name(name=unidecode(name.lower()), mode=mode)
        print('A pesquisa por "{}" retornou {} nomes:'.format(name, len(result)))
        for i in result:
            print(i)
