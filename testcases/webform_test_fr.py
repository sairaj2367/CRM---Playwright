import pytest
import config
from playwright.sync_api import Playwright, sync_playwright, Page, BrowserContext, Browser, expect
import utils.read_utility as reader
from pages.webform_po import Webform
from utils.actions import Action

testdata = "./test_data/test_webform.csv"
testdata_form = "./test_data/form_data.csv"

# @pytest.mark.webform
# @pytest.mark.parametrize("url", config.Config.URLs_to_test_fr)
# def test_page_url_path_fr(url, browser : Browser) -> None:
#     context = browser.new_context(
#         #record_video_dir= "video/"
#     )
#     page = context.new_page()
#     page.set_default_timeout(300000)
#     page.goto(url)
#     data = reader.read_test_data(testdata, Action.get_current_test_name())
#     expected_partial_url = data[0]
#     action_obj = Action(page)
#     action_obj.verify_current_url(expected_partial_url)
#     page.close()

# @pytest.mark.webform
# @pytest.mark.parametrize("url", config.Config.URLs_to_test_fr)
# def test_page_title_fr(url, page: Page) -> None:
#     page.set_default_timeout(80000)
#     page.goto(url)
#     data = reader.read_test_data(testdata, Action.get_current_test_name())
#     page_title = data[1]
#     webform_obj = Webform(page)
#     webform_obj.verify_page_title(page_title)

@pytest.mark.webform
@pytest.mark.parametrize("url", config.Config.URLs_to_test_fr)
def test_meta_description(url, page: Page) -> None:
    page.set_default_timeout(100000)
    page.goto(url)
    data = reader.read_test_data(testdata, Action.get_current_test_name())
    meta_fr = data[6]
    webform_obj = Webform(page)
    webform_obj.meta_description_check('FR', meta_fr)

# @pytest.mark.webform
# @pytest.mark.parametrize("url", config.Config.URLs_to_test_fr)
# def test_img_alt_tags_fr(url, browser : Browser) -> None:  #playwright: Playwright - device viewport
#     #iphone_13 = playwright.devices['iPhone 13']
#     context = browser.new_context(
#         #record_video_dir= "video/",
#         #**iphone_13
#     )
#     page = context.new_page()
#     page.set_default_timeout(80000)
#     page.goto(url)
#     data = reader.read_test_data(testdata, Action.get_current_test_name())
#     logo_text_fr, brand_text_fr = data[7], data[8]
#     webform_obj = Webform(page)
#     webform_obj.check_img_alt_tags("brand", brand_text_fr)
#     webform_obj.check_img_alt_tags("logo", logo_text_fr)
#     page.close()

# @pytest.mark.webform
# @pytest.mark.parametrize("url", config.Config.URLs_to_test_fr)
# def test_href_lang(url, page: Page) -> None:
#     page.set_default_timeout(80000)
#     page.goto(url)
#     data = reader.read_test_data(testdata, Action.get_current_test_name())
#     href_en, href_fr = data[4], data[5]
#     webform_obj = Webform(page)
#     webform_obj.check_href_lang("EN", href_en)
#     webform_obj.check_href_lang("FR", href_fr)

# @pytest.mark.webform
# @pytest.mark.parametrize("url", config.Config.URLs_to_test_fr)
# def test_privacy_policy(url, page: Page) -> None:
#     page.set_default_timeout(300000)
#     page.goto(url)
#     webform_obj = Webform(page)
#     webform_obj.check_privacy_policy("FR")

# # @pytest.mark.webform
# # @pytest.mark.parametrize("url", config.Config.URLs_to_test_fr)
# # def test_form_page_fr(url, browser : Browser) -> None:
# #     context = browser.new_context(
# #         #record_video_dir= "video/"
# #     )
# #     page = context.new_page()
# #     page.set_default_timeout(80000)
# #     page.goto(url)
# #     data = reader.read_test_data(testdata_form, Action.get_current_test_name())
# #     firstname, emailid, verify_email, birthdate, thank_you_content_one, page_content_two, expected_url = data[0], data[1], data[2], data[3], data[13], data[14], data[15]
# #     webform_obj = Webform(page)
# #     action_obj = Action(page)
# #     webform_obj.webform_form(firstname, emailid, verify_email, birthdate, "")
# #     webform_obj.submit_button()
# #     action_obj.verify_current_url(expected_url)
# #     webform_obj.verify_thankyou_page_content(thank_you_content_one, page_content_two)
# #     page.close()

