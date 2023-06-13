import asyncio
from urllib.parse import quote
from playwright import async_playwright


async def main():
    # 创建Playwright实例
    async with async_playwright() as p:
        # 在特定浏览器上创建一个新的上下文
        browser = await p.chromium.launch()
        context = await browser.new_context()

        # 创建一个新页面并导航到目标网页
        page = await context.new_page()
        JOB_KEY = quote("运维工程师")
        url = f"https://www.zhipin.com/web/geek/job?query={JOB_KEY}&city=101190400"
        await page.goto(url)

        info = []
        while True:
            # 获取当前页面的所有职位元素
            jobs = await page.query_selector_all("//ul[contains(@class,'job-list-box')]")

            for item in jobs:
                job_titles = await item.query_selector_all(
                    "//div[@class='job-card-body clearfix']/a[@class='job-card-left']")
                company_titles = await item.query_selector_all(
                    "//div[@class='job-card-body clearfix']/div[@class='job-card-right']")
                company_urls = await item.query_selector_all(
                    "//div[@class='job-card-body clearfix']/div[@class='job-card-right']/div[@class='company-info']/h3[@class='company-name']/a")

            info.extend([[await title.text(), await title.get_attribute('href'), await company.text(),
                          await url.get_attribute('href')] for title, url, company in
                         zip(job_titles, company_urls, company_titles)])

            if await page.query_selector(
                    "//div[@class='pagination-area']/div[@class='pager text-center']/div[@class='options-pages']/a[contains(text(), '...')]"):
                end_button = await page.query_selector(
                    "//div[@class='pagination-area']/div[@class='pager text-center']/div[@class='options-pages']/a[10]")
                if 'disabled' in await end_button.get_attribute('class'):
                    break
                else:
                    await end_button.click()
            else:
                end_button = await page.query_selector(
                    "//div[@class='pagination-area']/div[@class='pager text-center']/div[@class='options-pages']/a[11]")
                await end_button.click()

            await page.wait_for_timeout(6000)

        print(len(info))
        for item in info:
            print(item)

        # 关闭浏览器
        await browser.close()


# 异步运行主函数
asyncio.run(main())
