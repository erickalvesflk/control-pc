import websockets, asyncio

URL = "ws://127.0.0.1:8000"

async def test():
    async with websockets.connect(URL) as websocket:
        while(True):
            ms = input("> ")
            await websocket.send(ms)

if __name__=="__main__":
    asyncio.run(test())