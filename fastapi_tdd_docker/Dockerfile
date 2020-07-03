FROM python:3.8.3-slim-buster

WORKDIR /usr/src

# not writing pyc files to disc & not buffering stdout and stderr
ENV PYTHONDONTWRITEBYTECODE 1   
ENV PYTHONUNBUFFERED 1

RUN apt-get update \
    && apt-get -y install netcat gcc && apt-get clean 

RUN pip install --upgrade pip 
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . fastapi_tdd_docker/.

ENTRYPOINT ["/usr/src/fastapi_tdd_docker/entrypoint.sh"]