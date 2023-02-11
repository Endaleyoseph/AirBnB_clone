#!/usr/bin/python3
from datetime import datetime
import models
import uuid


class BaseModel:

    def __init__(self, *args, **kwargs):

        if kwargs:
            for arg, val in kwargs.items():
                if arg in ('created_at', 'updated_at'):
                    val = datetime.strptime(val, '%Y-%m-%dT%H:%M:%S.%f')
                if arg != '__class__':
                    setattr(self, arg, val)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)

    def __str__(self):

        return '[{0}] ({1}) {2}'.format(
                self.__class__.__name__, self.id, self.__dict__
            )

    def save(self):
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):

        dict_copy = self.__dict__.copy()
        dict_copy['__class__'] = self.__class__.__name__
        dict_copy['created_at'] = self.created_at.isoformat()
        dict_copy['updated_at'] = self.updated_at.isoformat()
        return dict_copy

#     def file_name(self):
#         return ("".join(list("[A-z]", lambda m:"_"+m[0].lower(),\
#         self.__name__))[1:])+"s.json"
# class Animal(BaseModel):
#     def __init__(self, *args, **kwargs):
#         super().__init__(kwargs)
# dog =Animal(name = "dog", age = 35)
# print(dog.__dict__)
# print(dog.id)
# print(dog.age)
# print(dog.created_at)
# print(Animal.file_name())
