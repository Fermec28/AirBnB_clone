# AirBnB_clone - The console
Holbertone project clone AirBnB web app

![image abnb](https://camo.githubusercontent.com/a0c52a69dc410e983b8c63fa4aa57e83cb4157cd/68747470733a2f2f73332e616d617a6f6e6177732e636f6d2f696e7472616e65742d70726f6a656374732d66696c65732f686f6c626572746f6e7363686f6f6c2d6869676865722d6c6576656c5f70726f6772616d6d696e672b2f3236332f4842544e2d68626e622d46696e616c2e706e67)

## Description

#### Command interpreter to manage AirBnB objects.

This is the first step towards building your first full web application: the **AirBnB clone**. This first step is very important because you will use what you build during this project with all other following projects: HTML/CSS templating, database storage, API, front-end integration... 

Each task is linked and will help you to:

-   put in place a parent class (called `BaseModel`) to take care of the initialization, serialization and deserialization of your future instances
-   create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file
-   create all classes used for AirBnB (`User`, `State`, `City`, `Place`...) that inherit from `BaseModel`
-   create the first abstracted storage engine of the project: File storage. 
-   create all unittests to validate all our classes and storage engine

### What's a command interpreter?

Do you remember the Shell? It's exactly the same but limited to a specific use-case. In our case, we want to be able to manage the objects of our project:

-   Create a new object (ex: a new User or a new Place)
-   Retrieve an object from a file, a database etc...
-   Do operations on objects (count, compute stats, etc...)
-   Update attributes of an object
-   Destroy an object

## How to start the interpreter

In the command line run:
```sh
$ ./console.py
```
## Class name available
BaseModel, User, State, City, Amenity, Place, Review

## Commands usage:

| Command | Syntax | Description | 
| ------ | ------ | ------ |
| EOF | EOF | Exit command interpreter |
| quit | quit | Exit command interpreter |
| help | help [option] | Lists all available commands, or displays what option does|
| create | create [class_name] or [class_name].create() | Creates an instance of class_name |
| update | update [class_name] [object_id] [update_key] [update_value] or [class].update([object_id] [update_key] [update_value] \()| Updates the key:value of class_name.object_id instance |
| show | show [class_name] [object_id] or [class_name].show([object_id])\() | Displays all attributes of class_name.object_id |
| all | all [class_name], [class_name].all\() | Displays every instance of class_name, if used without option displays every instance saved to the file |
| destroy | destroy [class_name] [object_id] or [class_name].destroy([object_id])\() | Deletes all attributes of class_name.object_id |
| count | count [class_name] or [class_name].count\() | Counts all the instances with class name specified |
