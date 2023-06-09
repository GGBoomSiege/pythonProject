from selenium import webdriver
import pymysql
from urllib import parse

drive = webdriver.Chrome()
KeyWord = input("请输入你要搜索的岗位关键字")
KeyWords = parse.quote(parse.quote(KeyWord))
# print(KeyWords)
drive.get("https://www.zhipin.com/c101270100/?query="+KeyWords+"&page=1&ka=page-")
drive.implicitly_wait(10)
datalist = []
def get_job_info():
    lis = drive.find_elements_by_css_selector('.job-list li')
    for li in lis:
        data = []
        # 工作名称
        name = li.find_element_by_css_selector('.job-name a').text
        data.append(name)
        # 工作地点
        area = li.find_element_by_css_selector('.job-area').text
        data.append(area)
        # 公司名称
        company_name = li.find_element_by_css_selector('.company-text .name a').text
        data.append(company_name)
        # 公司类型
        company_type = li.find_element_by_css_selector('.company-text p a').text
        data.append(company_type)
        # 薪资待遇
        money = li.find_element_by_css_selector('.red').text
        money = ''.join(money).replace("13薪", '').replace('14薪', '').replace('16薪', '').replace('·', '')
        if (len(money) > 6): #个别薪资格式不统一，强行用下面代替
            money = "6-8K"
        money = ''.join(money).replace('-','000-').replace('K','000')
        data.append(money)
        # 经验学历
        exp = li.find_element_by_css_selector('.job-limit p').text
        data.append(exp)
        # 标签
        tags = li.find_element_by_css_selector('.tags span').text
        data.append(tags)
        # 福利待遇
        boon = li.find_element_by_css_selector('.info-desc').text
        data.append(boon)
        #tags = [tag.find_element_by_css_selector('.tag-item') for tag in tags]
        # print(name,area,company_name,company_type,money,exp,tags,boon)
        datalist.append(data)
        # nonextpage = drive.find_element_by_css_selector(".page .disabled")
        print(data)
    return datalist

if __name__ == '__main__':
