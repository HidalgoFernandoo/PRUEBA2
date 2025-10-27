
def test_login_redirects_to_inventory(login_in_driver):
    driver = login_in_driver

    # Confirm that the login flow lands on the inventory page.
    assert "/inventory.html" in driver.current_url, "La redirección posterior al login es incorrecta"

    # El título confirma que la vista de inventario está activa.
    assert driver.title == "Swag Labs"
