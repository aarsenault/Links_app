import uuid
import app.common.database as database

database = {'email1@hello.com': 'password1'}

class User(object):
    def __init__(self, email, password, _id=None):
        self.email = email
        self.password = password
        self._id = uuid.uuid4().hex if _id is None else _id

    def __repr__(self):
        return "<User {}>".format(self.email)

    @staticmethod
    def is_login_valid(email, password):
        if email in database:
            if database[email] == password:
                return True
            print('Incorrect password!')
            return False
        print('No user account for that email!')
        return False
