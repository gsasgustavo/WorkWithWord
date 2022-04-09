# coding=utf8

from os import path
from unidecode import unidecode


def search(name, mode):
    """
    :param name: string
    :return: list of string
    """
    try:
        if not path.exists(r'./Assets/names.txt'):
            raise FileNotFoundError('Arquivo para pesquisa está ausente')
        result = list()
        with open(file=r'./Assets/names.txt', mode='r', encoding='utf8') as file:
            if mode == 1:
                for line in file:
                    if name in line:
                        result.append(line.replace('\n', ''))
            elif mode == 2:
                for line in file:
                    if name in unidecode(line.lower()):
                        result.append(line.replace('\n', ''))
            return result
    except Exception as e:
        print(e.args)
