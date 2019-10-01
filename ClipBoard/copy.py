import Main
import win32clipboard as CB
from time import sleep

def copy_clipboard():
    CB.OpenClipboard()
    content =  CB.GetClipboardData()
    CB.CloseClipboard()
    return content

currentContent = ""
clipboard = Main.textFile("content.txt")

while True:
    highlightedText = copy_clipboard()
    if (highlightedText != currentContent) and (highlightedText != ""):
        currentContent = highlightedText
        clipboard.writeLine(highlightedText+"<|>")
    sleep(1)
