# Django-Celery-FeedbackApp

Django, Celery, Redis

A simple project based on [tutorial from realpython.com](https://realpython.com/asynchronous-tasks-with-django-and-celery/)

Main Idea - made feedbackForm work asynchronous and don't freeze while message is sending (we use delay for test)

![image](https://user-images.githubusercontent.com/52755167/200572596-208cb8d3-ab09-4e65-bf2c-ff2b582062f4.png)


Extra features:

- Added Celery autoreload on changes based on Django Command:

```shell
python manage.py restartall
```
---
To start your app:

1. Create and activate a virtual environment:
```shell
$ python -m venv venv
$ source venv/bin/activate
(venv) $
```
2. Once your virtual environment is active, you can install Django:
```shell
(venv) $ python -m pip install django
```
3. Running the migrations and starting the development server:
```shell
(venv) $ python manage.py migrate
(venv) $ python manage.py runserver
```

---
Install Celery:
```shell
(venv) $ python -m pip install celery
```
Install Redis:
```shell
brew install redis \ sudo apt install redis
python -m pip install redis
```





