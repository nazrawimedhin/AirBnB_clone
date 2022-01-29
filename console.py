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
        """Prints the string representation of an instance based on
        the classname and id
        Usage: show <class_name> <id>
        Example: show BaseModel 1234-1234-1234"""
        if arg == "":
            print("** class name missing **")
        elif arg.split()[0] not in self.storage.all_models.keys():
            print("** class doesn't exist **")
        else:
            try:
                id = arg.split()[1]
                for i in self.storage.all().values():
                    if id == i.to_dict()["id"]:
                        # Print the object to the screen
                        print(i)
                        return False
                print("** no instance found **")
            except IndexError:
                print("** instance id missing **")

    def do_destroy(self, arg):
        """Deletes the object with the matching id
        Usage: destroy <class_name> <id>
        Example: destroy BaseModel 121212"""
        if arg == "":
            print("** class name missing **")
        elif arg.split()[0] not in self.storage.all_models.keys():
            print("** class doesn't exist **")
        else:
            try:
                if self.storage.destroy(arg.split()[1]):
                    return False
                print("** no instance found **")
            except IndexError:
                print("** instance id missing **")

    def do_all(self, arg):
        """Prints all string representation of all instances based on or not
        on the class name
        Usage: all <class_name>
               all
        Example: all BaseModel"""
        all_objs = []
        try:
            if arg.split()[0] not in self.storage.all_models.keys():
                print("** class doesn't exist **")
                return False
            for i in self.storage.all().values():
                if i.to_dict()["__class__"] == arg.split()[0]:
                    all_objs.append(i.__str__() + " " + str())
            print(all_objs)

        #  IndexError is raised only if the prompt takes 'all' only,
        #  hence print all the objects stored
        except IndexError:
            for i in self.storage.all().values():
                all_objs.append(i.__str__())
            print(all_objs)


if __name__ == '__main__':
    try:
        HBNBCommand().cmdloop()
    except KeyboardInterrupt:
        print()
        quit(0)
