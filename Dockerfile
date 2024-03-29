FROM --platform=$TARGETPLATFORM python:3.11.4-alpine as build

WORKDIR /usr/src/app/

COPY . .

RUN apk add binutils && \
    pip3 install pyinstaller && \
    pip3 install -r ./requirements.txt && \
    pyinstaller -F bot.py


FROM alpine

WORKDIR /app

RUN adduser -D appuser

COPY --from=build /usr/src/app/dist .

USER appuser

CMD ["./bot"]