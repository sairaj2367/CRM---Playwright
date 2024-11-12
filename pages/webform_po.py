import config
from playwright.sync_api import Playwright, sync_playwright, Page, BrowserContext, Browser, expect
from utils.actions import Action
from faker import Faker

class Webform:
    jnj_title_text = "Johnson and Johnson Inc."
    jnj_meta_text_fr = "Obtenez-en plus de la part de J&J Canada en devenant membre du Club Bons soins. Recevez des offres et de l'information exclusives directement dans votre boîte de réception, et l'accès à tous les nouveaux produits!"
    jnj_meta_text = "Get more out of JNJ Canada by signing up as a Care Club member. Get exclusive offers & education straight to your inbox with access to all product releases!"
    privacy_policy_data_en_p1 = "Your personal information will be governed by the Privacy Policy Open link in new window and will be used by Johnson & Johnson, Inc. (“Kenvue”), and its third party service providers inside and outside QC & Canada. You consent to the transfer of your data to jurisdictions outside your province and/or country of residence, which may have different data protection rules governing your personal information."
    privacy_policy_data_fr_p1 = "Vos renseignements personnels seront régis par notre Politique de confidentialité Open link in new window et seront utilisés par Johnson & Johnson Inc. (« Kenvue ») et ses tiers fournisseurs de services au Québec, au Canada et à l’étranger. Vous acceptez que vos données soient transférées vers des juridictions situées en dehors de votre province et/ou de votre pays de résidence, où les règles qui régissent la protection de vos renseignements personnels peuvent différer."
    privacy_policy_data_en_p2 = "You may opt-out of receiving emails from us at any time by following the unsubscribe instructions provided in any email message sent to you. Johnson & Johnson Inc., 88 McNabb Street, Markham, ON L3R 5L2, 1‑800‑265‑7323."
    privacy_policy_data_fr_p2 = "Vous pouvez refuser à tout moment de recevoir des courriels de notre part en suivant les instructions de désabonnement fournies dans tout message électronique qui vous est envoyé. Johnson & Johnson Inc., 88 McNabb Street, Markham, ON L3R 5L2, 1 800 265‑7323"


    def __init__(self, page : Page):
        self.page = page
        self.brand_name = page.get_attribute("meta[name='apple-mobile-web-app-title']", "content")
        self.meta_description = page.get_attribute("meta[name='description']", "content")
        self.logo_image = page.locator(".care-club-bar-logo img")
        self.brand_image = page.locator("#block-care-club-care-club-brands-block img")
        self.href_lang_en = page.locator("link[hreflang = 'en-CA']")
        self.href_lang_fr = page.locator("link[hreflang = 'fr-CA']")
        self.privacy_policy_en_p1 = page.locator(".careclub-form .careclub-warnings p:nth-child(2)")
        self.privacy_policy_en_p2 = page.locator(".careclub-form .careclub-warnings p:nth-child(3)")
        self.privacy_policy_data_link = page.locator('.careclub-warnings > p:nth-child(2) > a')
        self.first_name = page.locator("#edit-name")
        self.email = page.locator("#edit-email")
        self.verify_email = page.locator("#edit-confirm-email")
        self.birthdate = page.locator("#edit-birth-date")
        self.checkbox = page.locator("#edit-term")
        self.submit = page.locator(".careclub-form .form-submit")
        self.name_error = page.locator("div:nth-child(4) > .error-required")
        self.name_error_2 = page.locator("div:nth-child(3) > .error-required")
        self.email_error = page.locator("div:nth-child(5) > .error-required")
        self.email_error_2 = page.locator("div:nth-child(4) > .error-required")
        self.verify_email_error_message = page.locator("div:nth-child(6) > .error-required")
        self.verify_email_error_message_2 = page.locator("div:nth-child(5) > .error-required")
        self.checkbox_error_message_1 = page.locator("#edit-care-club .careclub-term .error-format")
        self.checkbox_error_message_2 = page.locator("div:nth-child(8) > .error-required")
        self.recaptcha_error_message = page.locator(".recaptcha-error")
        self.name_error_invalid = page.locator("div:nth-child(4) > .error-format")
        self.email_error_invalid = page.locator("div:nth-child(5) > .error-format")
        self.verify_email_error_message_invalid = page.locator("div:nth-child(6) > .error-format")
        self.birthdate_error_invalid = page.locator(".field-birthdate .error-format")
        self.name_error_invalid_2 = page.locator("div:nth-child(3) > .error-format")
        self.email_error_invalid_2 = page.locator("div:nth-child(4) > .error-format")
        self.verify_email_error_message_invalid_2 = page.locator("div:nth-child(5) > .error-format")
        self.terms_link = page.get_by_role("link", name="full terms and conditions.")
        self.terms_link_fr = page.get_by_role("link", name="conditions générales.")
        self.content_one = page.locator("#content-main")
        self.content_two = page.locator(".careclub-header p")
        self.checkbox_content = page.locator(".careclub-term label")
        self.privacy_content_one = page.locator(".careclub-warnings p:nth-child(2)")
        self.privacy_content_two = page.locator(".careclub-warnings p:nth-child(3)")
        self.privacy_content_three = page.locator(".careclub-warnings p:nth-child(4)")
        self.privacy_content_four = page.locator(".careclub-warnings p:nth-child(5)")
        self.page_content_two = page.locator(".main-row.region-row p:nth-child(1)")
        self.dob = page.locator(".field-birthdate em")
        self.dob_fr = page.locator(".field-birthdate i")
        self.page_content_two_2 = page.locator(".field--label-hidden p")
        self.page_content_two_3 = page.locator(".field--label-hidden p p")
        self.recaptcha_error_message_2 = page.locator("#submit-error")
        self.recaptcha_error_message_3 = page.locator("#email-registered-error")
        self.email_address_error_message = page.locator(".error-no-match")
        

    """
    Function to verify page titles
    """
    def verify_page_title(self, page_title):
        text = self.brand_name
        try:
            self.page.wait_for_timeout(10000)
            if text=="Johnson & Johnson Canada":
                page_title_modified = page_title + Webform.jnj_title_text
                print(f"Title verified to be : '{page_title_modified}'")
                expect(self.page).to_have_title(page_title_modified)
                print(f"Title verified to be : '{page_title_modified}'")
            elif text == "Quit Smoking with Our Products & Resources | NICORETTE®":
                page_title_modified = page_title + "NICORETTE®"
                expect(self.page).to_have_title(page_title_modified)
                print(f"Title verified to be : '{page_title_modified}'")
            elif text == "BENYLIN® Canada":
                page_title_modified = page_title + "BENYLIN®"
                expect(self.page).to_have_title(page_title_modified)
                print(f"Title verified to be : '{page_title_modified}'")
            elif text == "BAND-AID® Brand":
                page_title_modified = page_title + "BANDAID®"
                expect(self.page).to_have_title(page_title_modified)
                print(f"Title verified to be : '{page_title_modified}'")
            elif text == "Polysporin® Canada":
                page_title_modified = page_title + "POLYSPORIN®"
                expect(self.page).to_have_title(page_title_modified)
                print(f"Title verified to be : '{page_title_modified}'")
            elif text == "LISTERINE® Antiseptic Mouthwash, Rinse & Oral Care Products":
                page_title_modified = page_title + "LISTERINE®"
                expect(self.page).to_have_title(page_title_modified)
                print(f"Title verified to be : '{page_title_modified}'")
            elif text == "Johnson's® Baby":
                page_title_modified = page_title + "JOHNSON'S® Baby"
                expect(self.page).to_have_title(page_title_modified)
                print(f"Title verified to be : '{page_title_modified}'")
            elif text == "Marque BAND-AID®":
                page_title_modified = page_title + "BANDAID®"
                expect(self.page).to_have_title(page_title_modified)
                print(f"Title verified to be : '{page_title_modified}'")
            elif text == "CLEAN & CLEAR® Canada":
                page_title_modified = page_title + "CLEAN & CLEAR®"
                expect(self.page).to_have_title(page_title_modified)
                print(f"Title verified to be : '{page_title_modified}'")
            elif text == "Motrin":
                page_title_modified = page_title + "MOTRIN®"
                expect(self.page).to_have_title(page_title_modified)
                print(f"Title verified to be : '{page_title_modified}'")
            elif text == "PENATEN® Canada":
                page_title_modified = page_title + "PENATEN®"
                expect(self.page).to_have_title(page_title_modified)
                print(f"Title verified to be : '{page_title_modified}'")
            elif text == "PEPCID® Canada":
                page_title_modified = page_title + "PEPCID®"
                expect(self.page).to_have_title(page_title_modified)
                print(f"Title verified to be : '{page_title_modified}'")
            elif text == "Rogaine":
                page_title_modified = page_title + "ROGAINE®"
                expect(self.page).to_have_title(page_title_modified)
                print(f"Title verified to be : '{page_title_modified}'")
            elif text == "ROGAINE® Canada":
                page_title_modified = page_title + "ROGAINE®"
                expect(self.page).to_have_title(page_title_modified)
                print(f"Title verified to be : '{page_title_modified}'")
            elif text == "Cessez de fumer avec nos produits et ressources | NICORETTE®":
                page_title_modified = page_title + "NICORETTE®"
                expect(self.page).to_have_title(page_title_modified)
                print(f"Title verified to be : '{page_title_modified}'")
            elif text != "Johnson & Johnson Canada":
                page_title_modified = page_title + text
                expect(self.page).to_have_title(page_title_modified)
                print(f"Title verified to be : '{page_title_modified}'")
        except TimeoutError:
            print("Page title not verified")

    """
    Function to verify meta description
    """
    def meta_description_check(self, site, meta):
        try:
            if site == "EN":
                text = self.brand_name
                if text == "Johnson & Johnson Canada":
                    meta_desc = Webform.jnj_meta_text
                    if meta_desc == self.meta_description:
                        assert True, f"Meta description is as expected"
                        print("Meta description is as expected:", meta_desc)
                    else:
                        assert False, print(f"Meta description is not as expected: {meta_desc}")
                elif text == "Quit Smoking with Our Products & Resources | NICORETTE®":
                    meta_desc = "Get more out of NICORETTE® by signing up as a Care Club member. Get exclusive offers & education straight to your inbox with access to product releases!"   
                    if  meta_desc == self.meta_description:
                        assert True, f"Meta description is as expected"
                        print("Meta description is as expected:", meta_desc)
                    else:
                        assert False, print(f"Meta description is not as expected: {meta_desc}")
                elif text == "BENYLIN® Canada":
                        meta_desc = "Get more out of BENYLIN® by signing up as a Care Club member. Get exclusive offers & education straight to your inbox with access to product releases!"   
                        if  meta_desc == self.meta_description:
                            assert True, f"Meta description is as expected"
                            print("Meta description is as expected:", meta_desc)
                        else:
                            assert False, print(f"Meta description is not as expected: {meta_desc}")
                elif text == "Polysporin® Canada":
                        meta_desc = "Get more out of POLYSPORIN® by signing up as a Care Club member. Get exclusive offers & education straight to your inbox with access to product releases!"   
                        if  meta_desc == self.meta_description:
                            assert True, f"Meta description is as expected"
                            print("Meta description is as expected:", meta_desc)
                        else:
                            assert False, print(f"Meta description is not as expected: {meta_desc}")
                elif text == "LISTERINE® Antiseptic Mouthwash, Rinse & Oral Care Products":
                        meta_desc = "Get more out of LISTERINE® by signing up as a Care Club member. Get exclusive offers & education straight to your inbox with access to product releases!"  
                        if  meta_desc == self.meta_description:
                            assert True, f"Meta description is as expected"
                            print("Meta description is as expected:", meta_desc)
                        else:
                            assert False, print(f"Meta description is not as expected: {meta_desc}")
                elif text == "Johnson's® Baby":
                        meta_desc = "Get more out of JOHNSON'S® Baby by signing up as a Care Club member. Get exclusive offers & education straight to your inbox with access to product releases!"   
                        if  meta_desc == self.meta_description:
                            assert True, f"Meta description is as expected"
                            print("Meta description is as expected:", meta_desc)
                        else:
                            assert False, print(f"Meta description is not as expected: {meta_desc}")
                elif text == "BAND-AID® Brand":
                        meta_desc = "Get more out of BANDAID® by signing up as a Care Club member. Get exclusive offers & education straight to your inbox with access to product releases!"  
                        if  meta_desc == self.meta_description:
                            assert True, f"Meta description is as expected"
                            print("Meta description is as expected:", meta_desc)
                        else:
                            assert False, print(f"Meta description is not as expected: {meta_desc}")
                elif text == "Motrin":
                        meta_desc = "Get more out of MOTRIN® by signing up as a Care Club member. Get exclusive offers & education straight to your inbox with access to product releases!"   
                        if  meta_desc == self.meta_description:
                            assert True, f"Meta description is as expected"
                            print("Meta description is as expected:", meta_desc)
                        else:
                            assert False, print(f"Meta description is not as expected: {meta_desc}")
                elif text == "CLEAN & CLEAR® Canada":
                        meta_desc = "Get more out of CLEAN & CLEAR® by signing up as a Care Club member. Get exclusive offers & education straight to your inbox with access to product releases!"   
                        if  meta_desc == self.meta_description:
                            assert True, f"Meta description is as expected"
                            print("Meta description is as expected:", meta_desc)
                        else:
                            assert False, print(f"Meta description is not as expected: {meta_desc}")
                elif text == "PENATEN® Canada":
                        meta_desc = "Get more out of PENATEN® by signing up as a Care Club member. Get exclusive offers & education straight to your inbox with access to product releases!"   
                        if  meta_desc == self.meta_description:
                            assert True, f"Meta description is as expected"
                            print("Meta description is as expected:", meta_desc)
                        else:
                            assert False, print(f"Meta description is not as expected: {meta_desc}")
                elif text == "PEPCID® Canada":
                        meta_desc = "Get more out of PEPCID® by signing up as a Care Club member. Get exclusive offers & education straight to your inbox with access to product releases!"   
                        if  meta_desc == self.meta_description:
                            assert True, f"Meta description is as expected"
                            print("Meta description is as expected:", meta_desc)
                        else:
                            assert False, print(f"Meta description is not as expected: {meta_desc}")
                elif text == "ROGAINE® Canada":
                        meta_desc = "Get more out of ROGAINE® by signing up as a Care Club member. Get exclusive offers & education straight to your inbox with access to product releases!"   
                        if  meta_desc == self.meta_description:
                            assert True, f"Meta description is as expected"
                            print("Meta description is as expected:", meta_desc)
                        else:
                            assert False, print(f"Meta description is not as expected: {meta_desc}")
                elif text == "TYLENOL®":
                    meta_desc = "Looking to get more out of "+ text +"? Sign up to be a Care Club member to receive exclusive offers, personalized emails & access to new product releases."   
                    if  meta_desc == self.meta_description:
                        assert True, f"Meta description is as expected"
                        print("Meta description is as expected:", meta_desc)
                    else:
                        assert False, print(f"Meta description is not as expected: {meta_desc}")
                elif text != "Johnson & Johnson Canada":
                    meta_desc = "Get more out of "+ text +" by signing up as a Care Club member. Get exclusive offers & education straight to your inbox with access to product releases!"   
                    if  meta_desc == self.meta_description:
                        assert True, f"Meta description is as expected"
                        print("Meta description is as expected:", meta_desc)
                    else:
                        assert False, print(f"Meta description is not as expected: {meta_desc}")

            elif site == "FR":
                text = self.brand_name
                if text == "Johnson & Johnson Canada":
                    meta_desc_fr = Webform.jnj_meta_text_fr
                    if meta_desc_fr == self.meta_description:
                        assert True, f"Meta description is as expected"
                        print("Meta description is as expected:", meta_desc_fr)
                    else:
                        assert False, print(f"Meta description is not as expected: {meta_desc_fr}")
                elif text == "Cessez de fumer avec nos produits et ressources | NICORETTE®":
                        meta_desc_fr = meta + " " + "NICORETTE®" + "!"   
                        if  meta_desc_fr == self.meta_description:
                            assert True, f"Meta description is as expected"
                            print("Meta description is as expected:", meta_desc_fr)
                        else:
                            assert False, print(f"Meta description is not as expected: {meta_desc_fr}")
                elif text == "BENYLIN® Canada":
                        meta_desc_fr = meta + " " + "BENYLIN®" + "!"   
                        if  meta_desc_fr == self.meta_description:
                            assert True, f"Meta description is as expected"
                            print("Meta description is as expected:", meta_desc_fr)
                        else:
                            assert False, print(f"Meta description is not as expected: {meta_desc_fr}")
                elif text == "Polysporin® Canada":
                        meta_desc_fr = meta + " " + "POLYSPORIN®" + "!"   
                        if  meta_desc_fr == self.meta_description:
                            assert True, f"Meta description is as expected"
                            print("Meta description is as expected:", meta_desc_fr)
                        else:
                            assert False, print(f"Meta description is not as expected: {meta_desc_fr}")
                elif text == "LISTERINE® Antiseptic Mouthwash, Rinse & Oral Care Products":
                        meta_desc_fr = meta + " " + "LISTERINE®" + "!"   
                        if  meta_desc_fr == self.meta_description:
                            assert True, f"Meta description is as expected"
                            print("Meta description is as expected:", meta_desc_fr)
                        else:
                            assert False, print(f"Meta description is not as expected: {meta_desc_fr}")
                elif text == "Johnson's® Baby":
                        meta_desc_fr = meta + " " + "JOHNSON'S® Baby" + "!"   
                        if  meta_desc_fr == self.meta_description:
                            assert True, f"Meta description is as expected"
                            print("Meta description is as expected:", meta_desc_fr)
                        else:
                            assert False, print(f"Meta description is not as expected: {meta_desc_fr}")
                elif text == "Marque BAND-AID®":
                        meta_desc_fr = meta + " " + "BAND-AID®" + "!"   
                        if  meta_desc_fr == self.meta_description:
                            assert True, f"Meta description is as expected"
                            print("Meta description is as expected:", meta_desc_fr)
                        else:
                            assert False, print(f"Meta description is not as expected: {meta_desc_fr}")
                elif text == "Motrin":
                        meta_desc_fr = meta + " " + "MOTRIN®" + "!"   
                        if  meta_desc_fr == self.meta_description:
                            assert True, f"Meta description is as expected"
                            print("Meta description is as expected:", meta_desc_fr)
                        else:
                            assert False, print(f"Meta description is not as expected: {meta_desc_fr}")
                elif text == "CLEAN & CLEAR® Canada":
                        meta_desc_fr = meta + " " + "CLEAN & CLEAR®" + "!"   
                        if  meta_desc_fr == self.meta_description:
                            assert True, f"Meta description is as expected"
                            print("Meta description is as expected:", meta_desc_fr)
                        else:
                            assert False, print(f"Meta description is not as expected: {meta_desc_fr}")
                elif text == "PENATEN® Canada":
                        meta_desc_fr = meta + " " + "PENATEN®" + "!"   
                        if  meta_desc_fr == self.meta_description:
                            assert True, f"Meta description is as expected"
                            print("Meta description is as expected:", meta_desc_fr)
                        else:
                            assert False, print(f"Meta description is not as expected: {meta_desc_fr}")
                elif text == "PEPCID® Canada":
                        meta_desc_fr = meta + " " + "PEPCID®" + "!"   
                        if  meta_desc_fr == self.meta_description:
                            assert True, f"Meta description is as expected"
                            print("Meta description is as expected:", meta_desc_fr)
                        else:
                            assert False, print(f"Meta description is not as expected: {meta_desc_fr}")
                elif text == "Rogaine":
                        meta_desc_fr = meta + " " + "ROGAINE®" + "!"   
                        if  meta_desc_fr == self.meta_description:
                            assert True, f"Meta description is as expected"
                            print("Meta description is as expected:", meta_desc_fr)
                        else:
                            assert False, print(f"Meta description is not as expected: {meta_desc_fr}")
                elif text != "Johnson & Johnson Canada":
                    if text == "TYLENOL®":
                        meta_desc_fr = config.Config.meta_tylenol_fr + " " + text + "."   
                        if  meta_desc_fr == self.meta_description:
                            assert True, f"Meta description is as expected"
                            print("Meta description is as expected:", meta_desc_fr)
                        else:
                            assert False, print(f"Meta description is not as expected: {meta_desc_fr}")
                    else:
                        meta_desc_fr = meta + " " + text + "!"   
                        if  meta_desc_fr == self.meta_description:
                            assert True, f"Meta description is as expected"
                            print("Meta description is as expected:", meta_desc_fr)
                        else:
                            assert False, print(f"Meta description is not as expected: {meta_desc_fr}")
        except TimeoutError:
            print("Page title not verified")    

    """
    Function to verify image alt tag
    """

    def check_img_alt_tags(self,image_name, alt):
        try:
            if image_name == "logo":
                alt_text = self.logo_image.get_attribute('alt')
                print(alt_text)
                if alt_text == alt:
                    assert True
                    print(f"Image Alt Text: {alt_text}")
                else:
                    assert False, f"Image has no Alt Text."
        
            if image_name == "brand":
                alt_text = self.brand_image.get_attribute('alt')
                if alt_text == alt:
                    assert True
                    print(f"Image Alt Text: {alt_text}")
                else:
                    assert False, f"Image has no Alt Text."
        except TimeoutError:
            print("Timeout Error")
    """
    Function to verify href lang
    """
    def check_href_lang(self,site, href):
        if  site == "EN":
            href_text = self.href_lang_en.get_attribute('hreflang')
            if href_text == href:
                assert True
                print(f"href lang text is: {href_text}")
            else:
                assert False, f"href lang text not present."
        
        if  site == "FR":
            href_text = self.href_lang_fr.get_attribute('hreflang')
            if href_text == href:
                assert True
                print(f"href lang text is: {href_text}")
            else:
                assert False, f"href lang text not present."

    """
    Function to verify privacy policy content
    """

    def check_privacy_policy(self,site_name):
        try:
            text = self.brand_name
            if site_name == "EN":
                if text=="Johnson & Johnson Canada":
                    p_text1 = self.privacy_policy_en_p1
                    p_text2 = self.privacy_policy_en_p2
                    expect(p_text1).to_have_text(config.Config.jnj_careclub_privacy_data_en)
                    expect(p_text2).to_have_text(Webform.privacy_policy_data_en_p2)
                    print(f"Text is present and is correct: '{config.Config.jnj_careclub_privacy_data_en + Webform.privacy_policy_data_en_p2}'")
                else:
                    p_text1 = self.privacy_policy_en_p1
                    p_text2 = self.privacy_policy_en_p2
                    expect(p_text1).to_have_text(Webform.privacy_policy_data_en_p1)
                    expect(p_text2).to_have_text(Webform.privacy_policy_data_en_p2)
                    print(f"Text is present and is correct: '{Webform.privacy_policy_data_en_p1 + Webform.privacy_policy_data_en_p2}'")

            if site_name == "FR":
                if text=="Johnson & Johnson Canada":
                    p_text1 = self.privacy_policy_en_p1
                    p_text2 = self.privacy_policy_en_p2
                    expect(p_text1).to_have_text(config.Config.jnj_careclub_privacy_data_fr)
                    expect(p_text2).to_have_text(Webform.privacy_policy_data_fr_p2)
                    print(f"Text is present and is correct: '{config.Config.jnj_careclub_privacy_data_fr + Webform.privacy_policy_data_fr_p2}'")
                else:
                    p_text1 = self.privacy_policy_en_p1
                    p_text2 = self.privacy_policy_en_p2
                    expect(p_text1).to_have_text(Webform.privacy_policy_data_fr_p1)
                    expect(p_text2).to_have_text(Webform.privacy_policy_data_fr_p2)
                    print(f"Text is present and is correct: '{Webform.privacy_policy_data_fr_p1 + Webform.privacy_policy_data_fr_p2}'")
        except TimeoutError:
            print(f"Text not present.")

    """
    Function for form fields
    """
    def webform_form(self, name, email_id, email_verify, date, type):
        try:
            #firstname
            self.first_name.fill(name)

            if type == "recaptcha" or type == "verify_email":
                #email
                self.email.fill(email_id)

                #confirm email
                self.verify_email.fill(email_verify)
            else:
                #email
                fake = Faker()
                random_email = fake.email()
                self.email.fill(random_email)

                #confirm email
                self.verify_email.fill(random_email)
    
            #birthdate
            self.birthdate.fill(date)

            #checkbox
            check_box = self.checkbox
            check_box.highlight()
            check_box.check()  
        except TimeoutError:
                print(f"Timeout Error")

    """
    Function for submit buttom
    """
    def submit_button(self):
        try:
            #submit
            button = self.submit
            button.highlight()
            button.click()
        except TimeoutError:
                print(f"Timeout Error")
    
    """
    Function to verify form error messages for empty fields
    """
    def error_messages_fields(self, name_error, email_error, verify_email_error, checkbox_birthdate_error, recaptcha_error, type):
        brand = self.brand_name
        if type == 'empty':
            try:
                if brand == "Johnson & Johnson Canada":
                    #name
                    error_name = self.name_error
                    expect(error_name).to_have_text(name_error)
                    print(f"Error message is present and is correct: '{name_error}'")

                    #email
                    error_email = self.email_error
                    expect(error_email).to_have_text(email_error)
                    print(f"Error message is present and is correct: '{email_error}'")

                    #verify email
                    error_verify_email = self.verify_email_error_message
                    expect(error_verify_email).to_have_text(verify_email_error)
                    print(f"Error message is present and is correct: '{verify_email_error}'")

                    #checkbox
                    error_checkbox = self.checkbox_error_message_1
                    expect(error_checkbox).to_have_text(checkbox_birthdate_error)
                    print(f"Error message is present and is correct: '{checkbox_birthdate_error}'")
                else:
                    #name
                    error_name = self.name_error_2
                    expect(error_name).to_have_text(name_error)
                    print(f"Error message is present and is correct: '{name_error}'")

                    #email
                    error_email = self.email_error_2
                    expect(error_email).to_have_text(email_error)
                    print(f"Error message is present and is correct: '{email_error}'")

                    #verify email
                    error_verify_email = self.verify_email_error_message_2
                    expect(error_verify_email).to_have_text(verify_email_error)
                    print(f"Error message is present and is correct: '{verify_email_error}'")

                    #checkbox
                    error_checkbox = self.checkbox_error_message_2
                    expect(error_checkbox).to_have_text(checkbox_birthdate_error)
                    print(f"Error message is present and is correct: '{checkbox_birthdate_error}'")

                #recaptcha
                error_recaptcha = self.recaptcha_error_message
                expect(error_recaptcha).to_have_text(recaptcha_error)
                print(f"Error message is present and is correct: '{recaptcha_error}'")

            except TimeoutError:
                print(f"Error message not present.")
        
        if type == 'invalid': #need to update locator code
            brand = self.brand_name
            try:
                if brand == "Johnson & Johnson Canada":
                    #name
                    error_name = self.name_error_invalid
                    expect(error_name).to_have_text(name_error)
                    print(f"Error message is present and is correct: '{name_error}'")

                    #email
                    error_email = self.email_error_invalid
                    expect(error_email).to_have_text(email_error)
                    print(f"Error message is present and is correct: '{email_error}'")

                    #verify email
                    error_verify_email = self.verify_email_error_message_invalid
                    expect(error_verify_email).to_have_text(verify_email_error)
                    print(f"Error message is present and is correct: '{verify_email_error}'")
                else:
                    #name
                    error_name = self.name_error_invalid_2
                    expect(error_name).to_have_text(name_error)
                    print(f"Error message is present and is correct: '{name_error}'")

                    #email
                    error_email = self.email_error_invalid_2
                    expect(error_email).to_have_text(email_error)
                    print(f"Error message is present and is correct: '{email_error}'")

                    #verify email
                    error_verify_email = self.verify_email_error_message_invalid_2
                    expect(error_verify_email).to_have_text(verify_email_error)
                    print(f"Error message is present and is correct: '{verify_email_error}'")

                #birthdate
                birthdate_error = self.birthdate_error_invalid
                expect(birthdate_error).to_have_text(checkbox_birthdate_error)
                print(f"Error message is present and is correct: '{checkbox_birthdate_error}'")

                #recaptcha
                error_recaptcha = self.recaptcha_error_message
                expect(error_recaptcha).to_have_text(recaptcha_error)
                print(f"Error message is present and is correct: '{recaptcha_error}'")

            except TimeoutError:
                print(f"Error message not present.")
    
    """
    Function to verify links on webform
    """
    def verify_links(self, sitename):
        action_obj = Action(self.page)
            
        #privacy policy
        privacy_policy_en = self.privacy_policy_data_link
        href_link = privacy_policy_en.get_attribute('href')
        action_obj.new_tab_validate_url(privacy_policy_en, href_link)
        #self.page.go_back()

        if sitename == 'EN':
            #terms and conditions
            terms_link_en = self.terms_link
            href_link = terms_link_en.get_attribute('href')
            action_obj.new_tab_validate_url(terms_link_en, href_link)

        if sitename == 'FR':
            #terms and conditions
            terms_link_fr = self.terms_link_fr
            href_link = terms_link_fr.get_attribute('href')
            action_obj.new_tab_validate_url(terms_link_fr, href_link)

    """
    Function to verify webform content
    """
    def verify_webform_content(self, site, content_one, content_two, checkbox_content, privacy_content_one, privacy_content_two, privacy_content_three, privacy_content_four):
        try:
            brand = self.brand_name
            main_title = self.content_one
            expect(main_title).to_have_text(content_one)
            print(f"Text is present and is correct: '{content_one}'")

            textcontent_one = self.content_two
            expect(textcontent_one).to_have_text(content_two)
            print(f"Text is present and is correct: '{content_two}'")

            checkbox = self.checkbox_content
            expect(checkbox).to_have_text(checkbox_content)
            print(f"Text is present and is correct: '{checkbox_content}'")

            if site == "EN":
                privacy_text_one = self.privacy_content_one
                privacy_text = privacy_content_one + "1‑800‑265‑7323."
                expect(privacy_text_one).to_have_text(privacy_text)
                print(f"Text is present and is correct: '{privacy_text}'")
            
            elif site == "FR":
                privacy_text_one = self.privacy_content_one
                privacy_text = privacy_content_one + "1 800 265‑7323."
                expect(privacy_text_one).to_have_text(privacy_text)
                print(f"Text is present and is correct: '{privacy_text}'")

            if brand == "Johnson & Johnson Canada":
                if site == "EN":
                    privacy_text_two = self.privacy_content_two
                    expect(privacy_text_two).to_have_text(config.Config.jnj_careclub_privacy_data_en_new)
                    print(f"Text is present and is correct: '{config.Config.jnj_careclub_privacy_data_en_new}'")
                elif site == "FR":
                    privacy_text_two = self.privacy_content_two
                    expect(privacy_text_two).to_have_text(config.Config.jnj_careclub_privacy_data_fr_new)
                    print(f"Text is present and is correct: '{config.Config.jnj_careclub_privacy_data_fr_new}'")
            else:
                privacy_text_two = self.privacy_content_two
                expect(privacy_text_two).to_have_text(privacy_content_two)
                print(f"Text is present and is correct: '{privacy_content_two}'")

            privacy_text_three = self.privacy_content_three
            expect(privacy_text_three).to_have_text(privacy_content_three)
            print(f"Text is present and is correct: '{privacy_content_three}'")

            privacy_text_four = self.privacy_content_four
            expect(privacy_text_four).to_have_text(privacy_content_four)
            print(f"Text is present and is correct: '{privacy_content_four}'")
        except TimeoutError:
                print(f"Error message not present.")
    

    """
    Function to verify thank you page content
    """
    def verify_thankyou_page_content(self, thank_you_content_one, page_content_two):
        try:
            text = self.brand_name
            main_title = self.content_one
            expect(main_title).to_have_text(thank_you_content_one)
            print(f"Text is present and is correct: '{thank_you_content_one}'")

            if text == "CLEAN & CLEAR® Canada" or text == "SUDAFED®":
                content_two = self.page_content_two_2
                expect(content_two).to_have_text(page_content_two)
                print(f"Text is present and is correct: '{page_content_two}'")
            elif text == "BENADRYL®":
                content_two = self.page_content_two_3
                expect(content_two).to_have_text(page_content_two)
                print(f"Text is present and is correct: '{page_content_two}'")
            else:
                content_two = self.page_content_two
                expect(content_two).to_have_text(page_content_two)
                print(f"Text is present and is correct: '{page_content_two}'")

        except TimeoutError:
                print(f"Error message not present.")


    """
    Function to verify "facultative" text
    """
    def verify_dob_content(self, dob_content):
         try:
            dob_text = self.dob_fr
            expect(dob_text).to_have_text(dob_content)
            print(f"Text is present and is correct: '{dob_content}'")
         except TimeoutError:
                print(f"Error message not present.")

    """
    Function to verify "recaptcha" error text
    """
    def recaptcha_error_check(self, recaptcha_error, type):
         try:
            if type == "generic":
                #recaptcha
                error_recaptcha = self.recaptcha_error_message_2
                expect(error_recaptcha).to_have_text(recaptcha_error)
                print(f"Error message is present and is correct: '{recaptcha_error}'")
            elif type == "registered":
                error_recaptcha = self.recaptcha_error_message_3
                expect(error_recaptcha).to_have_text(recaptcha_error)
                print(f"Error message is present and is correct: '{recaptcha_error}'")
         except TimeoutError:
                print(f"Error message not present.")

    """
    Function to verify "email address" error text
    """
    def email_address_error_check(self, email_error_text):
         try:
            #recaptcha
            error_recaptcha = self.email_address_error_message
            expect(error_recaptcha).to_have_text(email_error_text)
            print(f"Error message is present and is correct: '{email_error_text}'")
         except TimeoutError:
                print(f"Error message not present.")              
            
            

    
            