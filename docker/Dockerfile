FROM python:3.10 as builder
WORKDIR /app

COPY ./docker/requirements.txt /tmp
RUN python -m venv .venv && \
    ./.venv/bin/python -m pip install --no-cache-dir --upgrade pip setuptools wheel && \
    ./.venv/bin/python -m pip install --no-cache-dir -r /tmp/requirements.txt && \
    rm /tmp/requirements.txt


FROM python:3.10-slim as runner
WORKDIR /app

RUN groupadd app && useradd app -g app

COPY --from=builder /app/.venv /app/.venv
COPY ./mailer ./mailer
COPY ./config ./config

USER app
EXPOSE 8001

ENTRYPOINT ["./.venv/bin/gunicorn", "--config", "./config/gunicorn.conf.py", "mailer:app"]