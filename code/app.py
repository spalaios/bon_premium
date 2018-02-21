from flask import Flask, request
from flask_restful import Resource,Api


app = Flask(__name__)
api = Api(app)


#creating in memory list

users = []

class User(Resource):
    def get(self,name):

        #loop through the users list and match the name given in the url with users list
        for user in users:
            if user:
                if user['name'] == name:
                    return user
        return 'No user found', 404

    def post(self,name):
        data = request.get_json()
        user = {
            'name':name,
            "Contact":data['Contact'],
	        "Plan":"Buy us coffee",
            "requested_feature":"More convienent buying plan",
            "requested_feature_date":"21/02/2018",
            "requested_feature_acted_upon":"True",
            "feedback":"Great App!!"
        }

        users.append(user)

        return user, 201


class Users(Resource):
    #since this only a get url we will only declare get method
    def get(self):
        return {'users':users}


api.add_resource(User, '/user/<string:name>')
api.add_resource(Users, '/users')

if __name__ == '__main__':
    app.run(debug=True)