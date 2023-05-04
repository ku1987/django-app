FROM python:3

WORKDIR /django

COPY requirements.txt /django/
RUN pip install -r requirements.txt

COPY . /django/

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
