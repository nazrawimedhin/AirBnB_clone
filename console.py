#!/usr/bin/python3

"""Module console.py
The program starts here. Run this script to interact with the program"""

import cmd


class HBNBCommand(cmd.Cmd):
    """The console program for this AirBnB clone starts here"""
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Exit the HBNB console:  quit"""
        return True

    def do_EOF(self, arg):
        """Exit the HBNB console:  EOF"""
        return True


if __name__ == '__main__':
    hbnb_console = HBNBCommand()
    hbnb_console.cmdloop()
