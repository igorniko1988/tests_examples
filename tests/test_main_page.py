import re
from playwright.sync_api import Page, expect


def test_example(page: Page) -> None:
    page.goto("https://www.gt-protocol.io/")
    page.get_by_role("link", name="Explore").click()
    expect(page.locator(".image")).to_be_visible()


def test_introduction(page: Page) -> None:
    page.goto("https://www.gt-protocol.io/#use-cases")
    expect(page.get_by_role("heading", name="GT APP is the Next-gen Web 3.")).to_be_visible()
    expect(page.locator("body")).to_contain_text(
        "GT APP is the Next-gen Web 3.0 Crypto Investment PlatformGT Protocol offers an intuitive non-custodial "
        "crypto investment experience guided by blockchain AI execution interfaceProfitable strategies featuring "
        "controllable risk levels, along with a transparent and traceable history of every dealUnique AI trading "
        "and investment tools powered by an AI execution technologyAccess to crypto investments across DeFi, CeFi, "
        "and NFT markets Join Now")
    with page.expect_popup() as page2_info:
        page.get_by_role("link", name="Join Now").click()
    page2 = page2_info.value
    expect(page2.get_by_role("heading", name="AI-powered crypto investment")).to_be_visible()
