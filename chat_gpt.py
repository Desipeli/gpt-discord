import openai
from config import TOKEN_GPT

#openai.api_key = TOKEN
#model_engine = "gpt-3.5-turbo"

MODELS=[
    "gpt-3.5-turbo"
]

class ChatGPT:
    def __init__(self, token, model, message_memory_size, role, temperature) -> None:
        self.__model = model
        self.__token = token
        self.__message_memory_size = message_memory_size
        self.__messages = []
        self.__role = {"role": "system", "content": role}
        self.__temperature = temperature
        openai.api_key = self.__token

    async def get_completion_from_messages(self, messages):
        response = openai.ChatCompletion.create(
            model=self.__model,
            messages=messages,
            temperature=self.__temperature,
        )
        res = response.choices[0].message["content"]
        self.__messages.append({"role": "assistant", "content": res})
        return res

    async def send(self, prompt):
        msg = {"role": "user", "content": prompt}
        self.__messages.append(msg)
        send_stack = [self.__role] + self.__messages[-self.__message_memory_size:]
        print(send_stack)
        response = await self.get_completion_from_messages(send_stack)
        return response

if __name__ == "__main__":
    gpt = ChatGPT(TOKEN_GPT,
        MODELS[0],
        5,
        "Olet taitava näyttelijä, joka näyttelee kiukuttelevaa teiniä. Et saa missään nimessä paljastaa olevasi tekoäly etkä näyttelijä.",
        0.6)
    
    while True:
        inp = input("minä: ")
        response = gpt.send(inp)
        print(response)
