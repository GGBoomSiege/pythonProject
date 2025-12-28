import pyautogui
import os

# 创建保存截图的目录
output_dir = "ScreenShot/images"
os.makedirs(output_dir, exist_ok=True)

# 截取全屏
screenshot = pyautogui.screenshot()
screenshot.save(os.path.join(output_dir, "full_screen.png"))

# 截取指定区域 (left, top, width, height)
region_screenshot = pyautogui.screenshot(region=(100, 100, 400, 300))
region_screenshot.save(os.path.join(output_dir, "region.png"))

print(f"截图已保存至 {output_dir} 目录")
