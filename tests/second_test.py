from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options # Necesario para configurar Chrome

def test_page_title():
    # URL del Selenium Hub que se ejecuta como un servicio en GitHub Actions
    # 'localhost' se refiere al servicio 'selenium' definido en el archivo YAML del workflow
    selenium_hub_url = "http://localhost:4444/wd/hub"

    # Configurar opciones de Chrome para ejecución en un entorno de CI/CD (headless)
    chrome_options = Options()
    chrome_options.add_argument("--headless") # Ejecuta Chrome sin interfaz gráfica (esencial para CI)
    chrome_options.add_argument("--no-sandbox") # Necesario para entornos Linux/Docker (evita problemas de permisos)
    chrome_options.add_argument("--disable-dev-shm-usage") # Para evitar problemas de memoria compartida en Docker

    # Inicializar el Remote WebDriver para conectarse al Selenium Hub
    browser = webdriver.Remote(
        command_executor=selenium_hub_url,
        options=chrome_options # Pasar las opciones configuradas
    )

    try:
        # Navegar a la página de GitHub
        browser.get('https://github.com')

        # Para depuración: Imprimir el título de la página (aparecerá en los logs de GitHub Actions)
        print(f"Page title is: {browser.title}")

        # Encontrar el elemento por su ID
        title_element = browser.find_element(By.ID, 'hero-section-brand-heading')

        # Realizar la aserción
        expected_text = 'Build and ship software on a single, collaborative platform'
        assert title_element.text == expected_text

    finally:
        # Siempre cierra el navegador al final para liberar recursos,
        # incluso si la prueba falla.
        browser.quit()