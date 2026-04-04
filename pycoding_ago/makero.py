import pyautogui
import time

time.sleep(3)  # 실행 후 3초 기다림 (준비 시간)

while True:
    pyautogui.hotkey('ctrl', 'v')  # 붙여넣기
    pyautogui.press('enter')      # 엔터
    time.sleep(1)  # 1초 간격 (너무 빠르면 문제 생길 수 있음)