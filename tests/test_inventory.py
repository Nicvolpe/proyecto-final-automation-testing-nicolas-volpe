# tests/test_inventory.py
import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

class TestInventory:

    @pytest.mark.smoke
    def test_agregar_producto_al_carrito(self, driver):
        """Verifica que se pueda agregar un producto y el contador se actualice."""
        
        # 1. Precondición: El usuario debe iniciar sesión primero
        login_page = LoginPage(driver)
        login_page.abrir().login_completo("standard_user", "secret_sauce")
        
        # 2. Instanciamos la página de inventario
        inventory_page = InventoryPage(driver)
        
        # 3. Aserción 1: Validamos que llegamos correctamente leyendo el título
        assert inventory_page.obtener_titulo() == "Products", "No se cargó la página de inventario"
        
        # 4. Acción: Agregamos el primer producto
        inventory_page.agregar_primer_producto()
        
        # 5. Aserción 2: Validamos que el icono del carrito ahora dice "1"
        assert inventory_page.obtener_contador_carrito() == 1, "El contador del carrito no se actualizó"