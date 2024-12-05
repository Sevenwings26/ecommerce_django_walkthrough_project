## E-commerce site built with DJANGO

Python 3.10.0
Django 5.1.3

# Project Protocols
1. **Create virtual environment**
    ```Windows
        virtualenv virt
        virt\scritps\activate
    ```

2. **Install packages and commands**
   - Django: `pip install django`
   - pillow: `pip install pillow` -- To work with image!
    
    *commands*
    - Collect packages: `pip freeze > requirements.txt`
    - Start Project:    `django-admin startproject setup .`
    - Start Application: `python manage.py startapp users`
    - Make migrations: `python manage.py makemigrations`
                        `python manage.py migrate`


    fixing migration errors ---- python manage.py migrate admin --fake 
    
3. **Load templates and static files**
    Template source - Colorlib
    configure template and static files in the _settings.py_ file
    - TEMPLATES = {"DIRS": [BASE_DIR / "templates"],}   
    - STATICFILES_DIRS = [BASE_DIR / "static"]
    
    
## - Create Custome User 
    - Use email as login requirement






