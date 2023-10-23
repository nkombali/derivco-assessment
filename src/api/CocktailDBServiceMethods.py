from src.BaseClass import BaseClass
import pytest_check as check
from src.config.url_config import COCKTAIL_SVC
from src.utilities.RequestUtility import RequestUtility


class CocktailDBServiceMethods(BaseClass):

    def __init__(self):
        self.headers = {"Content-Type": "application/json"}

    def search_ingredients_by_name(self, name):
        url = COCKTAIL_SVC["host"] + COCKTAIL_SVC["search_ingredients_by_name"] + name
        self.print_api_request(url, self.headers)
        response = RequestUtility.get(url, self.headers)
        check.equal(200, response.status_code, f"Expected status code to be 200, but found {response.status_code}")

        if response.status_code == 200:
            response_json = response.json()
            self.print_api_response(response.status_code, response_json)
            return response_json

    def search_cocktails_by_name(self, name):
        url = COCKTAIL_SVC["host"] + COCKTAIL_SVC["search_cocktails_by_name"] + name
        self.print_api_request(url, self.headers)
        response = RequestUtility.get(url, self.headers)
        check.equal(200, response.status_code, f"Expected status code to be 200, but found {response.status_code}")

        if response.status_code == 200:
            response_json = response.json()
            self.print_api_response(response.status_code, response_json)
            return response_json

    def lookup_ingredient_by_id(self, id):
        url = COCKTAIL_SVC["host"] + COCKTAIL_SVC["lookup_ingredient_by_id"] + id
        self.print_api_request(url, self.headers)
        response = RequestUtility.get(url, self.headers)
        check.equal(200, response.status_code, f"Expected status code to be 200, but found {response.status_code}")

        if response.status_code == 200:
            response_json = response.json()
            self.print_api_response(response.status_code, response_json)
            return response_json

    def list_cocktails_by_1st_letter(self, first_letter):
        url = COCKTAIL_SVC["host"] + COCKTAIL_SVC["list_cocktails_by_1st_letter"] + first_letter
        self.print_api_request(url, self.headers)
        response = RequestUtility.get(url, self.headers)
        check.equal(200, response.status_code, f"Expected status code to be 200, but found {response.status_code}")

        if response.status_code == 200:
            response_json = response.json()
            self.print_api_response(response.status_code, response_json)
            return response_json
