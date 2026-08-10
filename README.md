# Microservicios de Usuarios y Productos

Implementación académica de una arquitectura basada en **microservicios** desarrollada para el taller de Computación en la Nube.

El proyecto utiliza **Flask, APIs REST, MySQL, SQLAlchemy, Vagrant y Consul** para implementar, gestionar y monitorear servicios independientes.

## Descripción

El proyecto parte de una aplicación web compuesta por un frontend y un microservicio para la gestión de usuarios. Como parte del taller, se desarrolla un segundo microservicio para la gestión de productos y posteriormente se incorpora **Service Discovery mediante Consul**.

La arquitectura permite separar las responsabilidades de la aplicación en servicios independientes que se comunican mediante APIs REST.

##  Arquitectura

```text
                       
 - Frontend :5001        
 -HTTP / JSON
 - microUsers :5002                 
 - microProducts: :5003

 - MySQL      
 - myflaskapp
 - users
 - products     
 
 - Consul
 - Service         
 - Discovery

```

## Tecnologías utilizadas

* **Python**
* **Flask**
* **Flask-CORS**
* **Flask-SQLAlchemy**
* **MySQL**
* **Vagrant**
* **Ubuntu 22.04**
* **REST API**
* **Consul**
* **flask-consulate**

## Estructura del proyecto

```text
microwebAppBase/
├── frontend/
│   ├── web/
│   │   ├── static/
│   │   ├── templates/
│   │   └── views.py
│   ├── config.py
│   └── run.py
│
├── microUsers/
│   ├── db/
│   │   └── db.py
│   ├── users/
│   │   ├── controllers/
│   │   │   └── user_controller.py
│   │   ├── models/
│   │   │   └── user_model.py
│   │   └── views.py
│   ├── config.py
│   └── run.py
│
├── microProducts/
│   ├── db/
│   │   └── db.py
│   ├── products/
│   │   ├── controllers/
│   │   │   └── product_controller.py
│   │   ├── models/
│   │   │   └── product_model.py
│   │   └── views.py
│   ├── config.py
│   └── run.py
│
├── README.md
├── Vagrantfile
├── init.sql
└── script.sh
```

##  Microservicio de usuarios

El microservicio `microUsers` gestiona las operaciones CRUD de los usuarios mediante una API REST.

**Puerto:** `5002`

### Endpoints

```text
GET     /api/users
GET     /api/users/<id>
POST    /api/users
PUT     /api/users/<id>
DELETE  /api/users/<id>
```

##  Microservicio de productos

El microservicio `microProducts` gestiona los productos mediante una API REST.

**Puerto:** `5003`

La tabla `products` utiliza la siguiente estructura:

```sql
CREATE TABLE products (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description VARCHAR(255),
    price DECIMAL(10,2) NOT NULL,
    stock INT NOT NULL
);
```

### Endpoints

```text
GET     /api/products
GET     /api/products/<id>
POST    /api/products
PUT     /api/products/<id>
DELETE  /api/products/<id>
```

##  Base de datos

El proyecto utiliza MySQL con la base de datos:

```text
myflaskapp
```

La base contiene las tablas:

```text
users
products
```

Los microservicios utilizan **SQLAlchemy** como ORM para interactuar con la base de datos.

##  Frontend

El frontend está desarrollado con Flask y proporciona la interfaz para gestionar los recursos de la aplicación.

**Puerto:** `5001`

El frontend se comunica con los microservicios mediante peticiones HTTP y datos en formato JSON.

```text
Frontend :5001
     │
     ├── microUsers :5002
     │
     └── microProducts :5003
```

##  Service Discovery

Como parte del taller se incorpora **Consul** para implementar el mecanismo de **Service Discovery**.

Los microservicios se registran en Consul y proporcionan un endpoint de **health check** que permite verificar su disponibilidad.

Se utiliza `flask-consulate` para facilitar la integración entre Flask y Consul.

##  Ejecución

### 1. Iniciar la máquina virtual

Desde la carpeta raíz del proyecto:

```bash
vagrant up
```

### 2. Acceder a la máquina virtual

```bash
vagrant ssh servidorWeb
```

### 3. Ejecutar el frontend

```bash
cd /home/vagrant/frontend
export FLASK_APP=run.py
/usr/local/bin/flask run --host=0.0.0.0 --port 5001
```

### 4. Ejecutar microUsers

```bash
cd /home/vagrant/microUsers
export FLASK_APP=run.py
/usr/local/bin/flask run --host=0.0.0.0 --port 5002
```

### 5. Ejecutar microProducts

```bash
cd /home/vagrant/microProducts
export FLASK_APP=run.py
/usr/local/bin/flask run --host=0.0.0.0 --port 5003
```

### 6. Ejecutar agente consul

```bash
cd /home/vagrant/
consul agent -ui -dev -bind=192.168.80.3 -client=0.0.0.0 -data-dir=.

##  Verificación

Frontend:

```text
http://192.168.80.3:5001

Consul:

```text
http://192.168.80.3:8500
```

API de usuarios:

```
http://192.168.80.3:5002/api/users
```

API de productos:

```
http://192.168.80.3:5003/api/products
```

Los endpoints permiten verificar las operaciones CRUD implementadas en cada microservicio.

##  Contexto académico

**Asignatura:** Computación en la Nube
**Proyecto:** Taller de Microservicios y Service Discovery
**Tipo:** Proyecto académico

---

##  Autores

Proyecto desarrollado como parte de las actividades académicas de Computación en la Nube por:
- *Cristian Andrés Mera*
- *Miguel Ángel Mosquera González*



