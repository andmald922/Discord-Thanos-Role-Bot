class ThanosExceptions(Exception):
    pass


class InvalidSyntaxError(Exception):
    def __init__(self):
        pass

    def __str__(self):
        return 'Invalid syntax, enter -h to receive more information'
