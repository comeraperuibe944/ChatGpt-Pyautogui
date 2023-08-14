import pyautogui as bot
import time

# para exportar para exe: pyinstaller --noconfirm --onefile --console bot.py 

bot.FAILSAFE = True

input1 = input("Enter input da gpt: ")

bot.PAUSE = 1

print("INFO: pouse o mouse no canto superior esquerdo do monitor para forçar parada")

time.sleep(3)

bot.press("win")

bot.write("chrome")

bot.press("enter")

# Point(x=880, y=636)
bot.click(x=880, y=636)

bot.write("https://chat.openai.com/")

bot.press("enter")

bot.write(input1)

bot.press("enter")