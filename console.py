#!/usr/bin/python3

"""Module console.py
The program starts here. Run this script to interact with the program"""

import cmd


class HBNBCommand(cmd.Cmd):
    """The console program for this AirBnB clone starts here"""
    prompt = "(hbnb) "

    def emptyline(self):
        """Empty line + Enter will just return the prompt without any error.
        i.e. the prompt will not execute the previous command"""
        return False

    def do_quit(self, arg):
        """Exit the HBNB console:  quit"""
        return True

    def do_EOF(self, arg):
        """Exit the HBNB console:  EOF"""
        return True


if __name__ == '__main__':
    try:
        HBNBCommand().cmdloop()
    except KeyboardInterrupt:
        print()
        quit(0)
