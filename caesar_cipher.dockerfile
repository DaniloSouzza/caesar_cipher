FROM python:alpine3.9
WORKDIR /app
COPY caesar_cipher/requirements.txt .
RUN pip install -r requirements.txt
COPY caesar_cipher/ .
ENTRYPOINT [ "python3", "-m", "app.py" ]