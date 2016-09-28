
README
======

Django blog API
----------------
A blogging application rest API.
Has API endpoint for the user to signup and login to the system.
And An API endpoint for the user to Create/Update/Delete an article.
And an API endpoint for the user to post a comment on an article

.

Steps to get started
--------------------

1.clone this repository

		$ git clone https://github.com/nagarajbhat/django_blog_api.git
2. Enter into project directory

		$ cd django_blog_api

3. (recommended but not mandatory) create a new virtualenv space to isolate django config from the rest of the system

    $ virtualenv -p python3 name_of_my_new_virtualenv
    	$ git clone https://github.com/nagarajbhat/rails_hometravel.git

4.  Install dependencies through pip

    	$ pip install -r requirements.txt

5. run migrations

		$python manage.py makemigrations
		$python manage.py migrate

6. create superuser(if necessary)

		$python3 manage.py createsuperuser

7. run server

		$python3 manage.py runserver

8. Open in web browser

		http://127.0.0.1:8000


Note:
You can reset the db using the command(provided by django-extensions):

		$ python ./manage.py reset_db --router=default


Curl tests(in cmd)
------------------

Please change the vaules if you're using the following tests:

Register:

		curl -X POST -d "username=user1&&email=user1@user1.com&&email2=user1@user1.com&&password=firstuser" http://127.0.0.1:8000/api/users/register/

Token generation:

		curl -X POST -d "username=user1&&password=firstuser" http://127.0.0.1:8000/api/auth/token

Create Article:

		curl -X POST -H "Authorization: JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE0NzQ5NDY4MjEsImVtYWlsIjoidXNlcjFAdXNlcjEuY29tIiwidXNlcl9pZCI6MiwidXNlcm5hbWUiOiJ1c2VyMSJ9.KFkWuxtizF5aPKxi87lHt7imAU_21Sigsd4KqPQPLYs" -d "title=first article&&body=this is the first article" http://127.0.0.1:8000/api/articles/create/

View/Retrieve Articles:

		curl http://127.0.0.1:8000/api/articles/

View/Retrieve Comment:

		curl  http://127.0.0.1:8000/api/articles/1/comments/

Create Comment:

		curl -X POST -H "Authorization: JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE0NzUwMDY5MTIsImVtYWlsIjoidXNlcjFAdXNlcjEuY29tIiwidXNlcl9pZCI6MSwidXNlcm5hbWUiOiJ1c2VyMSJ9.gz0wTgqc18K0hMSZW1aYDbH_y3gHj9zk7r3mCpZ8Y5g" -d "text=third comment&&article=1" http://127.0.0.1:8000/api/articles/1/comments/create/


