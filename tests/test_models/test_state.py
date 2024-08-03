#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.state import State


class test_state(test_basemodel):
    """ unittest for state """

    def __init__(self, *args, **kwargs):
        """ initializing state class """
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    def test_name3(self):
        """ test for state attribute """
        new = self.value()
        self.assertEqual(type(new.name), str if
                         os.getenv('HBNB_TYPE_STORAGE') != 'db' else
                         type(None))
