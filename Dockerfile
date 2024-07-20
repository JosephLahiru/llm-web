FROM python:latest

WORKDIR /app

COPY . ./

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 5004
ENTRYPOINT ["streamlit", "run", "main.py", "--server.port=5004", "--server.address=0.0.0.0"]