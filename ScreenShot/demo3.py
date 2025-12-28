from screeninfo import get_monitors
import pyautogui
import os

monitors = get_monitors()
screenshots = []
output_dir = "ScreenShot/images"
os.makedirs(output_dir, exist_ok=True)

for i, monitor in enumerate(monitors):
    screenshot = pyautogui.screenshot(
        region=(monitor.x, monitor.y, monitor.width, monitor.height)
    )
    screenshot.save(f"{output_dir}/screenshot_{i}.png")
    print(screenshot)
