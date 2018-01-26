import uuid


class Reservation:
    def __init__(self, u_id, o_id, from_date, to_date, price_per_day, status):
        self.r_id = str(uuid.uuid4().get_hex().upper()[0:16])
        self.u_id = u_id
        self.o_id = o_id
        self.from_date = from_date
        self.to_date = to_date
        self.price = (to_date - from_date) * price_per_day
        self.status = status


class ReservationsDAO:
    def __init__(self):
        pass

    def create(self, reservation):
        pass

    def read(self):
        pass

    def update(self, reservation):
        pass

    def delete(self, reservation):
        pass

    def get_user_reservations(self, u_id):
        # Returns a list of reservations made by user with 'u_id'.
        pass

    def get_property_current_status(self, o_id):
        # Returns the current status of property with ownership 'o_id'
        pass

    def get_property_reservations(self, u_id):
        # Returns a list of reservations of the properties owned by user with 'u_id'
        pass

    def get_available_properties(self, from_date, to_date):
        # Returns a list of properties available for each day
        # in the period 'from_date' to 'to_date'.
        pass

    def get_nearby_properties(self, zip, from_date, to_date):
        # Returns a list of properties available for each day
        # in the period 'from_date' to 'to_date' with the
        # specified zip code.
        pass

    def get_properties_by_state(self, state, from_date, to_date):
        # Returns a list of properties available for each day
        # in the period 'from_date' to 'to_date' with in the
        # specified state
        pass