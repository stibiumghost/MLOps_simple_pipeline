FROM python:3.10
EXPOSE 8080
WORKDIR /app
COPY requirements.txt ./requirements.txt
RUN pip install -r requirements.txt
COPY . ./app
CMD [ "python" , "simple_app.py" ]