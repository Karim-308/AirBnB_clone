#!/usr/bin/python3
"""This module serves as the central command interpreter
for the HBNB project.

It introduces the `HBNBCommand()` class, which extends
the functionality of the `cmd.Cmd` class.
This module encapsulates the logic for interacting with
the underlying storage system,
allowing for seamless manipulation of data models and objects.

Key features include:
- Creation and management of data models and objects
- Interactive and non-interactive modes for ease of use
- Flexible storage options, for FileStorage and database

Example usage:

    $ ./console
    (hbnb)

    (hbnb) help
    Documented commands (type help <topic>):
    ========================================
    EOF  create  help  quit

    (hbnb)
    (hbnb) quit
    $
"""
import cmd
import uuid
import models
from datetime import datetime
from models.base_model import BaseModel
from models.state import State
from models.city import City
from models.user import User
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """The command interpreter.

    Class is the command interpreter with center for control
    for the project. This has handlers for all  the commands in
    console and calls the storage engine APIs to manipulate
    the data and models.
    """

    prompt = '(hbnb) '

    def do_quit(self, arg):
        """
        Quit command to exit the program.

        Usage: quit
        """
        return True

    def do_EOF(self, arg):
        """
        EOF command to exit the program.

        Usage: Ctrl+D or Ctrl+C
        """
        print()
        return True

    def do_help(self, arg):
        """
        Help command to display help messages.

        Usage: help [command]
        """
        cmd.Cmd.do_help(self, arg)

    def emptyline(self):
        """
        Handle empty input lines.

        This method does nothing when an empty line is entered.
        """
        pass

    def do_create(self, arg):
        """
        Create a new instance of BaseModel, save it, and print the id.

        Usage: create <class_name>
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in globals():
            print("** class doesn't exist **")
            return
        new_instance = eval(class_name)()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """
        Print the string representation of an instance
        based on the class name and id.

        Usage: show <class_name> <id>
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in globals():
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        obj_id = args[1]
        key = class_name + '.' + obj_id
        if key not in models.storage.all():
            print("** no instance found **")
            return
        print(storage.all()[key])

    def do_destroy(self, arg):
        """
        Delete an instance based on the class name and id.

        Usage: destroy <class_name> <id>
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in globals():
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        obj_id = args[1]
        key = class_name + '.' + obj_id
        if key not in models.storage.all():
            print("** no instance found **")
            return
        del models.storage.all()[key]
        models.storage.save()

    def do_all(self, arg):
        """
        Print the string representation of all instances
        or instances of a specific class.

        Usage: all [class_name]
        """
        args = arg.split()
        obj_list = []
        if not args:
            for key in models.storage.all():
                obj_list.append(str(models.storage.all()[key]))
            print(obj_list)
            return
        class_name = args[0]
        if class_name not in globals():
            print("** class doesn't exist **")
            return
        for key in models.storage.all():
            if key.split('.')[0] == class_name:
                obj_list.append(str(models.storage.all()[key]))
        print(obj_list)

    def do_count(self, arg):
        """Count the number of instances of a given class."""
        classes = arg.split('.')
        class_name = classes[0] if len(classes) == 2 else arg
        count = sum(1 for obj in models.storage.all().values()
                    if obj.__class__.__name__ == class_name)
        print(count)

    def do_update(self, arg):
        """
        Update an instance based on the class name
        and id by adding or updating an attribute.

        Usage: update <class_name> <id> <attribute_name> <attribute_value>
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in globals():
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        obj_id = args[1]
        key = class_name + '.' + obj_id
        if key not in models.storage.all():
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        setattr(models.storage.all()[key], args[2], args[3].strip('"'))
        models.storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
