# #!/usr/bin/python3
# import json,datetime,uuid,re,os
# class Transform:
#     def __init__(self, dict):
#         return self.__dict__.update(dict)

#     @staticmethod
#     def ToJson():
#         return json.dumps(dict_data)
    
#     @staticmethod
#     def ToDict():
#         return json.loads(json_data)
    
#     @classmethod
#     def ToObject(cls, json_data):
#         return json.loads(json_data, object_hook=cls)
# json_data = '{"name":"beki", "age":31}'
# dict_data = {"name":"bereket", "age":31}
# print("name: ",Transform.ToObject(json_data).name)
# print("name: ",Transform.ToJson())
    
    


# class BaseModel:
    
#     def __init__(self, kwargs):
#         self.id = uuid.uuid4().__str__()
#         for attr in kwargs:
#             self.__setattr__(attr, kwargs[attr])
#         self.created_at = datetime.datetime.now().__str__()
#         self.updated_at = datetime.datetime.now().__str__()
#     @classmethod
#     def file_name(cls):
#         return "".join(list(re.sub("[A-Z]", lambda m:"_"+m[0].lower(),cls.__name__))[1:])+"s.json"
    
#     @classmethod
#     def truncate(cls):
#         filename = "./db/"+cls.file_name()
#         if os.path.exists(filename):
#             os.unlink(filename)
#             print("{} truncated {} deleted".format(cls.__name__, filename))
#         else:
#             print("{} not found".format(filename))

#     @classmethod
#     def save(self):
#         filename = "./db/"+self.file_name
#         user_list = self.all(return_type ="dict")
#         user_list.append(self.__dict__)
#         user_list_json = json.dumps(user_list, indent=4)

#         with open(filename, 'w') as fileobj:
#             fileobj.write(user_list_json)
#             print(self.__class__.__name__+"saved")

#     @classmethod
#     def find(cls, search ={}, case_insensitive=False,
#     return_type="json"):
#         item_list = cls.all(return_type="dict")
#         if(isinstance(search, dict) and not len(search)):
#             return item_list
#         if not (isinstance(search,dict)):
#             raise TypeError("search parameter must be a dictionery")
#         if (len(search) > 1):
#             raise Exception("search parameter were not well constructed")
#         search_key = list(search.keys())[0]
#         search_value = search[search_key]
#         has_prop = False
        
#         for record in item_list:
#             if record.__contains__(search_key):
#                 has_prop = True
#         if not (has_prop):
#             raise KeyError("search proper key does not much each model")

#     @classmethod
#     def find_by_id(cls, search_id, return_type="json"):
#         if not search_id:
#             raise Exception("you must provide search id")
#         if(len(search_id)!=36):
#             raise Exception("len of search id must be 36")
#         item_list = cls.all(return_type="object")
#         for record in item_list:
#             if record.id == search_id:
#                 if(return_type == "object"):
#                     return record
#                 elif(return_type =="dict"):
#                     return Transform.ToDict(Transform.tojson(record.__dict__))
#                 return Transform.ToJson(record.__dict__)
#         return None
#     @classmethod
#     def all(cls, return_type="json"):
#         filename = "./db/"+cls.file_name()

#         if(os.path.exists(filename) and os.stat(filename).st_size):
#             with open(filename, 'r') as fileobj:
#                 if(return_type == "object"):
#                     return Transform.ToObject(fileobj.read())
#                 elif (return_type == "dict"):
#                     return Transform.ToDict(fileobj.read())
#                 else:
#                     return fileobj.read()
#         else:
#             return []


# class Animal(BaseModel):
#     def __init__(self, **kwargs):
#         super().__init__(kwargs)
# an =Animal(name ="bob", age = 34)
# # Animal.save()
# class Car(BaseModel):
#     def __init__(self, **kwargs):
#         super().__init__(kwargs)

# class Book(BaseModel):
#     def __init__(self, **kwargs):
#         super().__init__(kwargs)        
        
# dog = Animal(name="popy", age=32)
# print(dog.name)
# print(dog.id)

# print(dog.updated_at)

# print(type(dog.created_at))

# name ="_hello"
# print(list(name[2:]+"s.stud"))
# print(Animal.file_name())

