from typing import TypedDict, Literal, Any, get_args
from websockets import ClientConnection
import json

type message_author = Literal["mobile", "server"]
type message_action = Literal["volume","mute","pause","moveprogress","change"]
type message_move_progress = Literal["backward","forward"]
type message_change_midia = Literal["previous","next"]

class Message(TypedDict):
    """basic structure of a message"""
    author: message_author
    action: message_action
    value: str

class MessageVolume(Message):
    """Message relationed with change of the volume"""
    value: int
class MessageMute(Message):
    """Message relationed with mute the volume"""
    value: bool
class MessagePause(Message):
    """Message relationed with pause and return the midia"""
    value: bool
class MessageMoveProgress(Message):
    """Message relationed with the progress of the midia (-10s, +10s)"""
    value: message_move_progress
class MessageChange(Message):
    """Message relationed with the buttons previous and next (like when changes episode)"""
    value: message_change_midia

def message_validation(msg : str) -> bool:
    try:
        md : Message = json.loads(msg)

        if not {'author', 'action', 'value'}.issubset(md.keys()): return False
        if not(md['author'] in get_args(message_author.__value__)): return False
        if not(md['action'] in get_args(message_action.__value__)): return False

        return True
    
    except json.JSONDecodeError:
        return False
    except AttributeError :
        return False

def read_message(msg : str) -> tuple[bool,Message]:
    if(not message_validation(msg)): return False,None
    return True,json.loads(msg)

async def send_message(websocktet: ClientConnection, msg_author : message_author, msg_action : message_action, msg_value : Any) -> None:
    await websocktet.send(
        json.dumps(
            {
                'author': msg_author,
                'action': msg_action,
                'value': msg_value
            }
        )
    )