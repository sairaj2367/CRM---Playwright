import config
import inspect
from playwright.sync_api import Playwright, sync_playwright, Page, Browser, expect


class Action:
    def __init__(self, page : Page):
        self.page = page
        self.cookieCloseButton = page.locator("#popup-buttons .agree-button")
        self.brand_name = page.get_attribute("meta[name='apple-mobile-web-app-title']", "content")


    def verify_current_url(self, expected_partial_url):
        try:
            self.page.wait_for_timeout(1000)
            current_url = self.page.url
            assert expected_partial_url in current_url, f"Expected '{expected_partial_url}' to be present in URL, but it is not. Current URL: {current_url}"
            print(f"URL verified to contain : '{expected_partial_url}'")
        except TimeoutError:
            print(f"URL did not contain '{expected_partial_url}'")

    @classmethod
    def get_current_test_name(cls):
        frame = inspect.currentframe().f_back
        method_name = frame.f_code.co_name
        return method_name
    

    """
    Function to navigate to new tab
    """
    def new_tab_validate_url(self, obj, url):
        obj.highlight()
        with self.page.expect_popup() as new:
            obj.click()
            new_page = new.value
            try:
                if url == config.Config.privacy_policy_link_en:
                    assert True
                    print(f"Link navigates to correct url:'{url}'")
                elif url == config.Config.terms_condition_link_en:
                    assert True
                    print(f"Link navigates to correct url:'{url}'")
                elif url == config.Config.privacy_policy_link_fr:
                    assert True
                    print(f"Link navigates to correct url:'{url}'")
                elif url == config.Config.terms_condition_link_fr:
                    assert True
                    print(f"Link navigates to correct url:'{url}'")
                elif url == config.Config.privacy_policy_link_fr_jnj:
                    assert True
                    print(f"Link navigates to correct url:'{url}'")
                elif url == config.Config.privacy_policy_link_en_jnj:
                    assert True
                    print(f"Link navigates to correct url:'{url}'")
                else:
                    expect(new_page).to_have_url(url)
                    print(f"Link navigates to correct url:'{url}'")
            except TimeoutError:
                print("URL is incorrect")
    

    """
    Function to close cookie pop-up
    """
    def closeCookiePopup(self):
        try:
            text = self.brand_name
            if text == "CLEAN & CLEAR® Canada":
                print(f"No cookie banner displayed")
            else:
                #submit
                button = self.cookieCloseButton
                self.page.mouse.down()
                button.highlight()
                button.click()
        except TimeoutError:
                print(f"Timeout Error")