from Common_Packages.Base.basepage import Basepage


class JobCandidates(Basepage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver



    #Locators

    _add_candidate = "//button[contains(text(), 'Add Candidates')]"
    _skills = "//label[contains(text(), 'Skills')]//parent::div//input[@type='text']"
    _keywords = "//label[contains(text(), 'Keywords')]//parent::div//input[@type='text']"
    _min_experience = "//label[contains(text(), 'Min Years')]//parent::div//div//input"
    _mx_experience = "//label[contains(text(), 'Max Years')]//parent::div//div//input"
    _location = "//label[contains(text(), 'Location')]//parent::div//div//input"
    _search = "//button[contains(text(), 'Search')]"
    _cancel = "//button[contains(text(), 'Cancel')]"
    _candidate = "//button[contains(text(), 'Chetan')]"


    def click_add_candidates(self):
        self.wait_for_element(self._add_candidate, locator_type="xpath")
        self.element_click_js(self._add_candidate, locator_type="xpath")
        self.wait_for_page_load()

    def enter_skills(self, skill):
        self.wait_for_element(self._add_candidate, locator_type="xapth")
        self.sendkeys_multi_value(skill, self._skills, locator_type="xpath")
        self.wait_for_page_load()

    def enter_keywords(self, keyword):
        self.wait_for_element(self._add_candidate, locator_type="xapth")
        self.sendkeys_multi_value(keyword, self._skills, locator_type="xpath")
        self.wait_for_page_load()


    def enter_min_exp(self, min_exp):
        self.wait_for_element(self._add_candidate, locator_type="xapth")
        self.send_keys(min_exp, self._skills, locator_type="xpath")
        self.wait_for_page_load()

    def enter_max_exp(self, max_exp):
        self.wait_for_element(self._add_candidate, locator_type="xapth")
        self.send_keys(max_exp, self._skills, locator_type="xpath")
        self.wait_for_page_load()

    def enter_location(self, location):
        self.wait_for_element(self._add_candidate, locator_type="xapth")
        self.send_keys(location, self._skills, locator_type="xpath")
        self.wait_for_page_load()

    def click_search(self):
        self.wait_for_element(self._search, locator_type="xpath")
        self.element_click_js(self._search, locator_type="xpath")
        self.wait_for_page_load()

    def click_cancel(self):
        self.wait_for_element(self._cancel, locator_type="xpath")
        self.element_click_js(self._cancel, locator_type="xpath")
        self.wait_for_page_load()

    def  shortlist_candidate_for_Job(self, skills, keyword, min_exp, max_exp, location):
        self.click_add_candidates()
        self.enter_skills(skills)
        # self.enter_keywords(keyword)
        # self.enter_max_exp(max_exp)
        # self.enter_location(location)
        self.click_search()
        self.wait_for_element(self._candidate, locator_type="xpath")
        return self.get_text(self._candidate, locator_type="xpath")
