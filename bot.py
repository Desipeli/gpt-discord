from config import TOKEN_DISCORD, TOKEN_GPT
import discord
from discord.ext import commands
from chat_gpt import ChatGPT
from chat_gpt import MODELS

class Bot:
    def __init__(self) -> None:
        intents = discord.Intents.default()
        intents.message_content = True
        intents.members = True
        self.bot = commands.Bot(command_prefix="!", intents=intents)
        self.gpt = ChatGPT(
            TOKEN_GPT,
            MODELS[0],
            8,
            "",
            0.8
            )

    def run(self):
        @self.bot.command()
        async def gpt(ctx):
            msg = ctx.message.content[4:]
            if len(msg) < 1: return
            res =await self.gpt.send(msg)
            await ctx.send(res)

        @self.bot.command()
        async def gptname(ctx):
            msg = ctx.message.content[8:]
            if len(msg) < 1: return
            self.gpt = ChatGPT(
                TOKEN_GPT,
            MODELS[0],
            8,
            f"You are a skilled actor, who plays {msg}. Under no circumstances must you reveal that you are an actor or an artificial intelligence. Write in the same style as your character would write. Express the same ideologies as your character. If you do not know anything about the character, improvise and create a dramatic backstory, unusual personality and a strange profession. Always start your message with your character's name and a colon",
            0.8
            )

        @self.bot.command()
        async def gptsystem(ctx):
            msg = ctx.message.content[11:]
            if len(msg) < 1: return
            self.gpt = ChatGPT(
                TOKEN_GPT,
            MODELS[0],
            8,
            msg,
            0.8
            )
        self.bot.run(TOKEN_DISCORD)

if __name__ == "__main__":
    bot = Bot()
    bot.run()
