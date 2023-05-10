import autoit
import time

autoit.send("#r")
autoit.win_wait_active("[class:#32770]")
autoit.send("cmd")
time.sleep(1)
autoit.control_click("[class:#32770]","1")
time.sleep(1)
autoit.win_activate("[class:CASCADIA_HOSTING_WINDOW_CLASS]")
time.sleep(1)
# autoit.mouse_click("",478, 385)
autoit.send("ipconfig /all")
autoit.send("{ENTER}")