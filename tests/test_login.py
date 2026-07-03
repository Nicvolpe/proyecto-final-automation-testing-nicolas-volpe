# tests/test_login.py
import pytest
import json
import os
from pages.login_page import LoginPage

# Función auxiliar para leer el JSON
def cargar_datos_usuarios():
    ruta_archivo = os.path.join(os.path.dirname(__file__), '..', 'data', 'users.json')
    with open(ruta_archivo, 'r') as archivo:
        return json.load(archivo)

class TestLogin:

    @pytest.mark.parametrize("datos", cargar_datos_usuarios())
    def test_login_dinamico(self, driver, datos):
        """Verifica el login con múltiples sets de datos desde un JSON."""
        
        # Extraemos los datos del diccionario actual
        usuario = datos["usuario"]
        clave = datos["clave"]
        resultado = datos["resultado_esperado"]

        login_page = LoginPage(driver)
        login_page.abrir().login_completo(usuario, clave)

        # Evaluamos el resultado dinámicamente
        if resultado == "exito":
            assert "inventory.html" in driver.current_url, f"Falló el login exitoso para el usuario {usuario}"
        elif resultado == "bloqueado":
            assert login_page.esta_error_visible(), "No se mostró el error para el usuario bloqueado"
            assert "locked out" in login_page.obtener_mensaje_error(), "El mensaje de bloqueo no es el esperado"
        elif resultado == "error":
            assert login_page.esta_error_visible(), "No se mostró el error para credenciales inválidas"
            assert "Epic sadface" in login_page.obtener_mensaje_error(), "El mensaje de error general no es el esperado"