FROM python:3.7.4-slim-stretch
WORKDIR /djangoProject1
COPY . /djangoProject1
COPY ./requirements.txt ./
RUN pip install -r requirements.txt
ENV PORT=8000
ENV PYTHONUNBUFFERED=1
CMD python3 ./manage.py makemigrations && python ./manage.py migrate && python ./manage.py runserver 0.0.0.0:8000

//CMD [ "python3", "./manage.py makemigrations", "./manage.py migrate", "./manage.py runserver 0.0.0.0:8000" ]









