import websockets, asyncio
from constants import *
from platform import system as get_system
from messages import Message, read_message
from handlers import HandlerInterface, WinHandler, LinuxHandler
import logging

logging.basicConfig(
    level=None,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s"
)

handler_module : HandlerInterface
if get_system() == 'Windows': 
    print("Using the windows handler...")
    handler_module = WinHandler()
elif get_system() == 'Linux':
    print("Using the linux's handler...")
    handler_module = LinuxHandler()

async def pc_handler(message : Message):
    match message['action']:
        case 'change':
            handler_module.change_midia(message['value'])
        case 'moveprogress':
            handler_module.change_progress(message['value'])
        case 'pause':
            handler_module.set_pause()
        case 'volume':
            handler_module.set_volume(message['value'])
        case 'mute':
            handler_module.set_mute()

async def server_handler(websocket : websockets.ServerConnection):
    websocket.logger.info(
        f"New Connect session! ID:{websocket.id}\n - Server: {websocket.local_address}\n - Client: {websocket.remote_address}",
    )

    try:
        async for data in websocket:
            websocket.logger.info(f"New data: {data}", end='')
            message_container = read_message(data)

            if (message_container[0]):
                websocket.logger.debug(" ... It is a valid message!")
                await pc_handler(message_container[1])
            else:
                websocket.logger.debug(" ... It is NOT a valid message!")

    except websockets.exceptions.ConnectionClosed:
        websocket.logger.critical(f"Websocket f{websocket.id} session ended!")
    except Exception as e:
        websocket.logger.critical(e)

async def launch_ws():
    async with websockets.serve(server_handler, "0.0.0.0", PORT) as server:
        server.logger.info(f"Servidor rodando na porta {PORT}")
        await server.serve_forever()

if __name__=="__main__":
    try:
        asyncio.run(launch_ws())
    except KeyboardInterrupt:
        print(f"\nWebsocket server killed by KeyboardInterrupt")