# coding=utf8

from os import remove, path


def insert_file(names: str) -> bool:
    """
    :param names: list of string
    :return: boolean
    """
    try:
        with open(names, 'r') as file:
            if path.exists(r'./Assets/names.txt'):
                remove(r'./Assets/names.txt')
            data = open('./Assets/names.txt', 'a')
            for i in file.read():
                data.write(i)
            data.close()
        file.close()
        return True
    except Exception as e:
        print(e.args)
        return False


def insert_text(names: str) -> bool:
    """
    :param names: list of string
    :return:
    """
    try:
        print(names.split('\n'))
        file = names.split('\n')
        if path.exists(r'./Assets/names.txt'):
            remove(r'./Assets/names.txt')
        data = open('./Assets/names.txt', 'a')
        for i in file:
            data.write(i)
        data.close()
        return True
    except Exception as e:
        print(e.args)
        return False
