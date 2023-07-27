# Aromas a Tierra
<p align="center">
  <img src="Logo.png" alt="Logo de Aromas a Tierra" style="width: 30%; max-width: 200px;">
</p>
<h5 align="center">Aromas a Tierra: El mejor café</h5>

Aromas a Tierr es un proyecto de una página web desarrollado en Django, que ofrece una experiencia completa de uso tanto para el administrador como para el usuario. Todo en un sitio web intuitivo y fácil de usar.

## ¿En qué consiste?

Este proyecto desarrollado en Django cuenta con un entorno virtual se ha configurado cuidadosamente para asegurar una experiencia de desarrollo óptima y segura. La tecnología utilizada incluye Python, JavaScript, HTML, Bootstrap/CSS, MySQL y demás tecnologías. Cuenta con un blog, contacto, web son dinámicas y ofrecen una experiencia interactiva a los usuarios.

## Ejecución 

Es necesario tener instalado los requerimientos necesarios para ejecutarlo posteriormente con `python manage.py runserver` desde la terminal en el directorio de la carpeta clonada. Una vez realizado es necesario abrir localhost:8000 para visualizar el sistema.

### Instalación

Para poder utilizar el proyecto o modificarlo puedes:

1.- **Clonar el repositorio en tu máquina local:**
`git clone https://github.com/Nivaniz/web-cafeteria.git`
*(Hay que tener todos los requerimientos previamente instalados)*

2.- **Crea un entorno virtual e instala las dependencias necesarias.**

3.- **Configura la base de datos y realiza las migraciones.**

4.- **Ejecuta el servidor de desarrollo de Django.**

5.- **Navegar en el directorio del proyecto:**
`cd webempresa`

6.- **Instalar las dependencias necesarias:**
`pip install -r requirements.txt`

~~~
git clone https://github.com/tu-usuario/web-cafeteria.git
cd web-cafeteria
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
~~~

## Uso y cómo acceder al administrador

Para acceder al área de administración, sigue los siguientes pasos:

El sistema mediante el cual se maneja con localhost:8000/admin, para poder acceder a la ventana de administrador necesitas crear una cuenta desde la CMD o BASH utilizando `winpty python manage.py createsuperuser` para crear super usuario.

## Notas

Por cuestiones de seguridad, es necesario que si quieres utilizarlo insertes tus credenciales necesarias para el correcto funcionamiento de la página accediendo a settings con contraseñas de acceso de los servicios de google gmail.

## Autoría

¡Tus contribuciones son bienvenidas! Si encuentras errores o mejoras para el proyecto, no dudes en enviar tus pull requests. Si tienes alguna pregunta o comentario, puedes encontrarme y visitar mi sitio web https://codingwithnirvana.pythonanywhere.com.

Espero que esta versión del README sea útil.
Creado por **Nirvana Belen González López** 
