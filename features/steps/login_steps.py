from behave import given, when, then
from pages.login_page import LoginPage

@given('que el usuario esta en la pagina de login')
def step_impl(context):
    context.login_page = LoginPage(context.driver)
    context.login_page.abrir()

@when('ingresa el usuario "{usuario}" y la clave "{clave}"')
def step_impl(context, usuario, clave):
    context.login_page.login_completo(usuario, clave)

@then('deberia ser redirigido a la pagina de inventario')
def step_impl(context):
    assert "inventory.html" in context.driver.current_url