#!/usr/bin/python3
"""Module for BaseModel class."""

import cmd
import uuid
from datetime import datetime
from models import storage




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


if __name__ == '__main__':
    HBNBCommand().cmdloop()
