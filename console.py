#!/usr/bin/python3

"""Module console.py
The program starts here. Run this script to interact with the program"""

import cmd
import models


class HBNBCommand(cmd.Cmd):
    """The console program for this AirBnB clone starts here"""
    prompt = "(hbnb) "
    storage = models.storage

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

    def postloop(self):
        """Print a new line when program exits"""
        print()

    def do_create(self, arg):
        """Create a new instance with the argument as the class name
        Create a new instance of BaseModel: create BaseModel"""
        if arg == "":
            print("** class name missing **")
        elif arg not in self.storage.all_models.keys():
            print("** class doesn't exist **")
        else:
            bm = self.storage.all_models.get(arg)()
            bm.save()
            print(bm.to_dict().get("id"))

    def do_show(self, arg):
        """Prints the string representation of an instance based on the
        class name and id
        Example: show BaseModel 1234-1234-1234"""
        if arg == "":
            print("** class name missing **")
        elif arg.split()[0] not in self.storage.all_models.keys():
            print("** class doesn't exist **")
        else:
            try:
                for i in self.storage.all().values():
                    if arg.split()[1] == i.to_dict()["id"]:
                        # Print the object to the screen
                        print(i)
                        return False
                print("** instance id missing **")
            except IndexError:
                print("** instance id missing **")


if __name__ == '__main__':
    try:
        HBNBCommand().cmdloop()
    except KeyboardInterrupt:
        print()
        quit(0)
