#!/usr/bin/python3
import cmd


class HBNBCommand(cmd.Cmd):
    """Creating a terminal in python"""
    prompt = "(hbnb)"

    def do_EOF(self, arg):
        """Command for quitting the program"""
        print("")
        return True

    def emptyline(self):
        """Do nothing when empty line is passed"""
        pass

    def do_quit(self, arg):
        """Command for quitting the program"""
        return True


if __name__ == "__main__":
    HBNBCommand().cmdloop()
