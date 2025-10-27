# Automatización QA para SauceDemo

## Propósito del proyecto
Automatizar flujos básicos del sitio de pruebas [saucedemo.com](https://www.saucedemo.com) como parte de una pre-entrega del curso de Automatización QA. Las pruebas cubren el inicio de sesión, la navegación por el inventario y las operaciones simples del carrito para validar la experiencia de usuario.

## Tecnologías utilizadas
- Python 3.11+
- Selenium WebDriver
- Pytest
- webdriver-manager
- pytest-html (reporte en formato HTML)
- Google Chrome / Chromium como navegador de ejecución

## Instalación de dependencias
1. Crea y activa un entorno virtual (opcional pero recomendado).
2. Instala las dependencias necesarias:
   ```bash
   pip install -r requirements.txt
   ```
   Si no cuentas con un archivo `requirements.txt`, instala los paquetes manualmente:
   ```bash
   pip install selenium pytest webdriver-manager pytest-html
   ```

## Ejecución de pruebas
Ejecuta la suite completa y genera un reporte HTML autocontenido con el siguiente comando:
```bash
pytest -v --html=report.html --self-contained-html
```
También puedes utilizar el script auxiliar incluido:
```bash
python run_test.py
```
