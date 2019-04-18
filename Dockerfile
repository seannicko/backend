FROM python:3.7.2

RUN mkdir -p /home
RUN mkdir -p /home/temp

WORKDIR /home

# Copying over necessary files
COPY src ./src



COPY requirements.txt ./requirements.txt


# The following is to install numpy on full linux
RUN apt-get dist-upgrade
RUN apt-get update
RUN apt-get -y install libc-dev
RUN apt-get -y install build-essential
RUN pip install -U pip

# Installing packages
RUN pip install -r ./requirements.txt

# Entrypoint
CMD ["python", "./src/main/app.py" ]