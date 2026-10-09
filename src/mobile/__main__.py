import websockets, asyncio
import messages

URL = "ws://127.0.0.1:8000"

async def test():
    async with websockets.connect(URL) as websocket:
        while(True):
            ms = input("> ")
            match ms:
                case 'volume':
                    await messages.send_message(
                        websocktet=websocket,
                        msg_author='mobile',
                        msg_action='volume',
                        msg_value=input("- Volume: ")
                    )
                case 'pause':
                    await messages.send_message(
                        websocktet=websocket,
                        msg_author='mobile',
                        msg_action='pause',
                        msg_value=input("- pause: ")
                    )
                case 'moveprogress':
                    await messages.send_message(
                        websocktet=websocket,
                        msg_author='mobile',
                        msg_action='moveprogress',
                        msg_value=input("- moveprogress: ")
                    )
                case 'change':
                    await messages.send_message(
                        websocktet=websocket,
                        msg_author='mobile',
                        msg_action='change',
                        msg_value=input("- change: ")
                    )

if __name__=="__main__":
    try:
        asyncio.run(test())
    except KeyboardInterrupt:
        print(f"\nClient killed by KeyboardInterrupt")
    except ConnectionRefusedError:
        print(f"\nConnect failed!")