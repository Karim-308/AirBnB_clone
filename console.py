#!/usr/bin/python3
"""Module for HBNBCommand class, a command interpreter for the HBNB project."""

import cmd
import uuid
from datetime import datetime
from models import storage
from models.base_model import BaseModel
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """Command interpreter for the HBNB project."""

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
        Print the string representation of an instance based on the class name and id.

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
        if key not in storage.all():
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
        if key not in storage.all():
            print("** no instance found **")
            return
        del storage.all()[key]
        storage.save()

    def do_all(self, arg):
        """
        Print the string representation of all instances or instances of a specific class.

        Usage: all [class_name]
        """
        args = arg.split()
        obj_list = []
        if not args:
            for key in storage.all():
                obj_list.append(str(storage.all()[key]))
            print(obj_list)
            return
        class_name = args[0]
        if class_name not in globals():
            print("** class doesn't exist **")
            return
        for key in storage.all():
            if key.split('.')[0] == class_name:
                obj_list.append(str(storage.all()[key]))
        print(obj_list)

    def do_update(self, arg):
        """
        Update an instance based on the class name and id by adding or updating an attribute.

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
        if key not in storage.all():
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        setattr(storage.all()[key], args[2], args[3].strip('"'))
        storagesave()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
