import asyncio

async def stream_response(prompt: str):
    response = f"You asked: {prompt}"

    for word in response.split():
        yield word + " "
        await asyncio.sleep(0.2)