# pages/login_page.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    # 1. IDENTIDAD DE LA PÁGINA
    URL = "https://www.saucedemo.com/"

    # 2. LOCATORS (Privados y centralizados)
    _USER_INPUT = (By.ID, "user-name")
    _PASS_INPUT = (By.ID, "password") 
    _LOGIN_BUTTON = (By.ID, "login-button")
    _ERROR_MESSAGE = (By.CSS_SELECTOR, "[data-test='error']")

    # 3. CONSTRUCTOR
    def __init__(self, driver):
        """Recibe la instancia de WebDriver e inicializa el WebDriverWait."""
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # 4. MÉTODOS DE NAVEGACIÓN Y ACCIÓN
    def abrir(self):
        """Carga la URL de login en el navegador."""
        self.driver.get(self.URL)
        return self

    def completar_usuario(self, usuario: str):
        """Limpia y escribe el nombre de usuario."""
        campo = self.wait.until(EC.visibility_of_element_located(self._USER_INPUT))
        campo.clear()
        campo.send_keys(usuario)
        return self

    def completar_clave(self, clave: str):
        """Limpia y escribe la contraseña."""
        campo = self.driver.find_element(*self._PASS_INPUT)
        campo.clear()
        campo.send_keys(clave)
        return self 

    def hacer_clic_login(self):
        """Hace clic en el botón Login."""
        self.driver.find_element(*self._LOGIN_BUTTON).click()
        return self

    def login_completo(self, usuario: str, clave: str):
        """Método de conveniencia para realizar un flujo de login completo."""
        self.completar_usuario(usuario)
        self.completar_clave(clave) 
        self.hacer_clic_login() 
        return self

    # 5. HELPERS DE VERIFICACIÓN (Sin aserciones internas)
    def esta_error_visible(self) -> bool:
        """Comprueba si aparece un mensaje de error tras un intento fallido."""
        try:
            self.wait.until(EC.visibility_of_element_located(self._ERROR_MESSAGE))
            return True
        except:
            return False

    def obtener_mensaje_error(self) -> str:
        """Obtiene el texto del mensaje de error si está visible."""
        if self.esta_error_visible():
            return self.driver.find_element(*self._ERROR_MESSAGE).text
        return ""