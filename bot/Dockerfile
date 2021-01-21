FROM python:3.9.0-alpine AS dev-base
        WORKDIR /pie
        COPY requirements.txt ./
        RUN apk add --no-cache --virtual .build-deps gcc musl-dev \
         && pip install --no-cache-dir -r requirements.txt \
         && apk del .build-deps gcc musl-dev

FROM dev-base AS run
        COPY . .
        CMD [ "python", "./pie.py" ]
