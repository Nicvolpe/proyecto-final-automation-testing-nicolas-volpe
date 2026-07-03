Feature: Login en SauceDemo

  Scenario: Login exitoso con credenciales validas
    Given que el usuario esta en la pagina de login
    When ingresa el usuario "standard_user" y la clave "secret_sauce"
    Then deberia ser redirigido a la pagina de inventario