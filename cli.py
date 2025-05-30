class CommandHandler:
    def __init__(self, call_word, action):
        self.call_word = call_word.strip()
        self.action = action

    def __str__(self):
        return f"CommandHandler(command={self.call_word}, action={self.action})"

    def call_check(self, call_word):
        return self.call_word == call_word

    def start(self, input_data):
        print(self.action(*input_data))


class CLI:
    def __init__(self, handlers=None, cli_title="Command"):
        if handlers:
            for handler in handlers:
                if not isinstance(handler, CommandHandler):
                    raise TypeError("CLI accepts only handlers of the CommandHandler class")
        else:
            handlers = []
        self._handlers = handlers
        self._cli_title = cli_title

        self.add_handler(CommandHandler("exit", self.exit))
        self.add_handler(CommandHandler("help", self.help))

    def help(self, *args):
        """
        Command that explains how commands work
        :param: No params
        :example: help
        """
        if len(args) != 0:
            raise ValueError("This command should have 0 arguments")
        result = ""
        for handler in self.handlers:
            result += f"\n{handler.call_word}:{handler.action.__doc__}"
        return result

    @staticmethod
    def exit(*args):
        """
        Command that terminates the program
        :param: No params
        :example: exit
        """
        if len(args) != 0:
            raise ValueError("This command should have 0 arguments")
        exit()

    def __repr__(self):
        return f"CLI(handlers={self.handlers}, cli_title={self.cli_title})"

    @property
    def handlers(self):
        return self._handlers

    @property
    def cli_title(self):
        return self._cli_title

    def add_handler(self, handler):
        self._handlers.append(handler)

    def run(self):
        while True:
            input_data = input(f"{self.cli_title}: ").strip().split()
            if input_data:
                call_word = input_data.pop(0).strip()
                for handler in self.handlers:
                    try:
                        if handler.call_check(call_word):
                            handler.start(input_data)
                            break
                    except Exception as e:
                        print(e)
                        break
                else:
                    print("Unknown command")
            print()
