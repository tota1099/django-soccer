# Soccer Project with Django #

### How run ? ###

`$ docker-compose build --no-cache`

`$ docker-compose run web python3 manage.py migrate`

`$ docker-compose up -d`

**To acess the admin panel:**

`$ docker-compose run web python3 manage.py createsuperuser`

* **Username (leave blank to use 'root'):** admin
* **Email address:** youremail@address.com
* **Password:** password12345
* **Password (again):** password12345
