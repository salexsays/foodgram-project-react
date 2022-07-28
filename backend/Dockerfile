FROM python:3.7-slim
RUN apt update && apt -y install libpq-dev build-essential
WORKDIR /app
COPY requirements.txt /app
RUN pip3 install --upgrade pip && pip3 install -r requirements.txt --no-cache-dir
COPY ./ .
ADD entrypoint.sh /entrypoint.sh
RUN chmod a+x /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]
CMD ["gunicorn", "backend.wsgi:application", "--bind", "0:8000"]
