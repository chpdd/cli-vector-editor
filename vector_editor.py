from cli import CLI, CommandHandler
from figures import FiguresContainer


def main():
    figures = FiguresContainer()
    cli = CLI(cli_title="VectorEditor")
    cli.add_handler(CommandHandler("create", figures.create))
    cli.add_handler(CommandHandler("delete", figures.delete))
    cli.add_handler(CommandHandler("list", figures.list_figures))
    cli.add_handler(CommandHandler("save", figures.save_in_file))
    cli.add_handler(CommandHandler("load", figures.load_from_file))
    cli.run()


if __name__ == '__main__':
    main()
