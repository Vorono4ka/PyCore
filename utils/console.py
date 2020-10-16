class Console:
    def __init__(self, prefix):
        self.prefix = prefix

    def update_prefix(self, prefix) -> None:
        self.prefix = prefix

    def print(self, *args, **kwargs) -> None:
        if 'enter_new_string' not in kwargs:
            kwargs['enter_new_string'] = True

        print(f'[{self.prefix}]', end=' ')
        for arg in args:
            print(arg, end=' ')

        if kwargs['enter_new_string']:
            print()

    def ask(self, *args) -> str:
        self.print(*args[:-1], enter_new_string=False)
        return input(f'{args[-1]}: ')

    def ask_integer(self, *args) -> int:
        asked = self.ask(*args)

        try:
            asked = int(asked)
        except ValueError:
            asked = self.ask_integer(*args)

        return asked
