import asyncio
from playwright.async_api import async_playwright
import yaml


async def main():
    with open("./config.yaml", "r", encoding="utf-8") as f:
        config = yaml.load(f, Loader=yaml.FullLoader)
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context()
        page = await context.new_page()

        await page.goto(config["login_page"])

        await page.fill('input[placeholder="职工号/学号"]', config["student_id"])
        await page.fill('input[placeholder="密码"]', config["password"])

        await page.click("#index_login_btn")

        await page.wait_for_timeout(5000)

        cookies = await context.cookies()
        token = ""
        for cookie in cookies:
            if cookie["name"] == "accessToken":
                token = cookie["value"]

        await browser.close()
        return token


if __name__ == "__main__":
    asyncio.run(main())
