# Soccer Project with Django #

![image](https://user-images.githubusercontent.com/12802340/200949960-1db9bed4-56fb-4da7-a6c0-4dbd96ee7164.png)

![image](https://user-images.githubusercontent.com/12802340/200950000-711ca9d8-54b7-4029-bf2c-782cc00bd216.png)

### Installing and running ###

`$ docker-compose build --no-cache`

`$ docker-compose up -d`

`$ docker-compose run web python3 manage.py migrate`

**To acess the admin panel:**

`$ docker-compose run web python3 manage.py createsuperuser`

* **Username (leave blank to use 'root'):** admin
* **Email address:** youremail@address.com
* **Password:** password12345
* **Password (again):** password12345

**Open your browser in the address "http://localhost:8000" and enjoy the application**
