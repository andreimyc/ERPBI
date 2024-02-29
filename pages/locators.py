from selenium.webdriver.common.by import By


class AuthorizationPageLocators():
    LOGIN_FIELD = (By.CSS_SELECTOR, "#input-29")
    PASSWORD_FIELD = (By.CSS_SELECTOR, "#input-33")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "#app > div > main > div > div > div > div > div.v-card__text > form > div > button")
