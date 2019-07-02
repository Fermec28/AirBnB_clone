#!/usr/bin/python3
import cmd
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    '''Hbnbc command'''
    intro = 'Welcome to the Hbnb shell. Type help or ? to list commands.\n'
    prompt = '(hbnb) '
    file = None

    def do_EOF(self, line):
        return True

    def do_quit(self, line):
        return True

    def do_create(self, line):
        if len(line) == 0:
            print("** class name missing **")
        elif line != "BaseModel":
            print("** class doesn't exist **")
        else:
            my_model = BaseModel()
            my_model.save()
            print(my_model.id)

    def help_create(self):
        print("Creates a new instance of BaseModel, saves "
              "it (to the JSON file) and prints the id.\n"
              "Ex: $ create BaseModel\n")

    def help_quit(self):
        print("Quit command to exit the program \n")

    def help_EOF(self):
        print("Quit command to exit the program \n")

    def emptyline(self):
        print("", end="")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
