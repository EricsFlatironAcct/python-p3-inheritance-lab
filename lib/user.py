#!/usr/bin/env python

class User:
    def __init__(self, first_name="", last_name=""):
        self.set_first_name(first_name)
        self.set_last_name(last_name)
    
    def set_first_name(self, first_name):
        self._first_name= first_name

    def set_last_name(self, last_name):
        self._last_name= last_name
    
    def get_first_name(self):
        return self._first_name
    
    def get_last_name(self):
        return self._last_name

    first_name = property(get_first_name, set_first_name)
    last_name = property(get_last_name, set_last_name)