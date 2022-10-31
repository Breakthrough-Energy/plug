FROM ghcr.io/breakthrough-energy/postreise:latest

ENV FLASK_APP=/app/server.py
RUN pip install flask
WORKDIR /app
COPY . .
CMD ["flask", "run", "--host", "0.0.0.0"]
