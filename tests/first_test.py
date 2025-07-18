from selenium import webdriver
from selenium.webdriver.common.by import By
# Ya no necesitamos Options ni Service si Selenium Manager gestiona el driver localmente
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.chrome.service import Service

def test_page_title():
    # Con el nuevo pytest.yml, Chrome y ChromeDriver se instalan directamente en el runner.
    # Selenium Manager (integrado en Selenium 4.6+) detectará automáticamente el ChromeDriver.
    # Por lo tanto, no necesitamos especificar un Service local ni un Remote WebDriver.
    browser = webdriver.Chrome()

    try:
        # Navegar a la página de GitHub
        browser.get('https://github.com')

        # Para depuración: Imprimir el título de la página.
        # Esta salida aparecerá en los logs de GitHub Actions.
        print(f"Page title is: {browser.title}")

        # Encontrar el elemento por su ID.
        # Asegúrate de que el ID 'hero-section-brand-heading' sigue siendo válido en la página de GitHub.
        title_element = browser.find_element(By.ID, 'hero-section-brand-heading')

        # Definir el texto esperado.
        # Se eliminó el punto final para que coincida con el texto real del elemento.
        expected_text = 'Build and ship software on a single, collaborative platform'

        # Realizar la aserción: verificar que el texto del elemento coincide con el esperado.
        assert title_element.text == expected_text

    finally:
        # Siempre cierra el navegador al final para liberar recursos del sistema,
        # incluso si la prueba falla. Esto es una buena práctica en la automatización.
        browser.quit()