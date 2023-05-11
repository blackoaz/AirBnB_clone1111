import cmd


class HelloWorld(cmd.Cmd):
    """Creating a terminal in python"""

    def do_greet(self, person):
        """Function for grreting"""
        if person:
            print("Hello," person)
        else:
            print("hi")

    def do_quit(self, args):
        return True


if __name__ == "__main__":
    HelloWorld().cmdloop()
