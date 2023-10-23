import json


class BaseClass(object):

    def print_api_request(self, url, headers=None, payload=None):
        print(f"==================== REQUEST ===================")
        print(f"------------------ Url ----------------------")
        print(f"{url}\n")
        if headers is not None:
            print(f"\n----------------- Headers ----------------")
            print(f"{headers}\n")
        if payload is not None:
            print(f"------------- Payload -------------")
            print(json.dumps(payload, indent=2))

    def print_api_response(self, response_code, payload=None):
        print(f"==================== RESPONSE ==================")
        print(f"------------- Response Code ----------\n{response_code}")
        if payload is not None:
            print(f"------------- Response Body -------------\n")
            print(json.dumps(payload, indent=2))