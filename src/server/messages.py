from typing import TypedDict, Literal,Tuple, get_args
import json

type message_author = Literal["mobile", "server"]
type message_action = Literal["volume","pause","moveprogress","change"]

class Message(TypedDict):
    """basic structure of a message"""
    origin: message_author
    action: message_action
    value: any

class MessageVolume(Message):
    """Message relationed with change of the volume"""
    value: int
class MessagePause(Message):
    """Message relationed with pause and return the midia"""
    value: bool
class MessageMoveProgress(Message):
    """Message relationed with the progress of the midia (-10s, +10s)"""
    value: Literal["backward","forward"]
class MessageChange(Message):
    """Message relationed with the buttons previous and next (like when changes episode)"""
    value: Literal["previous","next"]

def message_validation(msg : str) -> bool:
    try:
        md : Message = json.loads(msg)

        if not {'origin', 'action', 'value'}.issubset(md.keys()): return False
        if not(md['origin'] in get_args(message_author)): return False
        if not(md['action'] in get_args(message_action)): return False

        return True
    
    except json.JSONDecodeError:
        return False

def read_message(msg : str) -> tuple[bool,Message]:
    if(not message_validation(msg)): return False,None
    return True,json.loads(msg)

def write_message(msg_origin : message_author, msg_action : message_action, msg_value : any) -> str:
    return json.dumps(
        {
            'origin': msg_origin,
            'action': msg_action,
            'value': msg_value
        }
    )