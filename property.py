import uuid


class Property:
    def __init__(self, title, address, zip, state, price):
        self.p_id = str(uuid.uuid4().get_hex().upper()[0:16])
        self.title = title
        self.address = address
        self.zip = zip
        self.state = state
        self.price = price


class PropertyDAO:

    def __init__(self):
        pass

    def create(self, property):
        # inserts 'property' data into the table
        pass

    def read(self):
        # returns list of properties from the table
        pass

    def update(self, property):
        # updates 'property' data in the table
        pass

    def delete(self, property):
        # deletes 'property' data from the table
        pass