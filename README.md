# DRM-project
 Django React Machine learning


 1. python -m venv env: create virtual environment.
 2. pip freeze: to see what are the packages using in it.
 3. source env/Scripts/activate:  to activate env.
 4. pip install django
 5. django-admin startproject django_rest_main . : start new project
 6. python manage.py runserver : to run the project port
 7. pip install djangorestframework : Django REST API framework installation
 8. Add 'rest_framework' to your INSTALLED_APPS setting.py.
 9. py manage.py startapp <APPNAME> : to create new app and register that app name in installed apps(settings.py) < then add url of that APPNAME in url to access in urls.py in main.
 10. create new file in apps folder named urls.py > then write views in app to display.
 11. API ENDPOINTS: create another app name api > do same settings as students app just change in view from http to json
 12. py manage.py migrate: to create db model > py manage.py createsuperuser
 13. you can access at <urladress>/admin to get into db. username: djangoadmin, pass: django2025
 14. now create schema in models.py(things are case sensitive,after creating do not forget to migrate and then makemigration).
 15. register the model in admin.py nd do serialization in views.py(it will get the db and show the api data).
 16. mixins
 17. generic
 18. nesteed serializers
 19. custom pagination
 20. Filter: pip install django-filter > put it in setting installed apps and can make global or custom filter like pagination in settings.py.
 21. search filter
 
Process to upload on git via terminal
1. create repo in github and copy the dire. from github web.
2. in cmd in project folder open terminal and type: git init(it will create a git folder in project folder in master terminal)
3. in command write git branch -m main(to convert into main)
4. then, git remote add origin "link which you copied"
5. then, git push -uf origin main if necessary
6. then, git add .
7. again, git commit -m "add your message"
8. git push origin main
   
10. if some modification been made then again, git add .
11. again, git commit -m "add your message"
12. git push origin main
13. if in branch change branch name git push origin <your branch name>
