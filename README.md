1. Primero se creó una carpeta principal en la computadora (denominada 
   "ejercicio_clientes") y se abrió directamente dentro de 
   Visual Studio Code.

2. Construir el entorno virtual (venv):
   En la terminal 
   se ejecutó el comando:
   
   python -m venv venv

3. Activar el entorno virtual:
   Antes de instalar herramientas, se activó el entorno para asegurar que 
   todo se configure de manera local.

4. Instalar las herramientas clave:
   Con el entorno activo, se instaló el framework principal (FastAPI) 
   
   pip install fastapi [stadard]

Una vez preparado el entorno, se crearon los archivos base que aparecen 
en la raíz del explorador de VS Code:

1. El archivo principal 'main.py':
 
   * Línea 1: Se importó el módulo 'FastAPI'.
   * Línea 4: Se creó la instancia principal de la aplicación: app = FastAPI()
   * Líneas 5-7: Se programó la ruta de inicio ('/'). Cuando alguien accede, 
     la API responde: {"mensaje": "Este es el proyecto de clientes a desarrollar"}.
   * Líneas 9-12: Se creó la ruta '/clientes'. Se definió una lista interna 
     con 5 clientes ficticios ("cliente1", "cliente2", etc.) y se configuró 
     el endpoint para retornar esa lista.

Para encender la API y validar el código escrito, se siguen estos pasos:

1. Para poder tener el servidor de el proyecto:
   En la terminal integrada de VS Code se ejecuta:
   
    fastapi dev main.py
   
2. Verificar los resultados en el navegador:
   * Al ingresar a: http://127.0.0.1:8000/ se visualiza el mensaje de bienvenida.
   * Al ingresar a: http://127.0.0.1:8000/clientes se obtiene la lista de los 5 clientes.

3. Explorar la documentación :
   FastAPI genera documentación de forma automática. Al ingresar a la dirección 
   http://127.0.0.1:8000/docs se abre una interfaz gráfica interactiva que 
   permite probar todas las rutas creadas sin escribir código adicional.
