# Document for setting up project

## 1. Install OS

- Linux is required (Ubuntu Desktop/Server 16.04)

## 2. Install needed packages

- Python3.5/3.6 and python virtual environment
```
python3.5
python3.5-venv
```

- Install database (Postgresql version 9 or later)

- Install Git (Source code management tool)

## 3. Initialize Project Environment

- Create python3.5 venv folder (this is only environment of the project)


`if app is running on python2.* environment`

 replace **$ python3.5 -m venv crm/** by **$ virtualenv folder_name**

```
$ cd ~/Documents/workspace/
$ mkdir crm
$ python3.5 -m venv crm/
$ cd crm/
$ source bin/activate
```

- Create or clone project into "repo" directory
```
$ git clone http://xxx.com/cuongnc/... .git repo
```

- 2 more required libraries (GonrinJS lib & GonrinUI)
```
$ cd ./repo/static/js
$ git clone https://github.com/gonrin/... .git lib
$ cd ../vendor
$ git clone https://github.com/gonrin/... .git
```

## 4. Run project

- Before running app, need to create database postgresql user to access db

- Go to repo directory to run app
```
$ cd ../../
$ pip install -r requirements.txt
$ python manage.py run
```
