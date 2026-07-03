import pytest
import pathlib
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import logging
import os

# Configuración básica de logging
log_dir = "logs"
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

logging.basicConfig(
    filename=os.path.join(log_dir, "suite.log"),
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

# Ejemplo de uso en tus tests:
# logging.info("Iniciando el test de login")

# Definición del directorio donde se almacenarán las capturas de pantalla de fallos
target = pathlib.Path('reports/screens')
target.mkdir(parents=True, exist_ok=True)

@pytest.fixture(scope="function")
def driver():
    """Fixture que proporciona un WebDriver de Chrome configurado para cada test."""
    chrome_options = Options()
    # chrome_options.add_argument("--headless") # Descomentar para ejecuciones en CI/CD
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    
    service = Service()
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.maximize_window()
    driver.implicitly_wait(5) # Red de seguridad ante la carga de elementos
    
    yield driver
    
    # Garantiza el cierre del navegador al finalizar el test
    driver.quit()

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Detecta automáticamente si un test de UI ha fallado y captura la pantalla."""
    outcome = yield
    report = outcome.get_result()
    
    # Captura pantalla únicamente si la falla ocurre en la fase de llamada (test principal)
    if report.when == 'call' and report.failed:
        driver = item.funcargs.get('driver')
        if driver:
            file_name = target / f"{item.name}.png"
            driver.save_screenshot(str(file_name)) # Genera el archivo físico
            
            # Vincula la captura directamente al reporte de pytest-html
            if hasattr(report, 'extra'):
                report.extra.append({
                    'name': 'screenshot',
                    'format': 'image',
                    'content': str(file_name)
                })

# Modificaciones para enriquecer la tabla de resultados del reporte HTML con datos contextuales
def pytest_html_results_table_header(cells):
    """Añade la columna 'URL' en el encabezado del reporte."""
    cells.insert(2, 'URL')

def pytest_html_results_table_row(report, cells):
    """Rellena la fila correspondiente con la URL del sitio al momento del test."""
    cells.insert(2, getattr(report, 'page_url', '-'))
    
@pytest.fixture
def driver():
    chrome_options = Options()
    # Si estamos en GitHub Actions, activar headless
    if os.getenv('GITHUB_ACTIONS'):
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
    
    driver = webdriver.Chrome(options=chrome_options)
    yield driver
    driver.quit()