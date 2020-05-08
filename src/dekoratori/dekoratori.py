from getpass import getpass

from helper.shell import shell_clear as cls


def isgreaterthan(argument):
    def main_wrapper(function):
        def wrapper(*args):
            if args[1] <= argument:
                raise ValueError('Neispravna vrednost')
            return function(*args)

        return wrapper

    return main_wrapper


def wrapisinstance(argument):
    def main_wrapper(function):
        def wrapper(*args):
            if isinstance(args[1], argument):
                return function(*args)
            else:
                raise TypeError(f'Nepravilan tip argumenta: {type(args[1])}, ocekuje se {argument}')

        return wrapper

    return main_wrapper


def isinrange(argument):
    def main_wrapper(function):
        def wrapper(*args):
            if not (argument[0] <= args[1] <= argument[1]):
                raise ValueError('Neispravna vrednost')
            return function(*args)

        return wrapper

    return main_wrapper


def isnotempty(function):
    def wrapper(*args):
        if isinstance(args[1], str):
            if not args[1]:
                raise ValueError('Prazna vrednost nije dozvoljena!')
        return function(*args)

    return wrapper


def cleanshell(function):
    def wrapper(*args, **kw):
        cls()
        ret_func = function(*args, **kw)
        print()
        x = getpass("[pritisnite dugme `enter` za nastavak]")
        cls()
        return ret_func

    return wrapper


def cleanshell_noinput(function):
    def wrapper(*args, **kw):
        cls()
        ret_func = function(*args, **kw)
        cls()
        return ret_func

    return wrapper
