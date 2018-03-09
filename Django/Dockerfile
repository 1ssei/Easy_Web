 FROM python:3
 ENV PYTHONUNBUFFERED 1
 RUN mkdir /docker_config  
 ADD /docker_config/requirements.pip /docker_config/  
 RUN pip install -r /docker_config/requirements.pip
 RUN pip install django-debug-toolbar
 RUN mkdir /code
 WORKDIR /code
 ADD . /code/