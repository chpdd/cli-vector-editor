A simple vector editor with a command line interface (CLI).
It is implemented in such a way that it can be easily extended, as the processing of commands here is implemented using separate objects of the CommandHandler class.

To understand how to work with commands, write “help” to the console.
exit:
        Command that terminates the program
        :param: No params
        :example: exit
        
help:
        Command that explains how commands work
        :param: No params
        :example: help
        
create:
        Creates figures using arguments.
        :param: figure_type and coordinates
        :example: create square 1 2 3 4

        Types of figures and args:
        Point - 2 coordinates,
        Line - 2 points(4 coordinates),
        Circle - center point(2 coordinates) and radius,
        Square - diagonal(4 coordinates)

        
delete:
        Deletes a figure by key
        :param: key
        :example: delete 1
        
list:
        Outputs a list of all figures with their indexes
        :param: No params
        :example: list
