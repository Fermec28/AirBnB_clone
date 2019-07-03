#!/usr/bin/python3
import cmd
import models
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

    def do_all(self, line):
        if line != "BaseModel" and line != "":
            print("** class doesn't exist **")
        else:
            objects = models.storage.all()
            toPrint = []
            for k, v in objects.items():
                toPrint.append(str(v))

            print(toPrint)

    def do_show(self, line):
        args = str(line).split(' ')
        idPrinted = 0
        if args[0] == '':
            print("** class name missing **")
        elif args[0] != "BaseModel":
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            objects = models.storage.all()
            for k, v in objects.items():
                model = str(k).split('.')
                if args[1] == model[1]:
                    idPrinted = 1
                    print(v)
            if idPrinted is 0:
                print("** no instance found **")

    def help_show(self):
        print("Prints the string representation of an instance "
              "based on the class name and id.\n"
              "Ex: $ show BaseModel 1234-1234-123\n")

    def help_all(self):
        print("Prints all string representation of all instances "
              "based or not on the class name.\n"
              "Ex: $ all BaseModel or $ all \n")

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
