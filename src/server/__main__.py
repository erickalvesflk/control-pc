import websockets, asyncio
from constants import *
import messages
URL = "ws://127.0.0.1:8000"

async def handler(websocket : websockets.ServerConnection):
    print(
        f"New Connect session! ID:{websocket.id}\n - Server: {websocket.local_address}\n - Client: {websocket.remote_address}"
    )

    try:
        async for mensagem in websocket:
            print(mensagem)
            print(messages.read_message(mensagem))

    except websockets.exceptions.ConnectionClosed:
        websocket.logger.critical(f"Websocket f{websocket.id} session ended!")


async def launch_ws():
    server = await websockets.serve(handler, '0.0.0.0', PORT)
    print(f"Control-pc com protocolo WebSocket rodando em ws://localhost:{PORT}")
    await server.serve_forever()

try:
    asyncio.run(launch_ws())
except KeyboardInterrupt:
    print(f"\nWebsocket server killed by KeyboardInterrupt")
         