FROM python:3.9
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/
EXPOSE  7000
CMD python manage.py makemigrations && python manage.py migrate && python manage.py runserver 0.0.0.0:7000