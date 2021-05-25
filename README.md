# **Webshop**

- [**Webshop**](#webshop)
  - [**General info**](#general-info)
    - [**Buit with**](#buit-with)
    - [**Installation**](#installation)
  - [**Usage**](#usage)
    - [**Important commands**](#important-commands)


## **General info**
![Generic badge](https://img.shields.io/badge/Python-3.9-blue.svg)
![Generic badge](https://img.shields.io/badge/Django-3.2.1-blue.svg)
![Generic badge](https://img.shields.io/badge/License-MIT-green.svg)

This project is an example of a webshop made with django with connection to MySql database. Shop have implemented systems of:

* Users system
* Creating products
* Buy and sell dashboard
* Searching
* Cart & checkout
* Product and user rating
* And few more...

### **Buit with**
To build this project I used following framowrks:
* Django
* Boostrap
* JQuery

I also used *MySql* database and *SCSS* preprocessor. For the virtual environment I have chosen *pipenv*. To make forms making I used *django crispy forms*.

### **Installation**

<details>
<summary>Using pipenv</summary>

1. Clone repository - `git clone https://github.com/makubas/webshop-django`
2. Enter project directory - `cd webshop-django `
3. Create virtual environment - `pipenv install -r requirements.txt`
4. Run it - `pipenv shell`
5. Create databases for the project - `python manage.py migrate`
6. Run server - `python manage.py runserver`

</details>
<details>
<summary>Using docker</summary>

1. Clone repository - `git clone https://github.com/makubas/webshop-django`
2. Enter project directory - `cd webshop-django`
3. Open the settings.py file under `/webshop` and change `DATABASES/default/host from 'localhost' to 'db'`
4. Build docker services - `docker-compose build`
5. Create database - `docker-compose up -d db`
6. Run server - `docker-compose up web`

</details>

---

## **Usage**
If you made everything correctly you should see the message that the server is running and you can connect on `localhost:8000`.

After you are see that server is working, register your new account and check out how this works!

If you want to make multiple things at once, run those commands:

### **Important commands**
* `py manage.py createuser <amount>` -> Create user(s), it'll return each user email and password.
* `py manage.py createproduct <amount>` -> This will create user (seller) of the product(s), and than create given amount of random items.

