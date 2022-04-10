# coding=utf8

from datetime import datetime

from Components.insert_data import insert_file, insert_text
from Components.search_data import search_name
from PySimpleGUI import PySimpleGUI as Interface
from unidecode import unidecode
from psutil import Process
from os import getpid, path


def window_components():
    Interface.theme(new_theme='DarkGrey10')
    elements = [
        [Interface.Text(text='Escolher ação:')],
        [
            Interface.Button(button_text='Inserir Dados', size=(26, 3)),
            Interface.Button(
                button_text='Iniciar Busca',
                size=(26, 3),
                disabled=path.exists(path=r'../Assets/names.txt')
            )
        ]
    ]
    return Interface.Window(
        title='Componentes',
        layout=elements,
        finalize=True,
        location=(500, 500),
        size=(450, 100)
    )


def window_insert():
    Interface.theme(new_theme='DarkGrey10')
    elements = [
        [Interface.Text('Inserir Dados:')],
        [Interface.Radio(text='Carregar Arquivo', group_id='dados', key='file_upload', default=True)],
        [
            Interface.Input(size=(52, 0), key='filepath'),
            Interface.FileBrowse(button_text='...')
        ],
        [Interface.Radio(text='Digitar/Colar Texto', group_id='dados', key='clipboard', default=True)],
        [Interface.Multiline(size=(60, 0), expand_y=True, key='listtext', no_scrollbar=True)],
        [
            Interface.Button(button_text='Inserir', size=(26, 3)),
            Interface.Button(button_text='Voltar', size=(26, 3))
        ]
    ]
    return Interface.Window(
        title='Inserir Dados',
        layout=elements,
        finalize=True,
        location=(500, 500),
        size=(450, 300)
    )


def window_search():
    Interface.theme(new_theme='DarkGrey10')
    elements = [
        [Interface.Text(text='Digitar texto:')],
        [Interface.Input(size=(60, None), expand_y=True, key='text')],
        [
            Interface.Text(text='Modo de Busca:'),
            Interface.Radio(text='Busca Exata', group_id='modo', key='exact', default=True),
            Interface.Radio(text='Busca Relativa', group_id='modo', key='relative', default=True)
        ], [
            Interface.Button(button_text='Buscar', size=(26, 3)),
            Interface.Button(button_text='Voltar', size=(26, 3))
        ]
    ]
    return Interface.Window(
        title='Iniciar Busca',
        layout=elements,
        finalize=True,
        location=(500, 500),
        size=(450, 160)
    )


def window_result(results):
    Interface.theme(new_theme='DarkGrey10')
    elements = [
        [Interface.Text(text='A busca retornou {} ocorrências:'.format(len(results)))],
        [Interface.Listbox(values=results, size=(60, 12))],
        [
            Interface.Button(button_text='Voltar', size=(26, 3)),
            Interface.Button(button_text='Analisar', size=(26, 3))
        ]
    ]
    return Interface.Window(
        title='Resultados',
        layout=elements,
        finalize=True,
        location=(500, 500),
        size=(450, 280)
    )


def window_analysis(time, process):
    Interface.theme(new_theme='DarkGrey10')
    elements = [
        [Interface.Text(text='Análise da Busca:\n')],
        [Interface.Text(text='Tempo de execução: ' + str(time) + 'ms')],
        [Interface.Text(text='Consumo de CPU: ' + str(process.cpu_times()[0]) + 's')],
        [Interface.Text(text='Consumo de RAM: ' + str(process.memory_info()[0] / 8000000000) + 'B')],
        [Interface.Button(button_text='Voltar', size=(26, 3))]
    ]
    return Interface.Window(
        title='Resultados',
        layout=elements,
        finalize=True,
        location=(500, 500),
        size=(450, 180)
    )


def layout():
    component, insert, search, result, analysis = window_components(), None, None, None, None
    execution_time = process = None
    while True:
        window, event, values = Interface.read_all_windows()
        if window == component:
            if event == Interface.WIN_CLOSED:
                break
            elif event == 'Inserir Dados':
                component.hide()
                insert = window_insert()
            elif event == 'Iniciar Busca':
                component.hide()
                search = window_search()
        if window == insert:
            if event == Interface.WIN_CLOSED:
                break
            elif event == 'Inserir':
                back = False
                if values['file_upload'] and not values['clipboard']:
                    back = insert_file(names=values['filepath'])
                elif values['clipboard'] and not values['file_upload']:
                    back = insert_text(names=values['listtext'])
                if back:
                    Interface.popup(
                        'Dados arquivados!',
                        title='Notificação',
                        location=(500, 500)
                    )
            elif event == 'Voltar':
                insert.hide()
                component.un_hide()
        if window == search:
            if event == Interface.WIN_CLOSED:
                break
            elif event == 'Buscar':
                start_time = datetime.now()
                process = Process(getpid())
                results = list()
                if values['text']:
                    if values['relative'] and not values['exact']:
                        results = search_name(name=unidecode(values['text'].lower()), mode=2)
                    elif values['exact'] and not values['relative']:
                        results = search_name(name=values['text'], mode=1)
                    if not len(results):
                        Interface.popup(
                            'Nenhuma informação encontrada!',
                            title='Notificação',
                            location=(500, 500)
                        )
                    else:
                        search.hide()
                        result = window_result(results)
                end_time = datetime.now()
                execution_time = (end_time - start_time).total_seconds() * 1000
            elif event == 'Voltar':
                search.hide()
                component.un_hide()
        if window == result:
            if event == Interface.WIN_CLOSED:
                break
            elif event == 'Analisar':
                result.hide()
                analysis = window_analysis(execution_time, process)
            elif event == 'Voltar':
                result.hide()
                search.un_hide()
        if window == analysis:
            if event == Interface.WIN_CLOSED:
                break
            elif event == 'Voltar':
                analysis.hide()
                result.un_hide()
    window.close()
