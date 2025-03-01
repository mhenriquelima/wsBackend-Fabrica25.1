FROM python

WORKDIR /app

RUN apt-get update && apt-get install -y git

COPY requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

EXPOSE 8000

ENV PYTHONUNBUFFERED=1
ENV DJANGO_SETTINGS_MODULE=project.settings

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]