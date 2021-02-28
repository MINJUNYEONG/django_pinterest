FROM python:3.9.0

WORKDIR /home/

RUN echo "testing"

RUN git clone https://github.com/MINJUNYEONG/django_pinterest.git

WORKDIR /home/django_pinterest/pragmatic

RUN pip install -r requirements.txt

RUN pip install gunicorn

RUN pip install mysqlclient

RUN echo "SECRET_KEY=i4z5u1mfa+@2l%yew1thzy=1#$5ix26u-=7+geamw6!prw1$ib" > .env

RUN python manage.py collectstatic

EXPOSE 8000

CMD ["bash", "-c", "python manage.py migrate --settings=django_pinterest.pragmatic.settings.deploy && gunicorn pragmatic.wsgi --env DJANGO_SETTINGS_MODULE=django_pinterest.pragmatic.settings.deploy --bind 0.0.0.0:8000"]