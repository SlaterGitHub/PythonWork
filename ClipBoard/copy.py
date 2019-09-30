import Main
import pyautogui as pya
import pyperclip
import time

def copy_clipboard():
    pya.hotkey('ctrl', 'c')
    time.sleep(.01)
    return pyperclip.paste()

clipboard = Main.textFile("content.txt")
highlightedText = copy_clipboard()
clipboard.writeLine(highlightedText+"<|>")
