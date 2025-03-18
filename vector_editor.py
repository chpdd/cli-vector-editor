from cli import CLI, CommandHandler
from figures import *


def main():
    figures = FiguresContainer()
    cli = CLI(cli_title="Command")
    cli.add_handler(CommandHandler("create", figures.create))
    cli.add_handler(CommandHandler("delete", figures.delete))
    cli.add_handler(CommandHandler("list", figures.list_figures))
    cli.run_command_handler()


if __name__ == '__main__':
    main()
