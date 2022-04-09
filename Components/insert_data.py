# coding=utf8

from os import remove, path


def insert_file(names: str) -> bool:
    """
    :param names: list of string
    :return: boolean
    """
    try:
        with open(file=names, mode='r', encoding='utf8') as file:
            if path.exists(path=r'./Assets/names.txt'):
                remove(r'./Assets/names.txt')
            data = open(file='./Assets/names.txt', mode='a', encoding='utf8')
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
    :return: boolean
    """
    try:
        if path.exists(path=r'./Assets/names.txt'):
            remove(r'./Assets/names.txt')
        data = open(file='./Assets/names.txt', mode='a', encoding='utf8')
        for i in names:
            data.write(i)
        data.close()
        return True
    except Exception as e:
        print(e.args)
        return False
