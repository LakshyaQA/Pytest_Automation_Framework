import Common_Packages.Utility.custom_logger as cl
from Common_Packages.Base.basepage import Basepage


class Job(Basepage):
    log = cl.custom_logger()


    def __init__(self, driver):
       super().__init__(driver)
       self.driver = driver


    #Locators

    _post_a_job = "//button[contains(text(), 'Post a Job')]"
    _view_details = "//h5[contains(text(), 'QA-Automation Script')]//parent::div//parent::div//parent::div//parent::div//button[contains(text(), 'View Details')]"
    _candidate_tab = "//button[contains(text(), 'Candidates')]"
    _approved_job_details = "//span[contains(text(), 'Approved')]//parent::div//parent::div//parent::div//parent::div//button"
    _loader = "//div[@class='MuiBackdrop-root loader css-xuaqpw']"





    def click_post_a_job(self):
        self.wait_for_element(self._post_a_job, locator_type="xpath")
        self.element_click_js(self._post_a_job, locator_type="xpath")
        self.wait_for_page_load()

    def click_view_details(self):
        self.wait_for_element(self._view_details, locator_type="xpath")
        self.element_click_js(self._view_details, locator_type="xpath")
        self.wait_for_page_load()


    def click_candidate_tab(self):
        self.wait_till_element_invisibility(self._loader, "xpath")
        self.wait_for_element(self._candidate_tab, locator_type="xpath")
        self.element_click(self._candidate_tab, locator_type="xpath")
        self.wait_for_page_load()

    def click_view_details_approved_job(self):
        self.wait_for_element(self._approved_job_details, locator_type="xpath")
        self.element_click_js(self._approved_job_details, locator_type="xpath")
        self.wait_for_page_load()