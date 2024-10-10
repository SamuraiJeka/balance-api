FROM python:3.11
ENV POETRY_VERSION=0.1.0 PYTHONUNBUFFERED=1 PYTHONDONTWRITEBYTECODE=1

WORKDIR /usr/src/src

COPY . .

RUN pip install --upgrade pip
RUN pip install poetry
RUN poetry install 

CMD ["poetry", "run", "uvicorn", "main:app"]
