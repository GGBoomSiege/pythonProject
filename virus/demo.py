import vt
import os
import threading
import time
from tqdm import tqdm

API_KEY = "2677854c2a261f0d3fd2353b7d3c00591e924ddeca451bd4b5b02bb42356d05d"
FILE_PATH = (
    "C:\\Users\\39694\\Downloads\\LANDrop\\GRLPackage_3.0.24.0821_52pj.exe.part0"
)


def show_progress_bar(f, filesize, stop_event):
    pbar = tqdm(total=filesize, unit="B", unit_scale=True, desc="上传进度")
    last_pos = 0
    while not stop_event.is_set():
        current_pos = f.tell()
        delta = current_pos - last_pos
        if delta > 0:
            pbar.update(delta)
            last_pos = current_pos
        time.sleep(0.1)
    pbar.update(f.tell() - last_pos)
    pbar.close()


client = vt.Client(API_KEY, timeout=1200)  # 这里传数字，不是 ClientTimeout 对象

with open(FILE_PATH, "rb") as f:
    filesize = os.path.getsize(FILE_PATH)
    stop_event = threading.Event()
    progress_thread = threading.Thread(
        target=show_progress_bar, args=(f, filesize, stop_event)
    )
    progress_thread.start()

    try:
        analysis = client.scan_file(f, wait_for_completion=True)
    finally:
        stop_event.set()
        progress_thread.join()
        client.close()

print("\n分析完成！查看结果：")
print(f"https://www.virustotal.com/gui/file/{analysis.file_id}")
