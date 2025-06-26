def split_file(filepath, chunk_size_mb):
    chunk_size = chunk_size_mb * 1024 * 1024
    with open(filepath, "rb") as f:
        i = 0
        while True:
            chunk = f.read(chunk_size)
            if not chunk:
                break
            with open(f"{filepath}.part{i}", "wb") as out:
                out.write(chunk)
            print(f"已生成: {filepath}.part{i} ({len(chunk)} bytes)")
            i += 1


# 使用方法
split_file(
    "C:\\Users\\39694\\Downloads\\LANDrop\\GRLPackage_3.0.24.0821_52pj.exe", 620
)  # 每段30MB以内
