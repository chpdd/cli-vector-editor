from cli import CLI, CommandHandler
from figures import FiguresContainer


def main():
    figures = FiguresContainer()
    cli = CLI(cli_title="VectorEditor")
    cli.add_handler(CommandHandler("create", figures.create))
    cli.add_handler(CommandHandler("delete", figures.delete))
    cli.add_handler(CommandHandler("list", figures.list_figures))
    cli.run()


if __name__ == '__main__':
    main()
