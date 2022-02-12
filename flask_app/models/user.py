from flask_app.config.mysqlconnection import MySQLConnection, connectToMySQL
from flask_app import app
from flask_app.models import

 CREATE model
    @classmethod
    def create_dojo(cls, data):
        query= '''
        Insert INTO dojos (name)
        VALUES (%(name)s)
        ;'''
        return connectToMySQL('dojos_and_ninjas_schema').query_db(query,data)


#READ model
    @classmethod
    def get_all_dojos(cls):
        query = """
        SELECT *
        FROM dojos
        ;"""
        result = connectToMySQL(cls.db).query_db(query)
        # print('LIST OF USERS', result)
        dojos = []
        for d in result:
            dojos.append(cls(d))
        return dojos

    @classmethod
    def get_one_dojo(cls,id):
        data= {'id' : id}
        query= '''
        SELECT *
        FROM dojos
        LEFT JOIN ninjas ON dojos.id = ninjas.dojo_id
        WHERE dojos.id = %(id)s
        ;'''
        result =  connectToMySQL(cls.db).query_db(query, data)
        this_dojo = cls(result[0])
        for a_ninja in result:
            data = {
                'id' : a_ninja['ninjas.id'],
                'first_name' : a_ninja['first_name'],
                'last_name' : a_ninja['last_name'],
                'age' : a_ninja['age'],
                'dojo_id' : a_ninja['dojo_id'],
                'created_at' : a_ninja['ninjas.created_at'],
                'updated_at' : a_ninja['ninjas.updated_at'],
                
            }
            this_dojo.ninjas.append(ninja.Ninja(data))
        return this_dojo

    #read all ninjas
    #left join to show all even if there are none
    # foriegn key ninja, primary dojo
    # on dojos.id = books.user_id
    # wHERE dojos.id = %(id)s

#UPDATE model
    @classmethod
    def update_dojo(cls, data):
        pass


#Delete

    @classmethod
    def delete_dojo(cls, id):
        data = { 'id' : id}
        query=  '''
        DELETE * FROM dojos
        WHERE id = %(id)s
        ;'''
        return connectToMySQL(cls.db).query_db(query, data)

    #Nuclear option
    def delete_all_dojo(cls):
        data = { 'id' : id}
        query=  '''
        DELETE * FROM dojos
        ;'''
        return connectToMySQL(cls.db).query_db(query, data)
