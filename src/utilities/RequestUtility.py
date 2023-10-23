import json
import requests


class RequestUtility:

    def __int__(self):
        pass

    @staticmethod
    def get(url, headers=None, credentials=None, payload=None):
        response = requests.request("GET", url=url, headers=headers, auth=credentials, data=payload)
        return response

    @staticmethod
    def post(url, headers=None, credentials=None, payload=None):
        payload = json.dumps(payload)
        response = requests.request("POST", url=url, headers=headers, auth=credentials, data=payload)
        return response

    @staticmethod
    def put(url, headers=None, credentials=None, payload=None):
        payload = json.dumps(payload)
        response = requests.request("PUT", url=url, headers=headers, auth=credentials, data=payload)
        return response

    @staticmethod
    def delete(url, headers=None, credentials=None, payload=None):
        response = requests.request("DELETE", url=url, headers=headers, auth=credentials, data=payload)
        return response