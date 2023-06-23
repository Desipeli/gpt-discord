FROM --platform=$TARGETPLATFORM python:3.11.4-alpine

WORKDIR /usr/src/app/

RUN pip install discord openai python-dotenv

COPY . .

CMD ["python3", "bot.py"]