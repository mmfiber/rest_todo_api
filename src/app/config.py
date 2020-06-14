import os

class Config:
  SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://{user}:{password}@{host}/{name}".format(**{
      "user": os.getenv("DB_USER"),
      "password": os.getenv("DB_PASSWORD"),
      "host": os.getenv("DB_HOST"),
      "name": os.getenv("DB_NAME")
  })
  SQLALCHEMY_TRACK_MODIFICATIONS = False
  SQLALCHEMY_ECHO = False