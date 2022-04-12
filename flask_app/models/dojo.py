from unittest import result
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import ninja


class Dojo:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

        self.ninjas = []

    @classmethod
    def save(cls,data):
        query = "INSERT INTO dojos (name, created_at, updated_at) VALUES (%(name)s, NOW(), NOW())"
        result = connectToMySQL('mydb').query_db(query, data)
        return result

    @classmethod
    def show(cls):
        # modify query to return all columns from dojos
        query = "SELECT * FROM dojos;"
        result = connectToMySQL('mydb').query_db(query)
        dojos =[]
        print(result)
        # return list of class objects from result
        for dojo in result:
            dojos.append( cls(dojo) )
        return dojos

    @classmethod
    def get_all_ninjas_in_dojo(cls, data):
        query = "SELECT * FROM dojos LEFT JOIN ninjas ON ninjas.dojo_id = dojos.id WHERE dojos.id = %(id)s"
        result = connectToMySQL('mydb').query_db(query, data)
        ninja1 = cls(result[0])
        for ninja_in_loop in result: 
            ninja_info = {
                'id': ninja_in_loop['ninjas.id'],
                'first_name': ninja_in_loop['first_name'],
                'last_name': ninja_in_loop['last_name'],
                'age': ninja_in_loop['age'],
                'created_at': ninja_in_loop['ninjas.created_at'],
                'updated_at': ninja_in_loop['ninjas.updated_at']
            }
            ninja1.ninjas.append(ninja.Ninja(ninja_info))
        return ninja1