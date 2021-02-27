FROM python:3.9.0

WORKDIR /home/

RUN git clone https://github.com/MINJUNYEONG/django_pinterest.git

WORKDIR /home/pragmatic/

RUN pip install -r requirements.txt

RUN python manage.py migrate

EXPOSE 8000

CMD ["python", "mange.py", "runserver", "0.0.0.0:8000"]