FROM python:3.10.0a6-buster

#make a directory
WORKDIR /app

# install dependencies
#COPY requirements.txt
#RUN pip install -r requirements.txt

# copy source code file
COPY /app .

CMD ["python", "main.py"]