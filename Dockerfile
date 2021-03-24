FROM python:3.8-alpine as base

FROM base as builder

ENV PYTHONDONTWRITEBYTECODE 1

RUN apk update && apk add --update --no-cache postgresql-dev gcc python3-dev musl-dev libffi-dev openssl-dev make

RUN pip install pipenv

# creation of requirements.txt
COPY Pipfile* ./
RUN pipenv lock -r > requirements.txt

# everything else stays the same
RUN pip install --no-cache-dir -r ./requirements.txt

FROM base
RUN apk add --update --no-cache libpq
COPY --from=builder /usr/local/lib/python3.8/site-packages/ /usr/local/lib/python3.8/site-packages/
COPY --from=builder /usr/local/bin/ /usr/local/bin/

WORKDIR /code

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONPATH /code:$PYTHONPATH

COPY . ./