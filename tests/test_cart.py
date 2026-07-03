# tests/test_cart.py
import pytest
from selenium.webdriver.common.by import By
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage

class TestCart:

    @pytest.mark.smoke
    def test_verificar_productos_en_carrito(self, driver):
        """Verifica que un producto agregado desde el inventario aparezca en el carrito."""
        
        # 1. Precondición: Login exitoso
        login_page = LoginPage(driver)
        login_page.abrir().login_completo("standard_user", "secret_sauce")
        
        # 2. Agregar un producto
        inventory_page = InventoryPage(driver)
        inventory_page.agregar_primer_producto()
        
        # 3. Navegar al carrito haciendo clic en el ícono
        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        
        # 4. Instanciar la página del carrito (el constructor validará que llegamos a cart.html)
        cart_page = CartPage(driver)
        
        # 5. Aserción 1: Verificamos que la lista de elementos en el carrito no esté vacía
        productos = cart_page.obtener_productos_en_carrito()
        assert len(productos) > 0, "El carrito aparece vacío, pero debería tener 1 producto."
        
        # 6. Aserción 2: Verificamos que se capturó el nombre del producto
        nombres = cart_page.obtener_nombres_productos()
        assert len(nombres) == 1, f"Se esperaban 1 producto, pero se encontraron {len(nombres)}."
        
        # 7. Limpieza/Acción final: Volver al inventario
        cart_page.continuar_comprando()
        assert "inventory.html" in driver.current_url, "No se regresó al inventario tras hacer clic en Continue Shopping."