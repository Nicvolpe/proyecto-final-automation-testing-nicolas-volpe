from selenium import webdriver

def before_all(context):
    # Aquí puedes integrar tu fixture de conftest si lo prefieres
    context.driver = webdriver.Chrome()
    context.driver.implicitly_wait(10)

def after_all(context):
    context.driver.quit()