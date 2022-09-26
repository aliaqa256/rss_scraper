FROM python:3.10
ENV PYTHONUNBUFFERED=1

WORKDIR /rss-scraper

COPY requirements.txt /ninjafits-back/

RUN pip install pip
RUN pip install -r requirements.txt

COPY . /ninjafits-back/

EXPOSE 8000
RUN python manage.py collectstatic --no-input

CMD ["gunicorn", "config.wsgi", ":8000"]

# CMD ["daphne","config.routing:application"]