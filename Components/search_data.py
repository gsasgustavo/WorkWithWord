# coding=utf8

from os import path

from mmap import mmap, ACCESS_READ


def search(name):
    """
    :param name: string
    :return: list of string
    """
    try:
        if not path.exists(r'./Assets/names.txt'):
            raise FileNotFoundError('Arquivo para pesquisa está ausente')
        result = list()
        with open(file=r'./Assets/names.txt', mode='r', encoding='utf8') as file:
            lines = [x.strip() for x in file.readlines()]
            for line in lines:
                if name.lower() in line.lower():
                    result.append(line)
            return result
    except Exception as e:
        print(e.args)
