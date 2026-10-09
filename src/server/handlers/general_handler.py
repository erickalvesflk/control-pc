from abc import ABC, abstractmethod
from typing import get_args 
from server.messages import message_move_progress, message_change_midia
import pyautogui

class HandlerInterface(ABC):

    # Volume interface
    @staticmethod
    def set_volume(value: int) -> None:
        if(value < 0 or value > 100): return
        HandlerInterface._set_volume(value)
    @abstractmethod
    def _set_volume(value: int) -> None:
        pass

    # Mute interface
    @staticmethod
    def set_mute() -> None:
        HandlerInterface._set_mute()
    @abstractmethod
    def _set_mute() -> None:
        pass

    # Pause interface
    def set_pause() -> None:
        HandlerInterface._set_pause()
    @abstractmethod
    def _set_pause() -> None:
        pass

    # Progress interface
    def change_progress(progress : message_move_progress) -> None:
        if not(progress in get_args(message_move_progress.__value__)): return
        HandlerInterface._change_progress(progress)
    @abstractmethod
    def _change_progress(progress : message_move_progress) -> None:
        pass

    # Change Midia interface
    def change_midia(change : message_change_midia) -> None:
        if not(change in get_args(message_change_midia.__value__)): return
        HandlerInterface._change_midia(change)
    @abstractmethod
    def _change_midia(change : message_change_midia) -> None:
        pass

class WinHandler(HandlerInterface):
    def _set_pause():
        pyautogui.press('playpause')

    def _set_mute():
        pyautogui.press('volumemute')

    def _change_progress(progress : message_move_progress):
        if progress == 'forward':
            pyautogui.press('right')
        elif progress == 'backward':
            pyautogui.press('left')

    def _set_volume(value):
        for _ in range(abs(value)):
            pyautogui.press('volumeup' if value > 0 else 'volumedown')

    def _change_midia(change : message_change_midia):
        pass