# @pytest.mark.webform # will update the code once new updates are deployed
# @pytest.mark.parametrize("url", config.Config.URLs_to_test_fr)
# def test_empty_form_fr(url, browser : Browser) -> None:
#     context = browser.new_context(
#         #record_video_dir= "video/"
#     )
#     page = context.new_page()
#     page.set_default_timeout(80000)
#     page.goto(url)
#     data = reader.read_test_data(testdata_form, Action.get_current_test_name())
#     name_error, email_error, verify_email_error, checkbox_error, recaptcha_error = data[4], data[5], data[6], data[7], data[8]
#     webform_obj = Webform(page)
#     webform_obj.submit_button()
#     webform_obj.error_messages_fields(name_error, email_error, verify_email_error, checkbox_error, recaptcha_error, 'empty')
#     page.close()

# @pytest.mark.webform
# @pytest.mark.parametrize("url", config.Config.URLs_to_test_fr)
# def test_form_invalid_data_fr(url, browser : Browser) -> None:
#     context = browser.new_context(
#         #record_video_dir= "video/"
#     )
#     page = context.new_page()
#     page.set_default_timeout(80000)
#     page.goto(url)
#     data = reader.read_test_data(testdata_form, Action.get_current_test_name())
#     firstname, emailid, verify_email, birthdate, name_error, email_error, verify_email_error, birthdate_error, recaptcha_error = data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7], data[8]
#     webform_obj = Webform(page)
#     webform_obj.webform_form(firstname, emailid, verify_email, birthdate, "")
#     webform_obj.submit_button()
#     webform_obj.error_messages_fields(name_error, email_error, verify_email_error, birthdate_error, recaptcha_error, 'invalid')
#     page.close()

# @pytest.mark.webform
# @pytest.mark.parametrize("url", config.Config.URLs_to_test_fr)
# def test_webform_links(url, browser : Browser) -> None:
#     context = browser.new_context(
#         #record_video_dir= "video/"
#     )
#     page = context.new_page()
#     page.set_default_timeout(300000)
#     page.goto(url)
#     webform_obj = Webform(page)
#     webform_obj.verify_links('FR')
#     page.close()

# @pytest.mark.webform
# @pytest.mark.parametrize("url", config.Config.URLs_to_test_fr_thankyou_page)
# def test_thankyou_page_url_fr(url, browser : Browser) -> None:
#     context = browser.new_context(
#         #record_video_dir= "video/"
#     )
#     page = context.new_page()
#     page.set_default_timeout(80000)
#     page.goto(url)
#     data = reader.read_test_data(testdata, Action.get_current_test_name())
#     expected_partial_url = data[0]
#     action_obj = Action(page)
#     action_obj.verify_current_url(expected_partial_url)
#     page.close()

# @pytest.mark.webform
# @pytest.mark.parametrize("url", config.Config.URLs_to_test_fr_thankyou_page)
# def test_thankyou_page_content_fr(url, browser : Browser) -> None:
#     context = browser.new_context(
#         #record_video_dir= "video/"
#     )
#     page = context.new_page()
#     page.set_default_timeout(80000)
#     page.goto(url)
#     data = reader.read_test_data(testdata, Action.get_current_test_name())
#     thank_you_content_one, page_content_two = data[16], data[17]
#     webform_obj = Webform(page)
#     webform_obj.verify_thankyou_page_content(thank_you_content_one, page_content_two)
#     page.close()

