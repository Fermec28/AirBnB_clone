#!/usr/bin/python3
import cmd


class HBNBCommand(cmd.Cmd):
    '''Hbnbc command'''
    intro = 'Welcome to the Hbnb shell.   Type help or ? to list commands.\n'
    prompt = '(hbnb) '
    file = None

    def do_EOF(self, line):
        return True

    def do_quit(self, line):
        self.do_EOF(self)

    def help_quit(self):
        print("Quit command to exit the program \n")

    def emptyline(self):
        print("", end="")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
