#!/usr/bin/python3
"""Module for BaseModel class."""

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
    """Command interpreter for HBNB project."""

    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program."""
        print()
        return True

    def do_help(self, arg):
        """Help command to display help messages."""
        cmd.Cmd.do_help(self, arg)

    def emptyline(self):
        """Handle empty input lines."""
        pass

    def do_create(self, arg):
        """Create a new instance of BaseModel, saves it, and prints the id."""
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
        """Prints the string representation of an instance based on the class name and id."""
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
        """Deletes an instance based on the class name and id."""
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
        """Prints all string representation of all instances."""
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
        """Updates an instance based on the class name and id by adding or updating attribute."""
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
        storage.all()[key].save()


    def do_count(self, arg):
        """Usage: count <class> or <class>.count()
        Retrieve the number of instances of a given class."""
        class_name = arg.split('.')[0]
        if class_name not in globals():
            print("** class doesn't exist **")
            return
        if len(arg.split('.')) == 2 and arg.split('.')[1] != 'count()':
            print("** Unknown syntax: {}".format(arg))
            return
        count = 0
        for obj in storage.all().values():
            if obj.__class__.__name__ == class_name:
                count += 1
        print(count)



if __name__ == '__main__':
    HBNBCommand().cmdloop()
