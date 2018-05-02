FROM python:3.6-stretch

WORKDIR /src

COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY . .

EXPOSE 5000

ENTRYPOINT ["python", "/src/back.py"]
