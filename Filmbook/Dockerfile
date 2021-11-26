FROM python:3.9-slim

# set work directory
WORKDIR /app

# set env variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

EXPOSE 5000

# install dependencies
COPY . .
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt


# Add flask to the environment variables
CMD ["export", "FlASK_APP=app.py"]

# make migrations
#CMD["flask", "db", "init"]
#CMD["flask", "db", "migrate"]
#CMD["flask", "db", "upgrade"]

#CMD["python", "/utils/add_users.py"]

# run gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app" ]
#CMD ["flask", "run", "--host=0.0.0.0" ]
