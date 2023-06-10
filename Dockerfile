# Base image
FROM python:3.10.11-alpine3.17

WORKDIR /app

COPY . .

RUN pip3 install --no-cache-dir -r requirements.txt
#RUN pip3 install flask

ENV PORT=8989
EXPOSE 5000
ENV FLASK_APP=main.py
CMD flask run --host=0.0.0.0 
#CMD ["python", "main.py"]
