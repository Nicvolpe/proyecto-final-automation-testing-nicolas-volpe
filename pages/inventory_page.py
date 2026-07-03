# pages/inventory_page.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class InventoryPage:
    # 1. LOCATORS
    _TITLE = (By.CLASS_NAME, "title")
    _ADD_BUTTONS = (By.CSS_SELECTOR, "button[data-test*='add-to-cart']")
    _CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")

    # 2. CONSTRUCTOR
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # 3. MÉTODOS DE ACCIÓN Y LECTURA
    def obtener_titulo(self) -> str:
        """Obtiene el título de la página de inventario."""
        return self.driver.find_element(*self._TITLE).text

    def agregar_primer_producto(self):
        """Añade el primer producto disponible al carrito."""
        primer_boton = self.driver.find_elements(*self._ADD_BUTTONS)[0]
        primer_boton.click()
        return self

    def obtener_contador_carrito(self) -> int:
        """Obtiene el número de productos en el carrito."""
        try:
            badge = self.driver.find_element(*self._CART_BADGE)
            return int(badge.text)
        except:
            return 0