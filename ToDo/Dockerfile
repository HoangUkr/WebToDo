FROM python:3.8
RUN apt-get update && apt-get -y upgrade
RUN pip install --upgrade pip
RUN mkdir -p /ToDo
ENV HOME=/ToDo
ENV APP_HOME=/ToDo/MyApp
RUN mkdir $APP_HOME
WORKDIR $HOME
COPY . $HOME
RUN pip install -r requirements.txt
CMD ["python manage.py runserver"]