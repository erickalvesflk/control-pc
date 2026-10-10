from abc import ABC, abstractmethod
from typing import get_args 
from messages import message_move_progress, message_change_midia
import pyautogui

class HandlerInterface(ABC):
    # Volume interface
    def set_volume(self, value: int) -> None:
        try:
            value = int(value)
        except:
            print("Tipo invalido para a alteração de volume")
            return
        if(value < -100 or value > 100): return
        print(f"- changing the volume to: {value}")
        self._set_volume(value)
    @abstractmethod
    def _set_volume(self, value: int) -> None:
        pass

    # Mute interface
    def set_mute(self) -> None:
        print(f"- Changing mute")
        self._set_mute()
    @abstractmethod
    def _set_mute(self) -> None:
        pass

    # Pause interface
    def set_pause(self) -> None:
        print(f"- Changing pause")
        self._set_pause()
    @abstractmethod
    def _set_pause(self) -> None:
        pass

    # Progress interface
    def change_progress(self, progress : message_move_progress) -> None:
        if not(progress in get_args(message_move_progress.__value__)): return
        print(f"- Changing progress to: {progress}")
        self._change_progress(progress)
    @abstractmethod
    def _change_progress(self, progress : message_move_progress) -> None:
        pass

    # Change Midia interface
    def change_midia(self, change : message_change_midia) -> None:
        if not(change in get_args(message_change_midia.__value__)): return
        print(f"- Changing the midia to: {change}")
        self._change_midia(change)
    @abstractmethod
    def _change_midia(self, change : message_change_midia) -> None:
        pass

class WinHandler(HandlerInterface):
    def _set_pause(self):
        pyautogui.press('playpause')

    def _set_mute(self):
        pyautogui.press('volumemute')

    def _change_progress(self, progress : message_move_progress):
        if progress == 'forward':
            pyautogui.press('right')
        elif progress == 'backward':
            pyautogui.press('left')

    def _set_volume(self, value):
        for _ in range( abs( round(value/2) ) ):
            pyautogui.press('volumeup' if value > 0 else 'volumedown')

    def _change_midia(self, change : message_change_midia):
        pass

class LinuxHandler(HandlerInterface):
    def _set_pause(self):
        ...
    def _set_mute(self):
        ...
    def _change_progress(self, progress : message_move_progress):
        ...
    def _set_volume(self, value):
        ...
    def _change_midia(self, change : message_change_midia):
        ...
