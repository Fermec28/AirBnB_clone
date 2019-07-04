#!/usr/bin/python3
#create BaseModel instance

from models import storage
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.review import Review

all_objs = storage.all()
print("-- Reloaded objects --")
for obj_id in all_objs.keys():
    obj = all_objs[obj_id]
    print(obj)

print("-- Create a new object --")
object = Review()
object.save()
