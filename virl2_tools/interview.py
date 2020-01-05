#!/usr/bin/env python

# from virl2_client import virl2_client
from virl2_tools.virl2_api import VIRL2API


class Candidate:
    def __init__(self, firstname, lastname, password=None):
        self.firstname = firstname
        self.lastname = lastname
        self.password = password

    @property
    def username(self):
        return self.firstname.lower() + "." + self.lastname.lower()

    @property
    def fullname(self):
        return self.firstname + " " + self.lastname

    @property
    def firstname(self):
        return self._firstname

    @firstname.setter
    def firstname(self, name):
        self._firstname = self._validate_name("first", name)

    @property
    def lastname(self):
        return self._lastname

    @lastname.setter
    def lastname(self, name):
        self._lastname = self._validate_name("last", name)

    def _validate_name(self, name_type, name):
        if not name:
            raise ValueError(f"Candidate must have a valid {name_type} name")
        if not isinstance(name, str):
            raise ValueError(f"Canidate {name_type} must only contain letters")
        if not name.isalpha():
            raise ValueError(f"Canidate {name_type} must only contain letters")
        return name

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, password=None):
        if not password:
            # TODO replace with a password generator function
            password = "Cisco12345!"
        self._password = self._validate_password(password)

    def _validate_password(self, password):
        if not password:
            raise ValueError("Must Define a valid password")
        if not isinstance(password, str):
            raise ValueError("Password must be a string")
        return password


class Environment:
    def __init__(self, candidate):
        self.candidate = candidate
        # TODO remove hardcoded server
        self.virl2 = VIRL2API("https://192.168.118.154/api/v0")
        self.virl2.authenticate()

    def _check_if_exists(self):
        response = self.virl2.get_user(self.candidate.username)
        if response.status_code == 200:
            return True
        else:
            return False

    def create(self):
        if self._check_if_exists():
            raise RuntimeError("User Exists")
        description = f"Interview Candidate: {self.candidate.fullname}"
        response = self.virl2.create_user(
            self.candidate.username,
            self.candidate.fullname,
            self.candidate.password,
            description,
        )
        return response

    def import_topology(self, topology=None):
        pass
