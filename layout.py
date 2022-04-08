# coding=utf8

from PySimpleGUI import PySimpleGUI as Interface

Interface.theme('DarkGrey10')
layout = [
    [
        Interface.Button(button_text='Inserir'),
        Interface.Button(button_text='Buscar')
    ]
]
window = Interface.Window('Desafio Desenvolvedor', layout)
while True:
    # event, values = window.read()
    event, values = Interface.Window(
        'Get filename example', [
            [Interface.Text('Inserir Arquivo:')],
            [Interface.Input(), Interface.FileBrowse()],
            [Interface.OK(), Interface.Cancel()]
        ]).read(close=True)
    if event == Interface.WIN_CLOSED or event == 'Cancel':
        break
    print('You entered ', values[0])
window.close()
