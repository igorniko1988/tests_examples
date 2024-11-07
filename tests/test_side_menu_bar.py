import re
from playwright.sync_api import Page, expect


def test_sidebar_is_visible(page: Page) -> None:
    page.goto("https://www.gt-protocol.io/")
    expect(page.locator(".aside-media")).to_be_visible()
    (expect(page.get_by_text("A Web3 AI execution technology that provides you with access to CeFi, DeFi, and")).
     to_be_visible())
    page.locator("#telegram-nav-link").get_by_role("link").click()
    expect(page.get_by_role("figure")).to_contain_text("Telegram ChannelGlobal Official ChatGTAI Traders ChatFounder's "
                                                       "Personal ChannelLocal Telegram Groups:СНГTRKRCNPR")


import re
from playwright.sync_api import Page, expect


import re
from playwright.sync_api import Page, expect


def test_sidebar_menu(page: Page) -> None:
    page.goto("https://www.gt-protocol.io/")
    page.locator("#telegram-nav-link").get_by_role("link").click()
    with page.expect_popup() as page1_info:
        page.get_by_role("link", name="Telegram Channel").click()
    page1 = page1_info.value
    expect(page1.locator("span")).to_contain_text("GT Protocol Announcements Channel")
    with page.expect_popup() as page2_info:
        page.get_by_role("figure").get_by_role("link", name="Global Official Chat").click()
    page2 = page2_info.value
    expect(page2.locator("span")).to_be_visible()
    expect(page2.locator("span")).to_contain_text("GT Protocol Community Chat")
    with page.expect_popup() as page3_info:
        page.get_by_role("figure").get_by_role("link", name="GTAI Traders Chat").click()
    page3 = page3_info.value
    expect(page3.locator("span")).to_contain_text("GT Protocol traders chat")
    with page.expect_popup() as page4_info:
        page.get_by_role("link", name="Founder's Personal Channel").click()
    page4 = page4_info.value
    expect(page4.locator("span")).to_contain_text("Vlad Balaban | 8 Billions Mindset")
    page.get_by_role("figure").get_by_text("Local Telegram Groups:").click()
    with page.expect_popup() as page5_info:
        page.get_by_role("link", name="СНГ").click()
    page5 = page5_info.value
    expect(page5.locator("span")).to_contain_text("GT Protocol - СНГ чат")
    with page.expect_popup() as page6_info:
        page.get_by_role("link", name="TR", exact=True).click()
    page6 = page6_info.value
    expect(page6.locator("span")).to_contain_text("GT Protocol Türkiye 🇹🇷")
    with page.expect_popup() as page7_info:
        page.get_by_role("link", name="KR").click()
    page7 = page7_info.value
    expect(page7.locator("span")).to_contain_text("GT Protocol Korean Chat")
    with page.expect_popup() as page8_info:
        page.get_by_role("link", name="CN").click()
    page8 = page8_info.value
    expect(page8.locator("span")).to_contain_text("GT Protocol Chinese Chat")
    with page.expect_popup() as page9_info:
        page.get_by_role("link", name="PR", exact=True).click()
    page9 = page9_info.value
    expect(page9.locator("span")).to_contain_text("GT Protocol Persian Chat")


import re
from playwright.sync_api import Page, expect


def test_example(page: Page) -> None:
    page.goto("https://www.gt-protocol.io/")
    with page.expect_popup() as page7_info:
        page.locator("li:nth-child(2) > .aside-link-block").click()
    page7 = page7_info.value
    with page.expect_popup() as page8_info:
        page.locator("li:nth-child(3) > .aside-link-block").click()
    page8 = page8_info.value
    with page.expect_popup() as page9_info:
        page.locator("li:nth-child(4) > .aside-link-block").click()
    page9 = page9_info.value
    with page.expect_popup() as page10_info:
        page.locator("li:nth-child(5) > .aside-link-block").click()
    page10 = page10_info.value
    with page.expect_popup() as page11_info:
        page.locator("li:nth-child(6) > .aside-link-block").click()
    page11 = page11_info.value
    with page.expect_popup() as page12_info:
        page.locator("li:nth-child(7) > .aside-link-block").click()
    page12 = page12_info.value
    with page.expect_popup() as page13_info:
        page.locator("li:nth-child(7) > .aside-link-block").click()
    page13 = page13_info.value
    with page.expect_popup() as page14_info:
        page.locator("li:nth-child(8) > .aside-link-block").click()
    page14 = page14_info.value


