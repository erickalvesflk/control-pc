from typing import TypedDict, Literal

class Message(TypedDict):
    origin: Literal["mobile", "server"]
    desc: Literal["volume","pause","moveprogress","change"]
    value: any

class MessageVolume(Message):
    value: int

class MessagePause(Message):
    value: bool

class MessageMoveProgress(Message):
    value: Literal["backward","forward"]

class MessageChange(Message):
    value: Literal["previous","next"]

PORT = 8000
URL = f"ws://127.0.0.1:{PORT}"