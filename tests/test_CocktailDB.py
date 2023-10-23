import pytest
import pytest_check as check
from src.BaseClass import BaseClass
from src.api.CocktailDBServiceMethods import CocktailDBServiceMethods


class TestCocktailDB(BaseClass):
    cocktail_db_svc = CocktailDBServiceMethods()

    @pytest.mark.INGREDIENTS
    def test_search_ingredient_by_valid_name(self):
        ingredient_name = "vodka"
        ingredients_by_name = self.cocktail_db_svc.search_ingredients_by_name(ingredient_name)

        # Extract values
        ingredient_list = ingredients_by_name["ingredients"]

        # Do validations
        for elem in ingredient_list:
            tmp_ingredient_name = elem["strIngredient"]
            print(f"\nValidate Ingredient Name: \nExpected: {ingredient_name.lower()} \nActual: "
                  f"{tmp_ingredient_name.lower()}")
            check.equal(tmp_ingredient_name.lower(), ingredient_name.lower(), f"Expected ingredient name to be "
                                                                              f"'{ingredient_name}', but found "
                                                                              f"'{tmp_ingredient_name}'")

    @pytest.mark.INGREDIENTS
    def test_search_mis_spelled_ingredients(self):
        ingredient_name = "vodta"
        mis_spelled_ingredients = self.cocktail_db_svc.search_ingredients_by_name(ingredient_name)

        # Extract values
        ingredient_list = mis_spelled_ingredients["ingredients"]

        # Do validations
        print(f"\nValidate Mis-spelled Ingredient: \nExpected: {None} \nActual: {ingredient_list}")
        check.equal(ingredient_list, None, f"Expected ingredient_list to be null, but found '{ingredient_list}'")

    @pytest.mark.INGREDIENTS
    def test_search_ingredients_without_name(self):
        ingredient_name = ""
        ingredients_without_name = self.cocktail_db_svc.search_ingredients_by_name(ingredient_name)

        # Extract values
        ingredient_list = ingredients_without_name["ingredients"]

        # Do validations
        print(f"\nValidate Ingredient List: \nExpected: {None} \nActual: {ingredient_list}")
        check.equal(ingredient_list, None, f"Expected ingredient_list to be null, but found '{ingredient_list}'")

    @pytest.mark.INGREDIENTS
    def test_search_non_alcoholic_ingredient_name(self):
        ingredient_name = "cucumber"
        non_alcoholic_ingredient = self.cocktail_db_svc.search_ingredients_by_name(ingredient_name)

        # Extract values
        alcohol = non_alcoholic_ingredient["ingredients"][0]["strAlcohol"]
        abv = non_alcoholic_ingredient["ingredients"][0]["strABV"]

        # Do validations
        print(f"\nValidate Alcohol: \nExpected: No \nActual: {alcohol}")
        check.equal(alcohol, "No", f"Expected Alcohol to be 'No' but found '{alcohol}'")

        print(f"\nValidate ABV: \nExpected: {None} \nActual: {abv}")
        check.equal(abv, None, f"Expected ABV to be '{None}', but found '{abv}'")

    @pytest.mark.COCKTAILS
    def test_valid_cocktail_name(self):
        cocktail_name = "negroni"
        cocktails_by_name = self.cocktail_db_svc.search_cocktails_by_name(cocktail_name)

        # Extract values
        cocktail_list = cocktails_by_name["drinks"]

        # Do validations
        for elem in cocktail_list:
            tmp_cocktail_name = elem["strDrink"]
            print(f"\nValidate Cocktail Name: \nExpected to contain {cocktail_name} \nActual: {tmp_cocktail_name}")
            check.is_true(cocktail_name.lower() in tmp_cocktail_name.lower(), f"Expected '{tmp_cocktail_name}' to "
                                                                              f"contain '{cocktail_name}'")

    @pytest.mark.COCKTAILS
    def test_mis_spelled_cocktail_name(self):
        cocktail_name = "majito"
        cocktails_by_name = self.cocktail_db_svc.search_cocktails_by_name(cocktail_name)

        # Extract values
        cocktail_list = cocktails_by_name["drinks"]

        # Do validations
        print(f"\nValidate Mis-spelled Cocktail: \nExpected: {None} \nActual: {cocktail_list}")
        check.equal(cocktail_list, None, f"Expected cocktail list to be '{None}', but found '{cocktail_list}'")

    @pytest.mark.COCKTAILS
    def test_search_cocktail_without_name(self):
        cocktail_name = ""
        cocktails_without_name = self.cocktail_db_svc.search_cocktails_by_name(cocktail_name)

        # Extract values
        cocktail_list = cocktails_without_name["drinks"]

        # Do validations
        print(f"\nValidate Cocktail List: \nExpected: {None} \nActual: {cocktail_list}")
        check.equal(cocktail_list, None, f"Expected cocktail_list to be null, but found {cocktail_list}")

    @pytest.mark.COCKTAILS
    def test_search_cocktails_in_all_caps(self):
        cocktail_name = "MOJITO"
        cocktails_all_caps = self.cocktail_db_svc.search_cocktails_by_name(cocktail_name)

        # Extract values
        cocktail_list = cocktails_all_caps["drinks"]

        # Do validations
        for elem in cocktail_list:
            tmp_cocktail_name = elem["strDrink"]
            print(f"\nValidate All Caps Cocktail Name: \nExpected cocktail name to contain '{cocktail_name.title()}'"
                  f"\nActual: '{tmp_cocktail_name}'")
            check.is_true(cocktail_name.title() in tmp_cocktail_name, f"Expected '{tmp_cocktail_name}' to contain "
                                                                      f"'{cocktail_name.title()}'")

    @pytest.mark.INGREDIENTS
    @pytest.mark.EXTRA
    def test_lookup_ingredient_by_id(self):
        ingredient_id = "552"
        expected_ingredient_name = "Elderflower cordial"
        ingredient_by_id = self.cocktail_db_svc.lookup_ingredient_by_id(ingredient_id)

        # Extract values
        actual_ingredient_id = ingredient_by_id["ingredients"][0]["idIngredient"]
        actual_ingredient_name = ingredient_by_id["ingredients"][0]["strIngredient"]

        # Do validation
        print(f"\nValidate Ingredient Id: \nExpected: {ingredient_id} \nActual: {actual_ingredient_id}")
        check.equal(ingredient_id, actual_ingredient_id, f"Expected ingredient_id to be {ingredient_id}, but found "
                                                         f"{actual_ingredient_id}")

        print(f"\nValidate Ingredient Name: \nExpected: {expected_ingredient_name} \nActual: {actual_ingredient_name}")
        check.equal(expected_ingredient_name, actual_ingredient_name, f"Expected ingredient_name to be "
                                                                      f"'{expected_ingredient_name}', but found "
                                                                      f"'{actual_ingredient_name}'")

    @pytest.mark.COCKTAILS
    @pytest.mark.EXTRA
    def test_list_cocktails_by_1st_letter(self):
        first_letter = "C"
        cocktails_by_1st_letter = self.cocktail_db_svc.list_cocktails_by_1st_letter(first_letter)

        # Extract values
        cocktail_list = cocktails_by_1st_letter["drinks"]

        # Do validations
        for elem in cocktail_list:
            tmp_cocktail_name = elem["strDrink"]
            print(f"\nValidate Cocktail Name: \nExpected '{tmp_cocktail_name}' starts with '{first_letter.upper()}'")
            check.equal(tmp_cocktail_name[0].upper(), first_letter.upper(), f"Expected '{tmp_cocktail_name}' starts "
                                                                            f"with '{first_letter.upper()}'")

