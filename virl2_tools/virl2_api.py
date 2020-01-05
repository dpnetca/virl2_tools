#!/usr/bin/env

import requests
import json
import os

import urllib3

urllib3.disable_warnings()


class VIRL2API:
    def __init__(self, base_url):
        self.base_url = base_url
        self.auth_token = None

    def _api_call(self, method, uri, data={}):
        url = self.base_url + uri
        data_json = json.dumps(data)
        headers = {
            "Content-Type": "application/json",
            "accept": "application/json",
        }
        if self.auth_token:
            headers["Authorization"] = f"Bearer {self.auth_token}"
        response = requests.request(
            method, url, headers=headers, data=data_json, verify=False
        )
        return response

    def authenticate(self, username=None, password=None):
        if username is None:
            username = os.getenv("VT_ui_admin_user")
        if password is None:
            password = os.getenv("VT_ui_admin_pass")
        uri = "/authenticate"
        data = {"username": username, "password": password}
        response = self._api_call("post", uri, data)
        self.auth_token = response.text.replace('"', "")

    def get_users(self):
        uri = "/users"
        return self._api_call("get", uri)

    def get_user(self, user):
        uri = f"/users/{user}"
        return self._api_call("get", uri)

    def create_user(self, user, fullname, password, description):
        uri = f"/users/{user}"
        data = {
            "fullname": fullname,
            "password": password,
            "description": description,
        }
        return self._api_call("post", uri, data=data)
