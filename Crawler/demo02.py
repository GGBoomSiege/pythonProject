import requests
from lxml import etree

url = 'http://www.baidu.com/s?'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
    'Cookie': 'PSTM=1659320039; BIDUPSID=A6A453D9C4C2B2DDDBEE6713F0BE6D01; BDUSS=C1OWVZpYlUydUNsQnVRaW1zNG9-T2tqVE1FbDd4Uk1OaUk2cEhUZmVzTWoxaEpqSVFBQUFBJCQAAAAAAAAAAAEAAACMPGYpamltNjIwNTIzAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACNJ62IjSetiV; BDUSS_BFESS=C1OWVZpYlUydUNsQnVRaW1zNG9-T2tqVE1FbDd4Uk1OaUk2cEhUZmVzTWoxaEpqSVFBQUFBJCQAAAAAAAAAAAEAAACMPGYpamltNjIwNTIzAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACNJ62IjSetiV; BAIDUID=719D3802A35CD1624EE4449E2DFD3617:SL=0:NR=10:FG=1; MCITY=-224%3A; BD_UPN=12314753; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; ai-studio-ticket=BB5375D672BF4B319F43761C0650B4F8223C4D866D8A4D3697449115FC24F4A6; BAIDUID_BFESS=719D3802A35CD1624EE4449E2DFD3617:SL=0:NR=10:FG=1; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; delPer=0; BD_CK_SAM=1; PSINO=5; BAIDU_WISE_UID=wapp_1680052780677_442; __bid_n=1859eda39e45b8471a4207; FPTOKEN=gT34cpcuOYv6k9i7GK6Jo0KNWQAFD0q2HAoWuONeHrEl+qGP+xTc5jQKtywvrip3BwNJFJjmqehMPFX7VuWXqY1JkGFJId2vZj7STe708uCJBBRPEjjurinzjZAs3mEk+eACx3KwprzJF4vT5ImOVx6e1TzY5pTv+Pcd13IEWPxQJefcEcwgb/71SAa+i5F+XCMzbAhHzmXIaP2hD6Jz8OuZhCHAse9xlxzpH2mhwDDR0oCPnnHz1hSgZSCR50LH2F0rZVXNz+tf23c+9pxjZScJhjX0UYIG+RKztxcc7gGrWhAWERK/2zMw42ZluBqj3ZwiHlnTzJ+J8I8a3xyvAm7p248/mre8QIJ8MovtT0nPC+4tCdYZ4i11FMYmmirgGJG7W5QroUR1HDoYK5oLQA==|hKYI3uFZLAPJREIoQlJ9/h/u6FhcElWCwYe4BOk2XPQ=|10|3ebe91605095e2a00c113d6e92318c5a; arialoadData=false; ZFY=vyeA6ZVbIg0L1RSA6X9HO9HVcbzV:BF8JQgLqw1GP6VA:C; BD_HOME=1; shifen[1720974_97197]=1680052835; RT="z=1&dm=baidu.com&si=654cc487-ce92-48cf-9c7c-e1b9bcdcb05e&ss=lft01o8i&sl=l&tt=ewr&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf&nu=53zsyvtq&cl=19nq&ld=53mw"; BA_HECTOR=ak2k2ha1al852k248h8hak8n1i274p61m; ab_sr=1.0.1_NGRmOWE0MWZkNmIwNjEzOWM0NzljODY1MzA0ZmJjNzJkNDc5ODM1ODVlZTllNjQyOWFjNDg1OTkwYWQyNWI1YmIyNTJjMTM1ZmU5NzBjYWQyY2Y3NTliZjA4YzE2NTRiY2JmYjlkODA1M2VlYjdiMzgyMGI0MDRlYmFhMDUzYmUwODM1NmRmMTFkZmMyNWM3ZGQ3MDM0MzAxNmJhMDVkZmYwZjExNDU3NGM3YjdiYjU1MzBkODk0MDVjMWE0OTQ1; shifen[1720973_97197]=1680053030; BCLID=11524972199838413812; BCLID_BFESS=11524972199838413812; BDSFRCVID=3q8OJeCT5G09-drfKvCmbYjGN8j2RanTTPjcTR5qJ04BtyCVcmimEG0Ptt_L8MPM_EGSogKKL2OTHmuF_2uxOjjg8UtVJeC6EG0Ptf8g0M5; BDSFRCVID_BFESS=3q8OJeCT5G09-drfKvCmbYjGN8j2RanTTPjcTR5qJ04BtyCVcmimEG0Ptt_L8MPM_EGSogKKL2OTHmuF_2uxOjjg8UtVJeC6EG0Ptf8g0M5; H_BDCLCKID_SF=tbIJoDK5JDD3fP36q45HMt00qxby26nKMjT9aJ5nQI5nhKIzb5jtynKwBU5kafbw5m3ion3vQUbmjRO206oay6O3LlO83h52aC5NKl0MLPbcq-Q2Xh3YBUL10UnMBMnrteOnan6a3fAKftnOM46JehL3346-35543bRTLnLy5KJYMDFRjj8KjjbBDHRf-b-XKD600PK8Kb7Vbn5bXMnkbft7jttjqCrbJDciLfosKfT8spu9M65C-tC73b3B5h3NJ66ZoIbPbPTTSROzMq5pQT8r5hOdWTvuLgjdKl3Rab3vOp44XpO1hJLzBN5thURB2DkO-4bCWJ5TMl5jDh3Mb6ksD-FtqjttJnut_KLhf-3bfTrP-trf5DCShUFsQjclB2Q-5M-a3KtBKJb4bxR-0RLVWf6xWjvBtHrKWfbmLncjSM_GKfC2jMD32tbp5-r0amTxoUJ2bU7dbh6MXqnpQptebPRiWTj9QgbLLlQ7tt5W8ncFbT7l5hKpbt-q0x-jLTnhVn0MBCK0hIKmD6_bj6oM5pJfetjK2CntsJOOaCvr8lQOy4oT35L1DauLKnjhW5cm_now2q3FbbF404Q_3h0rMxbnQjQDWJ4J5tbX0MQjDJTzQft20b03BPkOWlOuX2Txbb7jWhvdhl72y-chQlRX5q79atTMfNTJ-qcH0KQpsIJM5-DWbT8IjHCet60HJRkqoCv5b-0_HRjYbb__-P4DeNbDqURZ5m7n_l0Mf66fqRQo5xbV-lFqQPIOajjNKCon-UJ_KMbCMtj_D5OI5bFd3xbLa4r43bRTLPb7BInYVh63QfJ6hP-UyPkHWh37a6TlMKoaMp78jR093JO4y4Ldj4oxJpOJ5JbMopCafJOKHIC4eju5DUK; H_BDCLCKID_SF_BFESS=tbIJoDK5JDD3fP36q45HMt00qxby26nKMjT9aJ5nQI5nhKIzb5jtynKwBU5kafbw5m3ion3vQUbmjRO206oay6O3LlO83h52aC5NKl0MLPbcq-Q2Xh3YBUL10UnMBMnrteOnan6a3fAKftnOM46JehL3346-35543bRTLnLy5KJYMDFRjj8KjjbBDHRf-b-XKD600PK8Kb7Vbn5bXMnkbft7jttjqCrbJDciLfosKfT8spu9M65C-tC73b3B5h3NJ66ZoIbPbPTTSROzMq5pQT8r5hOdWTvuLgjdKl3Rab3vOp44XpO1hJLzBN5thURB2DkO-4bCWJ5TMl5jDh3Mb6ksD-FtqjttJnut_KLhf-3bfTrP-trf5DCShUFsQjclB2Q-5M-a3KtBKJb4bxR-0RLVWf6xWjvBtHrKWfbmLncjSM_GKfC2jMD32tbp5-r0amTxoUJ2bU7dbh6MXqnpQptebPRiWTj9QgbLLlQ7tt5W8ncFbT7l5hKpbt-q0x-jLTnhVn0MBCK0hIKmD6_bj6oM5pJfetjK2CntsJOOaCvr8lQOy4oT35L1DauLKnjhW5cm_now2q3FbbF404Q_3h0rMxbnQjQDWJ4J5tbX0MQjDJTzQft20b03BPkOWlOuX2Txbb7jWhvdhl72y-chQlRX5q79atTMfNTJ-qcH0KQpsIJM5-DWbT8IjHCet60HJRkqoCv5b-0_HRjYbb__-P4DeNbDqURZ5m7n_l0Mf66fqRQo5xbV-lFqQPIOajjNKCon-UJ_KMbCMtj_D5OI5bFd3xbLa4r43bRTLPb7BInYVh63QfJ6hP-UyPkHWh37a6TlMKoaMp78jR093JO4y4Ldj4oxJpOJ5JbMopCafJOKHIC4eju5DUK; baikeVisitId=92e8fc25-199e-4a8a-97c9-1a4e3e869934; sug=3; sugstore=0; ORIGIN=0; bdime=0; H_PS_PSSID=38185_36543_38408_38470_38351_38366_38399_38468_38171_38289_37920_38383_26350_38423_38283_37881; H_PS_645EC=2886NZIG6dUQLkZig0AIzq9wYm%2FGZ%2FTwxomPCymkWOBUEftIq47HCZ3%2BRk0; BDSVRTM=0; COOKIE_SESSION=160_1_8_8_8_16_0_0_8_6_0_2_1448_0_62_0_1680054227_1679994353_1680054165%7C9%232876747_13_1679993624%7C9; Hm_lvt_aec699bb6442ba076c8981c6dc490771=1678173661,1679994487,1680054575; Hm_lpvt_aec699bb6442ba076c8981c6dc490771=1680054575'
}

data = {
    'wd': 'python'
}

res = requests.get(url, headers=headers, params=data)

res.encoding='utf-8'

text = res.text

html = etree.HTML(text)

result = html.xpath('//div[@class="c-container"]/div[1]/h3[@class="c-title t t tts-title"]/a')
# print(result)

for item in result:
    print(item.text)