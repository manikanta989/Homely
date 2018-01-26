import uuid


class User:
    def __init__(self, name, password, email, mobile):
        self.u_id = str(uuid.uuid4().get_hex().upper()[0:16])
        self.name = name
        self.password = password
        self.email = email
        self.mobile = mobile
        self.blocked = False


class UserDAO:
    def __init__(self):
        pass

    def create(self, user):
        # inserts 'user' data into the table
        pass

    def read(self):
        # returns list of users from the table
        pass

    def update(self, user):
        # updates the 'user' data in the table
        pass

    def delete(self, user):
        # deletes the 'user' data from the table
        pass

    def get_user_by_email(self, email):
        # Returns user with specified email
        pass

    def get_user_by_mobile(self, mobile):
        # Returns user with specified mobile
        pass