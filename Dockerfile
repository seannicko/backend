FROM python:3.7.2-alpine

RUN mkdir -p /home

WORKDIR /home

# Copying over necessary files
COPY src ./src

COPY requirements.txt ./requirements.txt

RUN pip install -U pip

# Installing packages
RUN pip install -r ./requirements.txt

# Entrypoint
CMD ["python", "./src/main/app.py" ]