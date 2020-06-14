FROM python:3.8

COPY requirements.txt ./
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

WORKDIR /app

CMD ["python", "app.py"]