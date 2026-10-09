import websockets, asyncio
from server.constants import *
import server.messages as messages
import server.handlers.general_handler as gh


async def server_handler(websocket : websockets.ServerConnection):
    print(
        f"New Connect session! ID:{websocket.id}\n - Server: {websocket.local_address}\n - Client: {websocket.remote_address}"
    )

    try:
        async for data in websocket:
            message = messages.read_message(data)
            if (message[0]):
                match message[1]['action']:
                    case 'change':
                        ...
                    case 'moveprogress':
                        ...
                    case 'pause':
                        gh.WinHandler.set_pause()
                    case 'volume':
                        ...
                    case 'mute':
                        ...

    except websockets.exceptions.ConnectionClosed:
        websocket.logger.critical(f"Websocket f{websocket.id} session ended!")


async def launch_ws():
    server = await websockets.serve(server_handler, '0.0.0.0', PORT)
    print(f"Control-pc com protocolo WebSocket rodando em ws://localhost:{PORT}")
    await server.serve_forever()

if __name__=="__main__":
    try:
        asyncio.run(launch_ws())
    except KeyboardInterrupt:
        print(f"\nWebsocket server killed by KeyboardInterrupt")
         