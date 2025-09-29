

from Common_Packages.Base.basepage import Basepage
import Common_Packages.Utility.custom_logger as cl
from Techademy_Campus.Configuration.readProperties import ReadConfig

'''This page includes locators and functions of creating manual type of question bank under assessment repository for 
HOD and faculty role

    author: Vidyashri
    '''


class Questionbank(Basepage):
    log = cl.custom_logger()
    expected_result = ReadConfig.get_expected_result('Expected Results', 'question_bank_creation')
    expected_result_delete = ReadConfig.get_expected_result('Expected Results', 'delete_question_bank')
    expected_result_validate = ReadConfig.get_expected_result('Expected Results', 'question_bank_validation')

    def __init__(self, driver):
        super().__init__(driver)

        self.driver = driver

    # _dashboard_tab = "//span[text()='Dashboard']"
    _manage_tab = "//button[text()='Manage']"
    _programs_tab = "//span[text()='Programs']"
    _assessment_repository = "//span[text()='Assessment Repository']"
    _question_bank_name = "//input[@name='question_bank_name']"
    _enter_version = "//input[@name='version']"
    _course_name = "//input[@id='free-solo-2-demo']"
    _option_maths = "//li[text()='Mathematics – I  (ME1-01)']"
    _option_marine = "//li[text()='Marine Boilers  (ME4-15)']"
    _course_code = "//input[@name='course_code']"
    _question_bank_list = "//button[text()='Question Bank List']"
    _question_type = "//input[@name='questions[0].question_type']"
    _multiple_choice = "//li[text()='Multiple Choice']"
    _proficiency_level = "//input[@name='questions[0].proficiency_level']"
    _beginner = "//li[text()='Beginner']"
    _question_duration = "//input[@name='questions[0].duration']"
    _score = "//input[@name='questions[0].score']"
    _select_category = "//input[@name='questions[0].category']"
    _category1 = "//li[text()='Category-1']"
    _skill = "//input[@name='questions[0].skill']"
    _skill2 = "//li[text()='Skill-2']"
    _chapter_name = "//input[@name='questions[0].chapter']"
    _chapter_option = "//li[text()='Matrices']"
    _chapter_option_boiler = "//li[text()='Electric Boiler']"
    _mapped_co = "//input[@name='questions[0].mapped_co']"
    _mapped_pi = "//input[@name='questions[0].mapped_pi']"
    _question_text = "(//div[@data-placeholder='Type here'])[1]"
    _option1 = "//div[@data-placeholder='Option 1']"

    '2nd question'
    _add_another_question = "//button[text()='Add Another Question']"
    _question2 = "//input[@name='questions[1].question_type']"
    _fill_in_the_blanks = "//li[text()='Fill in the Blanks']"
    _proficiency_level2 = "//input[@name='questions[1].proficiency_level']"
    _beginner2 = "//li[text()='Beginner']"
    _question_duration2 = "//input[@name='questions[1].duration']"
    _score2 = "//input[@name='questions[1].score']"
    _select_category2 = "//input[@name='questions[1].category']"
    _category2 = "//li[text()='Category-1']"
    _skill2nd = "//input[@name='questions[1].skill']"
    _skill_2 = "//li[text()='Skill-2']"
    _chapter_name2 = "//input[@name='questions[1].chapter']"
    _chapter_option2 = "//li[text()='Matrices']"
    _chapter_option_boilers2 = "//li[text()='Electric Boiler']"
    _mapped_co2 = "//input[@name='questions[1].mapped_co']"
    _mapped_pi2 = "//input[@name='questions[1].mapped_pi']"
    _question_text2 = "(//div[@data-placeholder='Type here'])[2]"
    _answer_one = "//input[@name='questions[1].options[0].option_text']"
    _answer_two = "//input[@name='questions[1].options[1].option_text']"
    _answer_three = "//input[@name='questions[1].options[2].option_text']"
    _answer_four = "//input[@name='questions[1].options[3].option_text']"

    '3rd question'
    _clone_previous_question = "//button[text()='Clone Previous Question']"
    _question_text3 = "(//div[@data-placeholder='Type here'])[3]"
    _answer1 = "//input[@name='questions[2].options[0].option_text']"
    _answer2 = "//input[@name='questions[2].options[1].option_text']"
    _answer3 = "//input[@name='questions[2].options[2].option_text']"
    _answer4 = "//input[@name='questions[2].options[3].option_text']"
    _save = "//button[text()='Save']"
    _actual_result = "//div[text()='Question bank created successfully.']"

    # delete created question bank
    _3dots = ("(//button[@class='MuiButtonBase-root MuiIconButton-root MuiIconButton-sizeMedium qa-student-elipses "
              "css-1rtdwbw'])[2]")
    _delete = "//span[@class='MuiTypography-root MuiTypography-body1 MuiListItemText-primary css-17vjt6s']"
    _submit = "//button[text()='Submit']"
    _actual_result_delete = "//div[text()='Question bank deleted successfully.']"

    # validate question bank
    _validate_question_bank = "//button[text()='Validate Question Bank']"
    _view = "(//a[text()='view'])[1]"
    _evaluate = "//button[text()='Evaluate']"
    _action = "//input[@name='action']"
    _approve = "//li[text()='Approve']"
    _description = "//textarea[@name='description']"
    _actual_result_validate = "//div[text()='Evaluation Updated Successfully.']"

    def click_on_manage(self):
        self.element_click(self._manage_tab, "xpath")

    def click_on_programs(self):
        self.element_click(self._programs_tab, "xpath")

    def click_on_assessment_repository(self):
        self.wait_for_element(self._assessment_repository, "xpath")
        self.element_click_js(self._assessment_repository, "xpath")

    def enter_question_bank_name(self, question_bank_name):
        self.send_keys(question_bank_name, self._question_bank_name, "xpath")

    def enter_version(self, version):
        self.send_keys(version, self._enter_version, "xpath")

    def select_course_name(self):
        self.send_keys("Mathematics – I  (ME1-01)", self._course_name, "xpath")
        self.element_click_js(self._option_maths, "xpath")

    def select_course_name_marine(self):
        self.send_keys("Marine Boilers  (ME4-15)", self._course_name, "xpath")
        self.element_click_js(self._option_marine, "xpath")

    def enter_course_code(self, course_code):
        self.send_keys(course_code, self._course_code, "xpath")

    def select_question_type(self):
        self.element_click_js(self._question_type, "xpath")
        self.element_click_js(self._multiple_choice, "xpath")

    def select_proficiency_level(self):
        self.element_click_js(self._proficiency_level, "xpath")
        self.element_click_js(self._beginner, "xpath")

    def enter_duration(self, duration, locator):
        self.send_keys(duration, locator, "xpath")

    def enter_score(self, score, locator):
        self.send_keys(score, locator, "xpath")

    def select_category(self):
        self.element_click_js(self._select_category, "xpath")
        self.element_click_js(self._category1, "xpath")

    def select_skill(self):
        self.element_click_js(self._skill, "xpath")
        self.element_click_js(self._skill2, "xpath")

    def select_chapter_name(self, name):
        name_select = f"//li[normalize-space()='{name}']"
        self.element_click_js(self._chapter_name, "xpath")
        self.element_click_js(name_select, "xpath")

    def enter_mapped_co(self, co, locator):
        self.send_keys(co, locator, "xpath")

    def enter_mapped_pi(self, pi, locator):
        self.send_keys(pi, locator, "xpath")

    def enter_question_text(self, question_text, locator):
        self.send_keys(question_text, locator, "xpath")

    def enter_option1(self, option1):
        self.send_keys(option1, self._option1, "xpath")

    # 2nd Question

    def click_on_add_another_question(self):
        self.element_click_js(self._add_another_question, "xpath")

    def select_question_type2(self):
        self.element_click_js(self._question2, "xpath")
        self.element_click_js(self._fill_in_the_blanks, "xpath")

    def select_proficiency_level2(self):
        self.element_click_js(self._proficiency_level2, "xpath")
        self.element_click_js(self._beginner2, "xpath")

    def select_category2(self):
        self.element_click_js(self._select_category2, "xpath")
        self.element_click_js(self._category2, "xpath")

    def select_skill2(self):
        self.element_click_js(self._skill2nd, "xpath")
        self.element_click_js(self._skill_2, "xpath")

    def select_chapter_name2(self, name):
        name_select = f"//li[normalize-space()='{name}']"
        self.element_click_js(self._chapter_name2, "xpath")
        self.element_click_js(name_select, "xpath")

    def enter_answer(self, answer, locator):
        self.send_keys(answer, locator, "xpath")

    # 3rd question
    def click_on_clone_previous_question(self):
        self.element_click_js(self._clone_previous_question, "xpath")

    def click_on_save(self):
        self.element_click_js(self._save, "xpath")

    def click_on_question_bank_list(self):
        self.element_click_js(self._question_bank_list, "xpath")

        # delete created question bank

    def click_on_3dots(self):
        self.element_click_js(self._3dots, "xpath")

    def click_on_delete(self):
        self.element_click_js(self._delete, "xpath")

    def click_on_submit(self):
        self.element_click_js(self._submit, "xpath")

        # Validate question bank

    def click_on_validate_question_bank(self):
        self.wait_for_element(self._validate_question_bank, "xpath")
        self.element_click_js(self._validate_question_bank, "xpath")

    def click_on_view(self):
        self.element_click_js(self._view, "xpath")

    def click_on_evaluate(self):
        self.element_click_js(self._evaluate, "xpath")

    def select_action(self):
        self.element_click_js(self._action, "xpath")
        self.element_click_js(self._approve, "xpath")

    def enter_description(self, description):
        self.send_keys(description, self._description, "xpath")

    def navigate_to_manage_tab(self):
        self.click_on_manage()
        self.click_on_assessment_repository()

    def create_question_bank_fac(self, question_bank_name, version, course_code, duration, score, co, pi, question_text,
                                 option1, answer1, answer2, answer3, answer4):
        self.enter_question_bank_name(question_bank_name)
        self.enter_version(version)
        self.select_course_name()
        self.enter_course_code(course_code)
        self.select_question_type()
        self.select_proficiency_level()
        self.enter_duration(duration, self._question_duration)
        self.enter_score(score, self._score)
        self.web_scroll("down")
        self.select_category()
        self.select_skill()
        self.select_chapter_name("Vector Calculus")
        self.enter_mapped_co(co, self._mapped_co)
        self.enter_mapped_pi(pi, self._mapped_pi)
        self.enter_question_text(question_text, self._question_text)
        self.enter_option1(option1)
        self.click_on_add_another_question()
        self.select_question_type2()
        self.select_proficiency_level2()
        self.enter_duration(duration, self._question_duration2)
        self.enter_score(score, self._score2)
        self.web_scroll("down")
        self.select_category2()
        self.select_skill2()
        self.select_chapter_name2("Vector Calculus")
        self.enter_mapped_co(co, self._mapped_co2)
        self.enter_mapped_pi(pi, self._mapped_pi2)
        self.enter_question_text(question_text, self._question_text2)
        self.enter_answer(answer1, self._answer_one)
        self.enter_answer(answer2, self._answer_two)
        self.enter_answer(answer3, self._answer_three)
        self.enter_answer(answer4, self._answer_four)
        self.click_on_clone_previous_question()
        self.enter_question_text(question_text, self._question_text3)
        self.enter_answer(answer1, self._answer1)
        self.enter_answer(answer2, self._answer2)
        self.enter_answer(answer3, self._answer3)
        self.enter_answer(answer4, self._answer4)
        self.click_on_save()

    def create_question_bank_hod(self, question_bank_name, version, course_code, duration, score, co, pi, question_text,
                                 option1, answer1, answer2, answer3, answer4):
        self.enter_question_bank_name(question_bank_name)
        self.enter_version(version)
        self.select_course_name_marine()
        self.enter_course_code(course_code)
        self.select_question_type()
        self.select_proficiency_level()
        self.enter_duration(duration, self._question_duration)
        self.enter_score(score, self._score)
        self.web_scroll("down")
        self.select_category()
        self.select_skill()
        self.select_chapter_name("Electric Boiler")
        self.enter_mapped_co(co, self._mapped_co)
        self.enter_mapped_pi(pi, self._mapped_pi)
        self.enter_question_text(question_text, self._question_text)
        self.enter_option1(option1)
        self.click_on_add_another_question()
        self.select_question_type2()
        self.select_proficiency_level2()
        self.enter_duration(duration, self._question_duration2)
        self.enter_score(score, self._score2)
        self.web_scroll("down")
        self.select_category2()
        self.select_skill2()
        self.select_chapter_name2("Electric Boiler")
        self.enter_mapped_co(co, self._mapped_co2)
        self.enter_mapped_pi(pi, self._mapped_pi2)
        self.enter_question_text(question_text, self._question_text2)
        self.enter_answer(answer1, self._answer_one)
        self.enter_answer(answer2, self._answer_two)
        self.enter_answer(answer3, self._answer_three)
        self.enter_answer(answer4, self._answer_four)
        self.click_on_clone_previous_question()
        self.enter_question_text(question_text, self._question_text3)
        self.enter_answer(answer1, self._answer1)
        self.enter_answer(answer2, self._answer2)
        self.enter_answer(answer3, self._answer3)
        self.enter_answer(answer4, self._answer4)
        self.click_on_save()

    def delete_question_bank(self):
        self.click_on_question_bank_list()
        self.click_on_3dots()
        self.click_on_delete()
        self.click_on_submit()

    def validate_question_bank(self, description):
        self.refresh_page()
        self.click_on_validate_question_bank()
        self.click_on_view()
        self.web_scroll("down")
        self.click_on_evaluate()
        self.select_action()
        self.enter_description(description)
        self.click_on_submit()

    def verify_question_bank_creation(self):
        self.verify_by_comparing_text(locator=self._actual_result, locator_type="xpath",
                                      expected_result=self.expected_result,
                                      result_msg="Question bank created successfully.")

    def verify_delete_question_bank(self):
        self.verify_by_comparing_text(locator=self._actual_result_delete, locator_type="xpath",
                                      expected_result=self.expected_result_delete,
                                      result_msg="Question bank deleted successfully.")

    def verify_validate_question_bank(self):
        self.verify_by_comparing_text(locator=self._actual_result_validate, locator_type="xpath",
                                      expected_result=self.expected_result_validate,
                                      result_msg="Evaluation Updated Successfully.")
