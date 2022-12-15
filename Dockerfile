FROM python:3.9-alpine
COPY ./src /src
WORKDIR /src
RUN pip install poetry
RUN poetry install
CMD poetry run python src/main.py
