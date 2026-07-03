# tests_api/test_reqres_api.py
import pytest
import requests

class TestAPI:
    # Cambiamos a JSONPlaceholder, la API oficial requerida en tu Proyecto Final
    BASE_URL = "https://jsonplaceholder.typicode.com"

    @pytest.mark.api
    def test_obtener_lista_usuarios_get(self):
        """Verifica que el endpoint GET /users retorne un status 200 y contenga datos."""
        
        # Realizar la petición GET
        respuesta = requests.get(f"{self.BASE_URL}/users")
        datos = respuesta.json()
        
        # Aserciones
        assert respuesta.status_code == 200, f"Se esperaba status 200 pero dio {respuesta.status_code}"
        assert len(datos) > 0, "La lista de usuarios está vacía"
        
        # Verificamos que el primer usuario tenga la clave email
        primer_usuario = datos[0]
        assert "email" in primer_usuario, "El usuario no tiene email"

    @pytest.mark.api
    def test_crear_usuario_post(self):
        """Verifica que el endpoint POST /users cree un registro exitosamente."""
        
        # Payload adaptado al formato de JSONPlaceholder
        payload = {
            "name": "Matias",
            "username": "QALead",
            "email": "matias@qa.com"
        }
        
        # Realizar la petición POST
        respuesta = requests.post(f"{self.BASE_URL}/users", json=payload)
        datos = respuesta.json()
        
        # Aserciones
        assert respuesta.status_code == 201, f"Falló la creación, status code: {respuesta.status_code}"
        assert datos["name"] == "Matias", "El nombre creado no coincide"
        assert "id" in datos, "La API no generó un ID para el nuevo usuario"