FROM python:3.12-alpine AS dev
WORKDIR /app
COPY requirements.txt requirements.txt
RUN apk add git \
    && apk add openssh \
    gcc \
    musl-dev \
    linux-headers \
    python3-dev \
    && pip install --no-cache-dir --upgrade -r requirements.txt
CMD ["sh"]