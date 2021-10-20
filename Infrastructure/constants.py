from flask import Flask

app = Flask(__name__)

DATABASE = 'database.sqlite'


def build_path_with_args(route_name: str, *args):
    """

    :param route_name: Путь из мапки
    :param args: Агрументы пути
    :return: Возвращает полный путь, с учетом '/' и множества параметров
    """

    args_len = len(args)

    if args_len != 0:

        if args_len == 1:
            return f'{route_name}/{args[0]}'
        else:
            _str = f'{route_name}'
            for value in args:
                _str.join(f'/{value}')

            print(_str)
            return _str

    raise 'Метод ожидает аргументы в кол-во от 1-го'