# # @pytest.mark.webform
# # @pytest.mark.parametrize("url", config.Config.URLs_to_test_fr)
# # def test_webform_content_fr(url, browser : Browser) -> None:
# #     context = browser.new_context(
# #         #record_video_dir= "video/"
# #     )
# #     page = context.new_page()
# #     page.set_default_timeout(80000)
# #     page.goto(url)
# #     data = reader.read_test_data(testdata, Action.get_current_test_name())
# #     content_one, content_two, checkbox_content, privacy_content_one, privacy_content_two, privacy_content_three, privacy_content_four = data[9], data[10], data[11], data[12], data[13], data[14], data[15]
# #     webform_obj = Webform(page)
# #     webform_obj.verify_webform_content("FR", content_one, content_two, checkbox_content, privacy_content_one, privacy_content_two, privacy_content_three, privacy_content_four)
# #     page.close()

# # @pytest.mark.webform
# # @pytest.mark.parametrize("url", config.Config.URLs_to_test_fr)
# # def test_dob_text_fr(url, browser : Browser) -> None:
# #     context = browser.new_context(
# #         #record_video_dir= "video/"
# #     )
# #     page = context.new_page()
# #     page.set_default_timeout(80000)
# #     page.goto(url)
# #     data = reader.read_test_data(testdata, Action.get_current_test_name())
# #     dob_content = data[18]
# #     webform_obj = Webform(page)
# #     webform_obj.verify_dob_content(dob_content)
# #     page.close()

# # @pytest.mark.webform
# # @pytest.mark.parametrize("url", config.Config.URLs_to_test_fr)
# # def test_form_page_generic_message_fr(url, browser : Browser) -> None:
# #     context = browser.new_context(
# #         #record_video_dir= "video/"
# #     )
# #     page = context.new_page()
# #     page.set_default_timeout(80000)
# #     page.goto(url)
# #     data = reader.read_test_data(testdata_form, Action.get_current_test_name())
# #     firstname, emailid, verify_email, recaptcha_error = data[0], data[1], data[2], data[8]
# #     webform_obj = Webform(page)
# #     webform_obj.webform_form(firstname, emailid, verify_email, "", "recaptcha")
# #     webform_obj.submit_button()
# #     webform_obj.recaptcha_error_check(recaptcha_error, "generic")
# #     page.close()

# # @pytest.mark.webform
# # @pytest.mark.parametrize("url", config.Config.URLs_to_test_fr)
# # def test_form_page_registered_error_message_fr(url, browser : Browser) -> None:
# #     context = browser.new_context(
# #         #record_video_dir= "video/"
# #     )
# #     page = context.new_page()
# #     page.set_default_timeout(80000)
# #     page.goto(url)
# #     data = reader.read_test_data(testdata_form, Action.get_current_test_name())
# #     firstname, emailid, verify_email, recaptcha_error = data[0], data[1], data[2], data[8]
# #     webform_obj = Webform(page)
# #     webform_obj.webform_form(firstname, emailid, verify_email, "", "recaptcha")
# #     webform_obj.submit_button()
# #     webform_obj.recaptcha_error_check(recaptcha_error, "registered")
# #     page.close()

# @pytest.mark.webform
# @pytest.mark.parametrize("url", config.Config.URLs_to_test_fr)
# def test_form_page_addresses_do_not_match_fr(url, browser : Browser) -> None:
#     context = browser.new_context(
#         #record_video_dir= "video/"
#     )
#     page = context.new_page()
#     page.set_default_timeout(80000)
#     page.goto(url)
#     data = reader.read_test_data(testdata_form, Action.get_current_test_name())
#     firstname, emailid, verify_email, email_error_text = data[0], data[1], data[2], data[6]
#     webform_obj = Webform(page)
#     webform_obj.webform_form(firstname, emailid, verify_email, "", "verify_email")
#     webform_obj.submit_button()
#     webform_obj.email_address_error_check(email_error_text)
#     page.close()

@pytest.mark.webform
@pytest.mark.parametrize("url", config.Config.URLs_to_test_fr_thankyou_page)
def test_href_lang(url, page: Page) -> None:
    page.set_default_timeout(100000)
    page.goto(url)
    data = reader.read_test_data(testdata, Action.get_current_test_name())
    href_en, href_fr = data[4], data[5]
    webform_obj = Webform(page)
    webform_obj.check_href_lang("EN", href_en)
    webform_obj.check_href_lang("FR", href_fr)     