FROM python:alpine
LABEL authors="CharlieJ107 <charlie_j107@outlook.com>"
RUN pip install Flask
COPY . /app
ENTRYPOINT ["top", "-b"]