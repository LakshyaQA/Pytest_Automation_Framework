import time

import Common_Packages.Utility.custom_logger as cl
from Common_Packages.Base.basepage import Basepage


class Chapter(Basepage):
    log = cl.custom_logger()

    '''
        This class includes the adding/editing/deleting of the chapter for a subject.
        
        author: Abhilash
        
        '''

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # locators for adding, editing and deleting the chapter

    manage_tab = "//button[@id='basic-button']"
    Department_option = "//span[text()='Department']"
    ViewDetails_button = "//button[text()='View Details']"
    AddSymbol = "//button[text()='+ Add']"
    ChapterName_textfield = "//input[@name='chapter_name']"
    Objective_textfield = "//textarea[@name='objective']"
    Conditions = "//label[text()='Condition']"
    ReleaseOn = "//li[text()='Release On']"
    DateEntry = "//input[@type='tel']"
    AddChapter_button = "//button[text()='Add Chapter']"
    ThreeDots = "(//button[@id='long-button'])[2]"
    EditOption = "//span[text()='Edit']"
    UpdateButton = "//button[text()='Update Chapter']"
    DeleteOption = "//span[text()='Delete']"
    DeleteButton = "//button[text()='Delete']"
    add_success_message = "//div[text()='Chapter added successfully']"
    edit_success_message = "//div[text()='Chapter updated successfully']"
    delete_success_message = "//div[text()='Chapter deleted successfully']"

    def clickOnManageTab(self):
        self.wait_for_element(self.manage_tab, locator_type="xpath")
        self.element_click_js(self.manage_tab, "xpath")

    def clickOnDepartment(self):
        self.wait_for_element(self.Department_option, locator_type="xpath")
        self.element_click_js(self.Department_option, "xpath")

    def clickOnViewDetails(self):
        self.wait_for_element(self.ViewDetails_button, locator_type="xpath")
        self.element_click_js(self.ViewDetails_button, "xpath")

    def clickOnAddSymbol(self):
        self.wait_for_element(self.AddSymbol, locator_type="xpath")
        self.element_click_js(self.AddSymbol, "xpath")

    def clickOnChapterName(self):
        self.wait_for_element(self.ChapterName_textfield, locator_type="xpath")
        self.element_click_js(self.ChapterName_textfield, "xpath")

    def enterChapterName(self, chapter_name):
        self.send_keys(chapter_name, self.ChapterName_textfield, "xpath")

    def clickOnChapterObjective(self):
        self.wait_for_element(self.Objective_textfield, locator_type="xpath")
        self.element_click_js(self.Objective_textfield, "xpath")

    def enterChapterObjective(self, chapter_objective):
        self.send_keys(chapter_objective, self.Objective_textfield, "xpath")

    def selectCondition(self):
        self.wait_till_element_invisibility(self.Conditions, locator_type="xpath")
        self.element_click_js(self.Conditions, "xpath")
        self.wait_for_element(self.ReleaseOn, "xpath")
        self.element_click_js(self.ReleaseOn, "xpath")

    def clickOnDateField(self):
        self.wait_for_element(self.DateEntry, locator_type="xpath")
        self.element_click_js(self.DateEntry, "xpath")

    def enterDateMonYear(self, mm_dd_yyyy):
        self.send_keys(mm_dd_yyyy, self.DateEntry, "xpath")

    def clickOnAddChapter(self):
        self.wait_for_element(self.AddChapter_button, locator_type="xpath")
        self.element_click_js(self.AddChapter_button, "xpath")
        time.sleep(1)

    def clickOnThreeDots(self):
        self.wait_for_element(self.ThreeDots, locator_type="xpath")
        self.element_click_js(self.ThreeDots, "xpath")

    def clickOnEditOption(self):
        self.wait_for_element(self.EditOption, locator_type="xpath")
        self.element_click_js(self.EditOption, "xpath")

    def clickOnChapter_Objective(self):
        self.wait_for_element(self.Objective_textfield, locator_type="xpath")
        self.element_click_js(self.Objective_textfield, "xpath")

    def editChapterObjective(self, edited_objective):
        self.send_keys(" " + edited_objective, self.Objective_textfield, "xpath")

    def clickOnUpdateChapterButton(self):
        self.wait_for_element(self.UpdateButton, locator_type="xpath")
        self.element_click_js(self.UpdateButton, "xpath")
        time.sleep(1)

    def clickOn_ThreeDots(self):
        self.wait_for_element(self.ThreeDots, locator_type="xpath")
        self.element_click_js(self.ThreeDots, "xpath")

    def clickOnDeleteOption(self):
        self.wait_for_element(self.DeleteOption, locator_type="xpath")
        self.element_click_js(self.DeleteOption, "xpath")

    def clickOnDeleteButton(self):
        self.wait_for_element(self.DeleteButton, locator_type="xpath")
        self.element_click_js(self.DeleteButton, "xpath")
        time.sleep(1)

    def adding_the_Chapter(self, chapter_name, chapter_objective):
        self.clickOnManageTab()
        self.clickOnDepartment()
        self.clickOnViewDetails()
        self.clickOnAddSymbol()
        self.clickOnChapterName()
        self.enterChapterName(chapter_name)
        self.clickOnChapterObjective()
        self.enterChapterObjective(chapter_objective)
        self.clickOnAddChapter()
        time.sleep(2)

    def editing_the_Chapter(self, edited_objective):
        self.clickOnThreeDots()
        self.clickOnEditOption()
        self.clickOnChapterObjective()
        self.editChapterObjective(edited_objective)
        self.clickOnUpdateChapterButton()
        time.sleep(2)

    def deleting_the_Chapter(self):
        self.clickOn_ThreeDots()
        self.clickOnDeleteOption()
        self.clickOnDeleteButton()
        time.sleep(2)

