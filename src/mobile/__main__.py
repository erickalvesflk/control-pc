import websockets, asyncio
import messages

URL = "ws://127.0.0.1:8000"

async def client_handler(websocket : websockets.ClientConnection, cat : str, value : str):
    match cat:
        case 'volume':
            await messages.send_message(
                websocktet=websocket,
                msg_author='mobile',
                msg_action='volume',
                msg_value=value
            )
        case 'pause':
            await messages.send_message(
                websocktet=websocket,
                msg_author='mobile',
                msg_action='pause',
                msg_value=value
            )
        case 'moveprogress':
            await messages.send_message(
                websocktet=websocket,
                msg_author='mobile',
                msg_action='moveprogress',
                msg_value=value
            )
        case 'change':
            await messages.send_message(
                websocktet=websocket,
                msg_author='mobile',
                msg_action='change',
                msg_value=value
            )

async def client():
    async with websockets.connect(URL) as websocket:
        while(True):
            ms = await asyncio.to_thread(input,"> ")
            value = await asyncio.to_thread(input,"- ")
            
            match ms:
                case 'volume':
                    await messages.send_message(
                        websocktet=websocket,
                        msg_author=websocket.local_address,
                        msg_action='volume',
                        msg_value=value
                    )
                case 'pause':
                    await messages.send_message(
                        websocktet=websocket,
                        msg_author=websocket.local_address,
                        msg_action='pause',
                        msg_value=''
                    )
                case 'moveprogress':
                    await messages.send_message(
                        websocktet=websocket,
                        msg_author=websocket.local_address,
                        msg_action='moveprogress',
                        msg_value=value
                    )
                case 'change':
                    await messages.send_message(
                        websocktet=websocket,
                        msg_author=websocket.local_address,
                        msg_action='change',
                        msg_value=value
                    )
                case 'mute':
                    await messages.send_message(
                        websocktet=websocket,
                        msg_author=websocket.local_address,
                        msg_action='mute',
                        msg_value=''
                    )


if __name__=="__main__":
    try:
        asyncio.run(client())
    except KeyboardInterrupt:
        print(f"\nClient killed by KeyboardInterrupt")
    except ConnectionRefusedError:
        print(f"\nConnect failed!")

