import json

class Database:

    def register(self,name,email,password):
        with open('users.json','r') as f:
            users = json.load(f)

            if email in users:
                return 0
            else:
                users[email] = [name,password]

        with open('users.json','w') as f:
            json.dump(users,f)
            return 1


    def login_check(self,email,password):

        with open('users.json','r') as f:
            users = json.load(f)
            if email in users:
                if users[email][1] == password:
                    return 1
                else:
                    return 0
            return  0
