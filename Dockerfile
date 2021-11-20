FROM python:3.7.4-slim-stretch
WORKDIR /djangoProject1
COPY . /djangoProject1
COPY ./requirements.txt ./
RUN pip install -r requirements.txt
ENV PORT=5000
ENV PYTHONUNBUFFERED=1
CMD [ "python3", "./manage.py", "runserver", "0.0.0.0:8000" ]








