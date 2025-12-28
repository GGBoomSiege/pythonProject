import pyautogui
import time
import os
from time import sleep
from screeninfo import get_monitors


# def take_screenshot():
#     """
#     截取全屏并保存为PNG文件
#     :param filename: 保存文件名（可选，默认按时间戳生成）
#     :return: 保存的文件路径
#     """
#     # 创建保存截图的目录
#     output_dir = "ScreenShot/images"
#     os.makedirs(output_dir, exist_ok=True)

#     monitors = get_monitors()
#     screenshots = []

#     for monitor in monitors:
#         screenshot = pyautogui.screenshot(
#             region=(monitor.x, monitor.y, monitor.width, monitor.height)
#         )
#         screenshots.append(screenshot)

#     for i, screenshot in enumerate(screenshots):
#         filename = f"screenshot_{i}_{time.strftime('%Y%m%d_%H%M%S')}.png"
#         try:
#             screenshot.save(os.path.join(output_dir, filename))
#             print(f"截图已保存为: {filename}")
#         except Exception as e:
#             print(f"截图失败: {str(e)}")

#     return


def take_screenshot():
    """
    截取全屏并保存为PNG文件
    :param filename: 保存文件名（可选，默认按时间戳生成）
    :return: 保存的文件路径
    """
    # 创建保存截图的目录
    output_dir = "ScreenShot/images"
    os.makedirs(output_dir, exist_ok=True)

    filename = f"screenshot_{time.strftime('%Y%m%d_%H%M%S')}.png"
    try:
        screenshot = pyautogui.screenshot()
        screenshot.save(os.path.join(output_dir, filename))
        print(f"截图已保存为: {filename}")
    except Exception as e:
        print(f"截图失败: {str(e)}")

    return


if __name__ == "__main__":
    while True:
        take_screenshot()
        sleep(1)  # 每1秒截取一次

    # take_screenshot()
