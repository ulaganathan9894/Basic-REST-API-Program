import sqlite3
from flask_restful import Resource, reqparse
from Models.user import UserModel 

class Register(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username',
                        type = str,
                        required = True,
                        help = "This field cannot be blank that"
                        )
    

    parser.add_argument('password',
                        type = str,
                        required = True,
                        help = "This field cannot be blank that"
                        )                    



    def post(self):
        request_data = Register.parser.parse_args()

        if  UserModel.usernamefinding(request_data['username']):
            return{'Message': 'A user with that username already exist'}, 400


        user = UserModel(**request_data)
        user.save_db()
        
##        connection = sqlite3.connect('data.db')
##        cursor = connection.cursor()
##        insert = "INSERT INTO users VALUES(NULL, ?, ?)"
##        cursor.execute(insert, (request_data['username'],request_data['password']))
##
##        connection.commit()
##        connection.close()

        return {'Message':'User Id was created successfully'}, 201
                       
        
