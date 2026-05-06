from playwright.sync_api import sync_playwright
import time


def display_in_browser(title: str, content: str):
    p = sync_playwright().start()

    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    page.set_content(f"""
    <html>
        <body>
            <h1>{title}</h1>
            <p>{content}</p>
        </body>
    </html>
    """)

    print("浏览器已打开，按 Ctrl + C 退出")

    while True:
        time.sleep(1)