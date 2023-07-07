import asyncio
import json
import websockets

async def send_chat_request(user_input, history):
    url = "ws://127.0.0.1:5005/api/v1/stream"  # Replace with the appropriate WebSocket server URL

    payload = {
        'prompt': user_input,
        'history': history,
        'charcter_id': 'Gabriel',
        'instruction_template': 'Vicuna-v1.1',
    }

    async with websockets.connect(url) as websocket:
        await websocket.send(json.dumps(payload))

        async for message in websocket:
            data = json.loads(message)

            if data['event'] == 'text_stream':
                # Handle the streamed data here
                message_num = data['message_num']
                text = data['text']
                # Process the streamed data as needed
                print(f"Received message #{message_num}: {text}")

            elif data['event'] == 'stream_end':
                # Handle the end of the stream
                message_num = data['message_num']
                print(f"Stream ended. Total messages: {message_num}")


# Example usage
user_input = "Me, nothing - what do you know about Herzog?"
history = {'visible': [], 'internal': []}
history['visible'].append("How are you?")
history['visible'].append("What do You know about the shoe that Werner Herzog ate?")
history['internal'].append("How are you?")
history['internal'].append("What do You know about the shoe that Werner Herzog ate?")


async def main():
    await send_chat_request(user_input, history)


asyncio.run(main())
