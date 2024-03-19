FROM python:alpine
LABEL authors="CharlieJ107 <charlie_j107@outlook.com>"
COPY . /app
WORKDIR /app
RUN python -m pip install --no-cache-dir -r  requirements.txt
EXPOSE 80
CMD python -m gunicorn -w 4 -b 0.0.0.0:80 app:app