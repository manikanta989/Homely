from user import User
from property import Property
from ownership import Ownership
from reservation import Reservation
import uuid


class Admin:
    def __init__(self, name, email, password):
        self.a_id = str(uuid.uuid4().get_hex().upper()[0:16])
        self.name = name
        self.email = email
        self.password = password


class AdminDAO:
    def __init__(self):
        pass

    def block_user(self, user):
        pass

    def get_property_by_title(self, title):
        # returns a list of properties with specified title
        pass

    def get_property_by_zip(self, zip):
        # returns a list of properties with specified zip code
        pass

    def get_property_by_state(self, state):
        # returns a list of properties with specified state
        pass

    def get_ownership_of_property(self, property):
        # returns current ownership object of specified property
        pass

    def get_reservations_by_period(self, from_date=None, to_date=None):
        # returns a list of reservations done in the specified time period else overall.
        pass

    def get_reservations_by_zip(self, from_date=None, to_date=None):
        # returns a list of reservations done in the area with specified zip code
        # in the given time period if provided else overall
        pass

    def get_reservations_by_state(self, from_date=None, to_date=None):
        # returns a list of reservations done in specified state
        # in the given time period if provided else overall
        pass
