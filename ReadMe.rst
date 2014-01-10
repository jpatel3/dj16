- Install virtual environment 

- Create virtual env.

- Activate virtual env

- Install Django - 
	pip install Django==1.6

- django-admin.py startproject mywebapp
	- this will create the structure, you can rename the app name if you want.

- step in to mywebapp directory, and run following command -
	python manage.py runserver 8002

	It should give you instruction to run the app. run 127.0.0.1:8002

- Now time to setup the db and models
	- you can change the settings ‘DATABASE’ based on what databse you are planning to use. By default everything should be set for sqlite3
	- to setup the base db with system tabels (tables which is needed to run django site and certain basic operations) you will need to run the migration. 
	- In 1.7 migrate will be native command, if your are using >=1.6 then first you will need to install south. pip install south

	to crate table run following command - python manage.py syncdb
	It should create tables and ask you to create one account, you can leave everything blank except password.

- Now its time to create first app, lets call it post
	python manage.py startapp post

- Add the db fields you want in models.py

- to create the corresponding db you will need to again run 
	python manage.py syncdb
	This will create required tables from the models.py

