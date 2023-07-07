
import openai
import asyncio

"""
openai.token

one line, raw text of the token
"""
with open('openai.token', 'r') as file:
    file_content = file.read()
openai.api_key = file_content

async def try_and_answer(message):
    async with message.channel.typing():
        # get the current thread or create a new thread for the bot's response
        # TODO: I dint know how to make it nice so I made it work, sorry
        try:
            # if message.channel is type Thread it cannot create a new thread and will fail
            thread = await message.channel.create_thread(name="Answer Thread", message=message)
            
        except:
            # we know its a thread because it otherwise the last step would have not failed
            thread = message.channel
  

        initial_response = await thread.send("Marvin is thinking so hard it would hurt if it could ...")

        threadmessages=[
                {'role':'assistant', 'content':'you are Marvin, chatgpt based ai assisnt who can answer all sorts of questions and write python code. You keep answers as short as possible'},
                ]
        
        # get all messages from discord thread
        async for msg in thread.history(limit=None):
            if msg.author == message.author:
                threadmessages.append({'role': 'user', 'content': msg.content})
            else:
                threadmessages.append({'role': 'assistant', 'content': msg.content})

        threadmessages.append({'role': 'user', 'content': message.content})


        response = openai.ChatCompletion.create(
            model='gpt-3.5-turbo',
            messages=threadmessages,
            temperature=0.5,
        )

        while not response.choices[0].message.content.strip():
            await asyncio.sleep(2)
            response = openai.Completion.fetch(response.id)

        print(str(response))

        # Send the bot's response in the thread
        response_text = response.choices[0].message.content
        max_length = 2000  # Discord message character limit
        num_messages = (len(response_text) // max_length) + 1

        for i in range(num_messages):
            start = i * max_length
            end = start + max_length
            content = response_text[start:end]

            # Send each part of the response in the thread
            await thread.send(content)
        
        # Edit the initial response in the original channel
        await initial_response.edit(content="Response has been posted in a thread.")


# Create a simple test
# [1] Coms work
# [2] Rembers Context