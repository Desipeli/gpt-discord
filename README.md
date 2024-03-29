A Discord bot to send and receive messages from ChatGPT, supports multiple discord servers.

# How to run with docker

pull image from [docker hub](https://hub.docker.com/repository/docker/desipeli/gpt-discord/general): `desipeli/gpt-docker`

run with envs:

- TOKEN_GPT=`<openai token>`
- TOKEN_DISCORD=`<discord bot token>`

# How to use

After connecting bot to a discord server

- `!gpt <TEXT>` Sends message to gpt, returns response
- `!gptname <NAME>` Gives name and role to ChatGPT
- `!gptsystem <DESCRIPTION>` write a description to ChatGPT
