import requests

url = "https://www.fisica.ugto.mx/~ggutj/CV/Classical_Electrodynamics_Jackson_1a_Edicion.pdf"
response = requests.get(url, verify=False)

# 确保请求成功
if response.status_code == 200:
    with open("sample.pdf", "wb") as f:
        f.write(response.content)
    print("PDF 下载完成")
else:
    print("下载失败，状态码：", response.status_code)
