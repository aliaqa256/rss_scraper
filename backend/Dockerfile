FROM python:3.9
ENV PYTHONUNBUFFERED=1

WORKDIR /backend

COPY requirements.txt /backend/

RUN pip install pip
RUN pip install -r requirements.txt

COPY . /backend/

EXPOSE 8000
# RUN python manage.py collectstatic --no-input

CMD ["gunicorn", "config.wsgi", ":8000"]

# CMD ["daphne","config.routing:application"]