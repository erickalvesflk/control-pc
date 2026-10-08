import websockets, asyncio

URL = "ws://127.0.0.1:8000"

async def lisening_events(websocket : websockets.ServerConnection):
        print("[!] - Connected!")
        print(type(websocket))
        await websocket.send("Bem-vindo ao servidor WebSocket!")
        while True:
            await asyncio.sleep(.1)
            async for mensagem in websocket:
                print(mensagem)

async def launch_ws():
    async with websockets.serve(lisening_events, "0.0.0.0", 8000):
        print("[!] Servidor WebSocket rodando em ws://localhost:8000")
        await asyncio.Event().wait()
        
asyncio.run(launch_ws())