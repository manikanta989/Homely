import uuid


class Ownership:
    def __init__(self, u_id, p_id):
        self.o_id = str(uuid.uuid4().get_hex().upper()[0:16])
        self.u_id = u_id
        self.p_id = p_id


class OwnershipsDAO:
    def __init__(self):
        pass

    def create(self, ownership):
        # inserts the 'ownership' data into the table
        pass

    def read(self):
        # returns all ownerships from the table
        pass

    def update(self, ownership):
        # updates the 'ownership' data in the table
        pass

    def delete(self, ownership):
        # deletes the 'ownership' data from the table
        pass

    def get_owned_properties(self, u_id):
        # Returns a list of properties with owned by user with 'u_id'
        pass