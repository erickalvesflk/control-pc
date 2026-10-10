import websockets, asyncio, platform
from constants import *
import messages as messages
from handlers import HandlerInterface, WinHandler, LinuxHandler

handler_module : HandlerInterface
if platform.system() == 'Windows': 
    print("Using the windows' handler...")
    handler_module = WinHandler()
elif platform.system() == 'Linux':
    print("Using the linux's handler...")
    handler_module = LinuxHandler()

async def pc_handler(message : messages.Message):
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
    print(
        f"New Connect session! ID:{websocket.id}\n - Server: {websocket.local_address}\n - Client: {websocket.remote_address}",
    )
    try:
        async for data in websocket:
            print(f"New data: {data}", end='')
            message_container = messages.read_message(data)

            if (message_container[0]):
                print(" ... It is a valid message!")
                await pc_handler(message_container[1])
            else:
                print(" ... It is NOT a valid message!")


    except websockets.exceptions.ConnectionClosed:
        websocket.logger.critical(f"Websocket f{websocket.id} session ended!")
        
    except Exception as e:
        websocket.logger.critical(e)

async def launch_ws():
    async with websockets.serve(server_handler, "0.0.0.0", PORT) as server:
        print(f"Servidor rodando na porta {PORT}")
        await server.serve_forever()


if __name__=="__main__":
    try:
        asyncio.run(launch_ws())
    except KeyboardInterrupt:
        print(f"\nWebsocket server killed by KeyboardInterrupt")

