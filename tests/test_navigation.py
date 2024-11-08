# import re
# from playwright.sync_api import Page, expect
# import allure
#
#
# def test_pitch_deck_link_redirects_to_correct_url(page):
#     with allure.step('open gt_protocol site'):
#         page.goto("https://www.gt-protocol.io/")
#     with allure.step('open pitch deck link'):
#         with page.context.expect_page() as new_page_info:
#             page.click("text=Pitch Deck")
#     new_page = new_page_info.value
#
#     expected_url = "https://docsend.com/view/zaxagncyq87qpvyc"
#     with allure.step('Check that pitch deck has needed url'):
#         expect(new_page).to_have_url(expected_url)
#
#     new_page.close()
#
#
# def test_use_cases_link_redirects_to_correct_section(page):
#     page.goto("https://www.gt-protocol.io/")
#     page.click("text=Use Cases")
#
#     expected_url_fragment = "/#use-cases"
#     expect(page).to_have_url("https://www.gt-protocol.io/#use-cases")
#     expect(page.get_by_role("heading", name="AI crypto management")).to_be_visible()
#
#
# def test_technology_link_redirects_to_correct_section(page):
#     page.goto("https://www.gt-protocol.io/")
#
#     page.click("text=Technology")
#     # page.wait_for_load_state("networkidle")
#
#     expect(page).to_have_url("https://www.gt-protocol.io/#technology")
#     expect(page.locator("#technology").get_by_text("Technology")).to_be_visible()
#
#
# #
#
#
# def test_community(page):
#     # page.hover(page.get_by_role("button", name="Community"))
#     expect(page.get_by_label("Community")).to_contain_text(
#         "Telegram ChannelGlobal Official ChatGTAI Traders ChatLocal "
#         "Telegram Groups:СНГTRCNTwitterMediumYoutubeLinkedin"
#         "FacebookInstagramTikTok"
#     )
#
#
#
# def test_partners_link_and_backers_section(page):
#     page.goto("https://www.gt-protocol.io/")
#
#     page.click("text=Partners")
#
#     expected_anchor = "https://www.gt-protocol.io/#partners"
#     expect(page).to_have_url(expected_anchor)
#
#     backers_section = page.locator(".backers-wrapper")
#     expect(backers_section).to_be_visible()
#
#     expect(page.locator(".backers-list .logo-card")).to_have_count(8)
#
#
# def test_team_section_and_member_bios(page):
#     page.goto("https://www.gt-protocol.io/")
#
#     page.click("text=Team")
#
#     expected_anchor = "https://www.gt-protocol.io/#team"
#     expect(page).to_have_url(expected_anchor)
#
#     team_section = page.locator("section#team")
#     expect(team_section).to_be_visible()
#
#
# # def test_buy_gtai_link_redirects_to_correct_url(page):
# #     page.goto("https://www.gt-protocol.io/")
# #
# #     with page.context.expect_page() as new_page_info:
# #         page.click("text=Buy $GTAI")
# #
# #     new_page = new_page_info.value
# #
# #     # expected_title = "Bybit | Spot Trading Platform"
# #     # expect(new_page).to_have_title(expected_title)
# #     new_page.wait_for_load_state('load')
# #     new_page.close()
#
#
# #
# # def test_stake_gtai_link_redirects_to_correct_url(page):
# #     page.goto("https://www.gt-protocol.io/")
# #
# #     with page.context.expect_page() as new_page_info:
# #         page.click("text=Stake $GTAI")
# #     new_page = new_page_info.value
# #
# #     expected_title = "GT Protocol | Staking"
# #     expect(new_page).to_have_title(expected_title)
# #     new_page.close()
#
#
# # def test_launch_app_link_redirects_to_correct_url(page):
# #     page.goto("https://www.gt-protocol.io/")
# #
# #     with page.context.expect_page() as new_page_info:
# #         page.locator('#fixed-nav > div.nav.w-nav > div.nav-container.nav-dark-bg.w-container > div.nav-action > '
# #                      'a.btn-outline.header-action.btn-app.btn-hide-mobile.w-inline-block > div.btn-outline-frame').click()
# #     new_page = new_page_info.value
# #
# #     new_page.wait_for_load_state("networkidle")
# #     expected_title = "GT App— Copy Trading Bot for Binance Futures"
# #     expect(new_page).to_have_title('GT App— Copy Trading Bot for Binance Futures')
# #
# #
# #     new_page.close()
