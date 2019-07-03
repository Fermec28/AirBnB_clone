#!/usr/bin/python3
import cmd
import shlex
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
        args = str(line).split(' ')
        if len(line) == 0:
            print("** class name missing **")
        elif not args[0] in models.storage.validClasses:
            print("** class doesn't exist **")
        else:
            my_model = models.storage.validClasses[args[0]]()
            my_model.save()
            print(my_model.id)

    def do_all(self, line):
        args = str(line).split(' ')
        objects = models.storage.all()
        toPrint = []
        if args[0] == "":
            for k, v in objects.items():
                toPrint.append(str(v))
            print(toPrint)
        elif not args[0] in models.storage.validClasses:
            print("** class doesn't exist **")
        else:
            for k, v in objects.items():
                cname = str(k).split('.')
                if args[0] == cname[0]:
                    toPrint.append(str(v))
            print(toPrint)

    def do_show(self, line):
        args = str(line).split(' ')
        idPrinted = 0
        if args[0] == '':
            print("** class name missing **")
        elif not args[0] in models.storage.validClasses:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            objects = models.storage.all()
            try:
                obj = objects["{}.{}".format(args[0], args[1])]
                print(obj)
            except:
                print("** no instance found **")

    def do_destroy(self, line):
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
            try:
                obj = objects["{}.{}".format(args[0], args[1])]
                obj.destroy()
            except:
                print("** no instance found **")

    def do_update(self, line):
        args = shlex.split(line)
        idPrinted = 0
        if args[0] == '':
            print("** class name missing **")
        elif args[0] != "BaseModel":
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif len(args) < 3:
            print("** attribute name missing **")
        elif len(args) < 4:
            print("** value missing **")
        elif args[2] != "id" and args[2] != "created_at" and \
                        args[2] != "updated_at":
            obj = models.storage.all()
            key = "{}.{}".format(args[0], args[1])
            try:
                obj[key].update(args[2], args[3])
            except:
                print("** no instance found **")

    def help_update(self):
        print("Updates an instance based on the class name and id by "
              "adding or updating attribute.\n"
              "Ex: $ update BaseModel 1234-1234-1234 name "'"First name"')

    def help_destroy(self):
        print("Deletes an instance based on the class name and id.\n"
              "Ex: $ destroy BaseModel 1234-1234-1234\n")

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
