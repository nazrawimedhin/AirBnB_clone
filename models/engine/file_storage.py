#!/usr/bin/python3
"""Module file_storage
Contains class FileStorage"""
import json
from importlib import import_module


class FileStorage:
    """Handles saving data into a JSON file, also retrieving from it """

    # File to store JSON data generated by this class
    __file_path = "file.json"
    __objects = {}  # Stores all objects by <class name>.id

    #  Holds all the possible classes that objects can be made from
    all_models = {
        "BaseModel": import_module("models.base_model").BaseModel
    }

    def all(self):
        """Returns all objects in __objects"""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id
        Adds a new object to the objects dictionary"""
        class_name = obj.__class__.__name__ + "." + obj.id
        self.__objects.update([(class_name, obj)])

    def save(self):
        """Serializes __objects and saves it to __file_path"""
        with open(self.__file_path, "w") as f:
            to_write_to_json = {}
            for i, j in zip(self.__objects.keys(), self.__objects.values()):
                to_write_to_json.update([(i, j.to_dict())])
            f.write(json.dumps(to_write_to_json))

    def destroy(self, id_to_delete):
        """Finds a BaseModel with matching id in __objects, deletes it and
        updates __file_path to delete it in the JSON as well

        Returns: True, if the object was found, and it's deleted
                 False, if the object wasn't found"""
        for i, j in zip(self.__objects.keys(), self.__objects.values()):
            if id_to_delete == j.to_dict()["id"]:
                self.__objects.pop(i)
                self.save()
                return True
        return False

    def reload(self):
        """Loads objects from __file_path and stores them in __objects"""
        self.__objects = {}
        try:
            with open(self.__file_path, "r") as f:
                if f.read() != "":
                    f.seek(0)
                    json_dict = json.load(f)
                    #  Create objects from the JSON by looking up matching
                    #  class name from the JSON file and all_models.
                    #  When a matching __class__ is found, the object is
                    #  initialized from the dictionary representation of it.
                    for i, j in zip(json_dict.keys(), json_dict.values()):
                        reloaded_obj = self.all_models[j["__class__"]](**j)
                        self.__objects.update([(i, reloaded_obj)])

        except FileNotFoundError:
            return
