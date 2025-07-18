from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options # Necesario para configurar Chrome

def test_page_title():
    # Configurar opciones de Chrome para ejecución en un entorno de CI/CD.
    chrome_options = Options()
    # --headless: Ejecuta Chrome sin abrir una ventana visible. Esencial para entornos CI.
    chrome_options.add_argument("--headless")
    # --no-sandbox: Necesario para ejecutar Chrome dentro de contenedores Docker en Linux
    # para evitar problemas de permisos.
    chrome_options.add_argument("--no-sandbox")
    # --disable-dev-shm-usage: Aborda un problema común de memoria compartida en entornos Docker
    # que puede causar fallos en Chrome.
    chrome_options.add_argument("--disable-dev-shm-usage")
    # NUEVAS OPCIONES PARA RESOLVER "user data directory is already in use"
    # --incognito: Inicia Chrome en modo incógnito, lo que usa un perfil temporal y limpio.
    chrome_options.add_argument("--incognito")
    # --disable-gpu: Deshabilita el uso de la GPU. A veces necesario en entornos sin GPU.
    chrome_options.add_argument("--disable-gpu")
    # --window-size: Establece un tamaño de ventana para el navegador headless.
    chrome_options.add_argument("--window-size=1920,1080")


    # Inicializar el WebDriver.
    # Selenium Manager (integrado en Selenium 4.6+) detectará automáticamente el ChromeDriver
    # instalado por las acciones de GitHub.
    browser = webdriver.Chrome(options=chrome_options) # Pasar las opciones configuradas

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
        expected_text = 'Build and ship software on a single, collaborative platform'

        # Realizar la aserción: verificar que el texto del elemento coincide con el esperado.
        assert title_element.text == expected_text

    finally:
        # Siempre cierra el navegador al final para liberar recursos del sistema,
        # incluso si la prueba falla. Esto es una buena práctica en la automatización.
        browser.quit()