import requests
import json
from lxml import etree

url = 'https://complexsearch.kugou.com/v2/search/song?callback=callback123&srcappid=2919&clientver=1000&clienttime=1680059448649&mid=7d2c08b54d7703de1e5775d9069e1efa&uuid=7d2c08b54d7703de1e5775d9069e1efa&dfid=1bmguz1ka3uc1f09CB3leCa8&page=1&pagesize=30&bitrate=0&isfuzzy=0&inputtype=0&platform=WebFilter&userid=0&iscorrection=1&privilege_filter=0&filter=10&token=&appid=1014&signature=73ef6e365fb61365aa5da86ca04c9e68&keyword=%E8%99%8E%E4%BA%8C'

data = {
    'keyword': '%E8%99%8E%E4%BA%8C'
}

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
    'cookie': 'kg_mid=7d2c08b54d7703de1e5775d9069e1efa; kg_dfid=1bmguz1ka3uc1f09CB3leCa8; kg_dfid_collect=d41d8cd98f00b204e9800998ecf8427e; Hm_lvt_aedee6983d4cfc62f509129360d6bb3d=1680057024; kg_mid_temp=7d2c08b54d7703de1e5775d9069e1efa; Hm_lpvt_aedee6983d4cfc62f509129360d6bb3d=1680070945'
}

response = requests.get(url, headers=headers)

response.encoding = 'utf-8'

music_str = response.text[12:-2]

music_dic = json.loads(music_str)

for item in music_dic['data']['lists']:
    # print(f'{item["SingerName"]}-----{item["SongName"]}-----{item["EMixSongID"]}')
    filename = f'data/{item["SongName"]}-{item["SingerName"]}.mp3'
    info_url = f'https://wwwapi.kugou.com/yy/index.php?r=play/getdata&encode_album_audio_id={item["EMixSongID"]}'
    info_response = requests.get(info_url, headers=headers)
    info_response.encoding = 'utf-8'
    info_response_str = info_response.text
    info_response_dic = json.loads(info_response_str)
    music_url = info_response_dic['data']['play_url']
    with open(filename,'wb') as wfile:
        wfile.write(requests.get(music_url, headers=headers).content)