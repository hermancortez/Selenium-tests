from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options # Necesario para configurar Chrome

def test_page_title():


    # Configurar opciones de Chrome para ejecución en un entorno de CI/CD (headless)
    chrome_options = Options()
    chrome_options.add_argument("--headless") # Ejecuta Chrome sin interfaz gráfica (esencial para CI)
    chrome_options.add_argument("--no-sandbox") # Necesario para entornos Linux/Docker (evita problemas de permisos)
    chrome_options.add_argument("--disable-dev-shm-usage") # Para evitar problemas de memoria compartida en Docker


    try:
        driver = webdriver.Chrome(options=chrome_options)
        # Navegar a la página de GitHub
        driver.get('https://github.com')

        # Para depuración: Imprimir el título de la página (aparecerá en los logs de GitHub Actions)
        print(f"Page title is: {driver.title}")

        # Encontrar el elemento por su ID
        title_element = driver.find_element(By.ID, 'hero-section-brand-heading')

        # Realizar la aserción
        expected_text = 'Build and ship software on a single, collaborative platform'
        assert title_element.text == expected_text

    finally:
        # Siempre cierra el navegador al final para liberar recursos,
        # incluso si la prueba falla.
        driver.quit()