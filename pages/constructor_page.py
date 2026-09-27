from pages.base_page import BasePage
from locators import ConstructorPageLocators


class ConstructorPage(BasePage):
    def open_constructor(self):
        self.open("/")

    def get_ingredient_items(self):
        return self.find_elements(ConstructorPageLocators.INGREDIENT_ITEMS)

    def click_first_ingredient(self):
        ingredients = self.get_ingredient_items()
        if ingredients:
            ingredients[0].click()

    def is_ingredient_modal_open(self):
        try:
            self.find_element(ConstructorPageLocators.INGREDIENT_MODAL, timeout=5)
            return True
        except:
            return False

    def close_ingredient_modal(self):
        self.click_element(ConstructorPageLocators.INGREDIENT_MODAL_CLOSE)