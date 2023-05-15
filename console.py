#!/usr/bin/python3
import cmd


class HBNBCommand(cmd.Cmd):
    """Creating a terminal in python"""
    prompt = "(hbnb)"

    def do_EOF(self, args):
        """Function for end of file"""
        return True

    def emptyline(self):
        """Function for emptyline"""
        pass

    def help_EOF(self):
        """Help function for EOF method"""
        print("Function for exitting the program")

    def help_quit(self):
        """Help function for quit"""
        print("Function for quiring the console")

    def do_quit(self, args):
        return True


if __name__ == "__main__":
    HBNBCommand().cmdloop()
