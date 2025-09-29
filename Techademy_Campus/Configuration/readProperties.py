import configparser
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
config = configparser.RawConfigParser()
property = configparser.RawConfigParser()
test = str(BASE_DIR)
config.read(test + "//configuration//configs.ini")


# config.read("C:/Users/GS-2155/PycharmProjects/pythonProject3/Configurations/logging.config")
# config.read("../Configurations/logging.config")"

class ReadConfig:
    @staticmethod
    def get_login(section, opt):
        login = config.get(section, opt)
        return login


    @staticmethod
    def get_onboard_student_details(section, opt):
        onboard_student = config.get(section, opt)
        return onboard_student

    @staticmethod
    def get_event(section, opt):
        event = config.get(section, opt)
        return event

    @staticmethod
    def get_holiday(section, opt):
        holiday = config.get(section, opt)
        return holiday

    @staticmethod
    def get_expected_result(section, opt):
        expected_result = config.get(section, opt)
        return expected_result

    @staticmethod
    def get_badge(section, opt):
        badge = config.get(section, opt)
        return badge

    @staticmethod
    def get_my_repository(section, opt):
        my_repository = config.get(section, opt)
        return my_repository

    @staticmethod
    def get_feedback(section, opt):
        feedback = config.get(section, opt)
        return feedback

    @staticmethod
    def get_peer_group_interaction(section, opt):
        peer_group_interaction = config.get(section, opt)
        return peer_group_interaction

    @staticmethod
    def get_prospectus_and_application_form(section, opt):
        prospectus_and_application_form = config.get(section, opt)
        return prospectus_and_application_form

    @staticmethod
    def get_university_vision(section, opt):
        university_vision = config.get(section, opt)
        return university_vision

    @staticmethod
    def get_university_mission(section, opt):
        university_mission = config.get(section, opt)
        return university_mission

    @staticmethod
    def get_reg_username():
        username = config.get('registrar info', 'username')
        return username

    @staticmethod
    def get_reg_password():
        password = config.get('registrar info', 'password')
        return password

    @staticmethod
    def get_HR_username():
        username = config.get('hr info', 'HR_username')
        return username

    @staticmethod
    def get_HR_password():
        password = config.get('hr info', 'HR_password')
        return password

    @staticmethod
    def get_HOD_username():
        username = config.get('hod info', 'HOD_username')
        return username

    @staticmethod
    def get_HOD_password():
        password = config.get('hod info', 'HOD_password')
        return password

    @staticmethod
    def get_Fac_username():
        username = config.get('faculty info', 'Fac_username')
        return username

    @staticmethod
    def get_Fac_password():
        password = config.get('faculty info', 'Fac_password')
        return password

    @staticmethod
    def get_Stud_username():
        username = config.get('student info', 'Stud_username')
        return username

    @staticmethod
    def get_Stud_password():
        password = config.get('student info', 'Stud_password')
        return password

    @staticmethod
    def get_Mooc_username():
        username = config.get('MoocAdmin info', 'Mooc_username')
        return username

    @staticmethod
    def get_Mooc_password():
        password = config.get('MoocAdmin info', 'Mooc_password')
        return password

    @staticmethod
    def get_abc_id():
        abc_id = config.get('ABC ID', 'abc_id')
        return abc_id


    @staticmethod
    def get_SC_Title():
        title = config.get('Student Connect info', 'title')
        return title

    @staticmethod
    def get_SC_Description():
        description = config.get('Student Connect info', 'description')
        return description

    @staticmethod
    def get_search_student():
        search_student = config.get('Student Connect info', 'search_student')
        return search_student

    @staticmethod
    def get_ClusterName():
        cluster = config.get('CreateExam info', 'cluster')
        return cluster

    @staticmethod
    def get_DepartmentName():
        department = config.get('CreateExam info', 'department')
        return department

    @staticmethod
    def get_ProgramName():
        program = config.get('CreateExam info', 'program')
        return program

    @staticmethod
    def getExamTitle():
        title = config.get('CreateExam info', 'exam_title')
        return title

    @staticmethod
    def getExamStartDate():
        s_date = config.get('CreateExam info', 'exam_start_date')
        return s_date

    @staticmethod
    def getExamEndDate():
        e_date = config.get('CreateExam info', 'exam_end_date')
        return e_date

    @staticmethod
    def getResultPublishOn():
        result = config.get('CreateExam info', 'result_publish_on')
        return result

    @staticmethod
    def getDiscussionTitle():
        title = config.get('DiscussionBoard info', 'title')
        return title

    @staticmethod
    def getDiscussionDesc():
        desc = config.get('DiscussionBoard info', 'desc')
        return desc

    @staticmethod
    def getPollOneOption():
        poll_one = config.get('DiscussionBoard info', 'poll_one')
        return poll_one

    @staticmethod
    def getSearchRoleValue():
        search_role = config.get('Search Role info', 'search_role')
        return search_role

    @staticmethod
    def getEditedRDesc():
        editRDesc = config.get('Edit UserRole info', 'editRDesc')
        return editRDesc

    @staticmethod
    def getPollTwoOption():
        poll_two = config.get('DiscussionBoard info', 'poll_two')
        return poll_two

    @staticmethod
    def getRoleName():
        role_name = config.get('Create UserRole info', 'role_name')
        return role_name

    @staticmethod
    def getRoleDesc():
        role_desc = config.get('Create UserRole info', 'role_desc')
        return role_desc

    @staticmethod
    def getGroupName():
        group_name = config.get('Create UserGroup info', 'group_name')
        return group_name

    @staticmethod
    def getGroupDesc():
        group_desc = config.get('Create UserGroup info', 'group_desc')
        return group_desc

    @staticmethod
    def getEditedGDesc():
        editGDesc = config.get('Edit UserGroup info', 'editGDesc')
        return editGDesc

    @staticmethod
    def get_notificationName():
        name = config.get('CreateNotification info', 'notification_name')
        return name

    @staticmethod
    def getFirstName():
        f_name = config.get('Create User info', 'f_name')
        return f_name

    @staticmethod
    def getLastName():
        l_name = config.get('Create User info', 'l_name')
        return l_name

    @staticmethod
    def getMobileNumber():
        phone = config.get('Create User info', 'phone')
        return phone

    @staticmethod
    def getEmailID():
        email = config.get('Create User info', 'email')
        return email

    @staticmethod
    def get_notificationDesc():
        desc = config.get('CreateNotification info', 'notification_desc')
        return desc

    @staticmethod
    def getSearchUserValue():
        search_user = config.get('Search User info', 'search_user')
        return search_user

    @staticmethod
    def getChapterName():
        chapter_name = config.get('Add Chapter info', 'chapter_name')
        return chapter_name

    @staticmethod
    def getChapterObjective():
        chapter_objective = config.get('Add Chapter info', 'chapter_objective')
        return chapter_objective

    @staticmethod
    def getEditedObjective():
        edited_objective = config.get('Edit Chapter info', 'edited_objective')
        return edited_objective

    @staticmethod
    def getPhysicalPracticalTitle():
        practical_title = config.get('Create PhysicalPractical info', 'practical_title')
        return practical_title

    @staticmethod
    def getPhysicalPracticalDescription():
        practical_description = config.get('Create PhysicalPractical info', 'practical_description')
        return practical_description

    @staticmethod
    def getPracticalDate():
        practical_date = config.get('Create PhysicalPractical info', 'practical_date')
        return practical_date

    @staticmethod
    def getPracticalStartTime():
        start_time = config.get('Create PhysicalPractical info', 'start_time')
        return start_time

    @staticmethod
    def getPracticalEndTime():
        end_time = config.get('Create PhysicalPractical info', 'end_time')
        return end_time

    @staticmethod
    def getPracticalLocation():
        location = config.get('Create PhysicalPractical info', 'location')
        return location

    @staticmethod
    def getVLabTitle():
        VLab_title = config.get('Create VirtualLab info', 'VLab_title')
        return VLab_title

    @staticmethod
    def getVLabDescription():
        VLab_description = config.get('Create VirtualLab info', 'VLab_description')
        return VLab_description

    @staticmethod
    def getVLabDate():
        VLab_date = config.get('Create VirtualLab info', 'VLab_date')
        return VLab_date

    @staticmethod
    def getVLabStartTime():
        VLab_stime = config.get('Create VirtualLab info', 'VLab_stime')
        return VLab_stime

    @staticmethod
    def getVLabEndTime():
        VLab_etime = config.get('Create VirtualLab info', 'VLab_etime')
        return VLab_etime

    @staticmethod
    def getVirtualLabEndDate():
        end_date = config.get('Create VirtualLab info', 'end_date')
        return end_date

    @staticmethod
    def getDate():
        mm_dd_yyyy = config.get('Add Chapter info', 'mm_dd_yyyy')
        return mm_dd_yyyy

    @staticmethod
    def getCourseCost():
        cost = config.get('Affiliate Course info', 'cost')
        return cost

    @staticmethod
    def getCourseCreditPoints():
        credit_points = config.get('Affiliate Course info', 'credit_points')
        return credit_points

    @staticmethod
    def getOnlSessionTitle():
        onl_session_title = config.get('Create OnlineSession info', 'onl_session_title')
        return onl_session_title

    @staticmethod
    def getOnlSessionDescription():
        onl_session_description = config.get('Create OnlineSession info', 'onl_session_description')
        return onl_session_description

    @staticmethod
    def getSessionTopic():
        topic = config.get('Create OnlineSession info', 'topic')
        return topic

    @staticmethod
    def getSessionDate():
        session_date = config.get('Create OnlineSession info', 'session_date')
        return session_date

    @staticmethod
    def getSessionStartTime():
        onl_session_stime = config.get('Create OnlineSession info', 'onl_session_stime')
        return onl_session_stime

    @staticmethod
    def getSessionEndTime():
        onl_session_etime = config.get('Create OnlineSession info', 'onl_session_etime')
        return onl_session_etime

    @staticmethod
    def getSessionMeetLink():
        meet_link = config.get('Create OnlineSession info', 'meet_link')
        return meet_link

    @staticmethod
    def getSessionPassword():
        meet_password = config.get('Create OnlineSession info', 'meet_password')
        return meet_password

    @staticmethod
    def getOffSessionTitle():
        off_session_title = config.get('Create OfflineSession info', 'off_session_title')
        return off_session_title

    @staticmethod
    def getOffSessionDescription():
        off_session_description = config.get('Create OfflineSession info', 'off_session_description')
        return off_session_description

    @staticmethod
    def getOffSessionTopic():
        topic = config.get('Create OfflineSession info', 'topic')
        return topic

    @staticmethod
    def getOffSessionDate():
        session_date = config.get('Create OfflineSession info', 'session_date')
        return session_date

    @staticmethod
    def getOffSessionStartTime():
        off_session_stime = config.get('Create OfflineSession info', 'off_session_stime')
        return off_session_stime

    @staticmethod
    def getOffSessionEndTime():
        off_session_etime = config.get('Create OfflineSession info', 'off_session_etime')
        return off_session_etime

    @staticmethod
    def getSessionVenue():
        venue = config.get('Create OfflineSession info', 'venue')
        return venue

    @staticmethod
    def getHybSessionTitle():
        hyb_session_title = config.get('Create HybridSession info', 'hyb_session_title')
        return hyb_session_title

    @staticmethod
    def getHybSessionDescription():
        hyb_session_description = config.get('Create HybridSession info', 'hyb_session_description')
        return hyb_session_description

    @staticmethod
    def getHybSessionTopic():
        topic = config.get('Create HybridSession info', 'topic')
        return topic

    @staticmethod
    def getHybSessionDate():
        session_date = config.get('Create HybridSession info', 'session_date')
        return session_date

    @staticmethod
    def getHybSessionStartTime():
        hyb_session_stime = config.get('Create HybridSession info', 'hyb_session_stime')
        return hyb_session_stime

    @staticmethod
    def getHybSessionEndTime():
        hyb_session_etime = config.get('Create HybridSession info', 'hyb_session_etime')
        return hyb_session_etime

    @staticmethod
    def getHybSessionMeetLink():
        meet_link = config.get('Create HybridSession info', 'meet_link')
        return meet_link

    @staticmethod
    def getHybSessionPassword():
        meet_password = config.get('Create HybridSession info', 'meet_password')
        return meet_password

    @staticmethod
    def getHybSessionVenue():
        venue = config.get('Create HybridSession info', 'venue')
        return venue

    @staticmethod
    def getInteractionTitle():
        title = config.get('Interaction info', 'title')
        return title

    @staticmethod
    def getInteractionDesc():
        desc = config.get('Interaction info', 'desc')
        return desc

    @staticmethod
    def getPollOne_Option():
        poll_one = config.get('Interaction info', 'poll_one')
        return poll_one

    @staticmethod
    def getPollTwo_Option():
        poll_two = config.get('Interaction info', 'poll_two')
        return poll_two

    @staticmethod
    def getReadingTitle():
        reading_title = config.get('ReadingFile info', 'reading_title')
        return reading_title

    @staticmethod
    def getVideoTitle():
        UploadVideo_title = config.get('UploadVideoFile info', 'UploadVideo_title')
        return UploadVideo_title

    @staticmethod
    def getAddVideoTitle():
        AddVideo_title = config.get('AddVideoLink info', 'AddVideo_title')
        return AddVideo_title

    @staticmethod
    def getAddVideoLink():
        AddVideo_link = config.get('AddVideoLink info', 'AddVideo_link')
        return AddVideo_link

    @staticmethod
    def getUploadAssignmentTitle():
        assignment_title = config.get('AddAssignment info', 'assignment_title')
        return assignment_title

    @staticmethod
    def getUploadAssignmentMarks():
        assignment_marks = config.get('AddAssignment info', 'assignment_marks')
        return assignment_marks

    @staticmethod
    def getUploadAssignmentDescription():
        assignment_description = config.get('AddAssignment info', 'assignment_description')
        return assignment_description

    @staticmethod
    def getUploadAssignmentHours():
        assignment_hours = config.get('AddAssignment info', 'assignment_hours')
        return assignment_hours

    @staticmethod
    def getUploadAssignmentMinutes():
        assignment_minutes = config.get('AddAssignment info', 'assignment_minutes')
        return assignment_minutes

    @staticmethod
    def getUploadAssignmentGuideline():
        guideline = config.get('AddAssignment info', 'guideline')
        return guideline
      
    @staticmethod
    def getAddVideoLink():
        AddVideo_link = config.get('AddVideoLink info', 'AddVideo_link')
        return AddVideo_link

    @staticmethod
    def get_answer(section, opt):
        answer = config.get(section, opt)
        return answer

    @staticmethod
    def get_appdescription():
        description = config.get('Assessment repository', 'description')
        return description

    @staticmethod
    def get_expected_result(section, opt):
        expected_result = config.get(section, opt)
        return expected_result

    @staticmethod
    def get_question_bank_name():
        question_bank_name = config.get('Assessment repository', 'question_bank_name')
        return question_bank_name

    @staticmethod
    def get_version():
        version = config.get('Assessment repository', 'version')
        return version

    @staticmethod
    def get_course_code():
        course_code = config.get('Assessment repository', 'course_code')
        return course_code

    @staticmethod
    def get_duration():
        duration = config.get('Assessment repository', 'duration')
        return duration

    @staticmethod
    def get_score():
        score = config.get('Assessment repository', 'score')
        return score

    @staticmethod
    def get_mapped_co():
        co = config.get('Assessment repository', 'co')
        return co

    @staticmethod
    def get_mapped_pi():
        pi = config.get('Assessment repository', 'pi')
        return pi

    @staticmethod
    def get_question_text():
        question_text = config.get('Assessment repository', 'question_text')
        return question_text

    @staticmethod
    def get_option1():
        option1 = config.get('Assessment repository', 'option1')
        return option1

    @staticmethod
    def get_evaluation_feedback():
        feedback = config.get('Evaluation', 'feedback')
        return feedback

    @staticmethod
    def get_evaluation_points():
        points = config.get('Evaluation', 'points')
        return points

